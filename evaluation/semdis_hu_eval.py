#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module computes the measures defined by the Semdis 2014
lexical substitution task for French

http://www.irit.fr/semdis2014
"""

__author__ = "Tim Van de Cruys, Ludovic Tanguy"
__version__ = "0.3"

import re
import sys
import argparse
import warnings

class SemdisEvaluation(object):
    """Main class that contains the evaluation measures. Class is
    initialized with gold standard, test file is evaluated using the
    function 'evaluate'"""

    def __init__(self, goldFile):
        self.goldFile = goldFile
        self.goldDict, self.sumAnswerDict = self.__parseGoldStandard()
        self.normalizationMapping = self.__parseNormalizationMapping('mapping.txt')

    def __parseNormalizationMapping(self, mappingFile):
        normalizationMapping = {}
        # regex for mapping rules
        mappingPattern = re.compile(r'^([\w ]+)\((\w+\.[a-z])\)-->([\w ]+)$', re.UNICODE)
        for line in open(mappingFile):
            line = line.decode('utf8').rstrip()
            mappingMatch = re.match(mappingPattern, line)
            try:
                lexeltId = mappingMatch.group(2)
                proposedForm = mappingMatch.group(1)
                normalizedForm = mappingMatch.group(3)
            except AttributeError:
                #ignore comment lines
                continue
            # mappings in dictionary of dictionaries
            try:
                normalizationMapping[lexeltId][proposedForm] = normalizedForm
            except KeyError:
                normalizationMapping[lexeltId] = {}
                normalizationMapping[lexeltId][proposedForm] = normalizedForm
        return normalizationMapping

    def __parseGoldStandard(self):
        goldDict = {}
        sumAnswerDict = {}

        # define some useful regular expressions
        splitPattern1 = re.compile(r' :: ')
        idPattern = re.compile(r'(\w+) ([0-9]+)', re.UNICODE)
        answerPattern = re.compile(r'(.*) ([0-9]+)', re.UNICODE)

        for line in open(self.goldFile):
            #also strip off possible ";" at end of line
            line = line.decode('utf8').strip().rstrip(';')

            # split on " :: "
            left,right = re.split(splitPattern1, line)
            idMatch = re.match(idPattern, left)
            # (word, numberid) tuple as key
            keyTuple = (idMatch.group(1), int(idMatch.group(2)))
            goldDict[keyTuple] = {}

            answerList = right.split(';')
            answerList = [answer.strip() for answer in answerList]
            answerTupleList = []

            # extract answers as (word, frequency) tuples
            # multiword expressions are left as they are
            sumAnswers = 0
            for answer in answerList:
                answerMatch = re.match(answerPattern, answer)
                answerTuple = (answerMatch.group(1),int(answerMatch.group(2)))
                # each item in goldDict contains dictionary with answer as key
                # and frequency as value
                goldDict[keyTuple][answerTuple[0]] = answerTuple[1]
                sumAnswers += answerTuple[1]
            # in addition, sumAnswerDict contains items with the sum off
            # all answer frequencies as value
            sumAnswerDict[keyTuple] = sumAnswers
        return goldDict, sumAnswerDict 

    def __parseTestFile(self, testFile, normalize=True):
        testDict = {}

        splitPattern1 = re.compile(r' :: ')
        idPattern = re.compile(r'(\w+) ([0-9]+)', re.UNICODE)

        compliantFlag = True
        for line in open(testFile):
            line = line.decode('utf8').strip().rstrip(';')

            # split on " :: "
            try:
                left,right = re.split(splitPattern1, line)
            except ValueError:
                #possible empty list - in that case line ends with
                #double semicolon
                if line.endswith('::'):
                    #if id matches, include id with empty answerlist
                    idMatch = re.match(idPattern, line)
                    try:
                        # (word, numberid) tuple as key
                        keyTuple = (idMatch.group(1), int(idMatch.group(2)))
                    except AttributeError:                    
                        raise ValueError('Wrong file format')
                    testAnswerList = []
            else:
                idMatch = re.match(idPattern, left)
                try:
                    # (word, numberid) tuple as key
                    keyTuple = (idMatch.group(1), int(idMatch.group(2)))
                except AttributeError:
                    raise ValueError('Wrong file format')
                else:
                    testDict[keyTuple] = {}

                testAnswerList = right.split(';')
                testAnswerList = [answer.strip() for answer in testAnswerList]
                #when normalize flag is on, answers are mapped to their normalized form
                if self.normalizationMapping.has_key(keyTuple[0]) and normalize:
                    for i,answer in enumerate(testAnswerList):
                        if self.normalizationMapping[keyTuple[0]].has_key(answer):
                            testAnswerList[i] = self.normalizationMapping[keyTuple[0]][answer]
                    #normalizing might cause duplicates
                    #we want to remove duplicates, but preserve the order of the list
                    testAnswerSet = set()
                    newTestAnswerList = []
                    for answer in testAnswerList:
                        if answer in testAnswerSet:
                            continue
                        testAnswerSet.add(answer)
                        newTestAnswerList.append(answer)
                    testAnswerList = newTestAnswerList
                if not len(testAnswerList) == len(set(testAnswerList)):
                    warnings.warn('Some items contain duplicates, which is not allowed')
            if not len(testAnswerList) == 10:
                warnings.warn('Some items do not contain 10 guesses - or wrong file format; trying to proceed anyway')
            testDict[keyTuple] = testAnswerList
        return testDict

    def evaluate(self, testFile, metric, normalize):
        testDict = self.__parseTestFile(testFile, normalize)

        #print '\nEvaluating', len(testDict), 'instances..\n'

        if metric == 'all':
            self.__best(testDict)
            self.__oot(testDict)
        elif metric == 'best':
            self.__best(testDict)
        elif metric == 'oot':
            self.__oot(testDict)
        elif metric == 'detail':
            self.__detail(testDict)    
        else:
            raise NotImplementedError('Unsupported evaluation method')

    def __best(self,testDict):
        sumNumerator = 0
        for key, valueList in testDict.items():
            # if empty valuelist, score for this item is zero, so we
            # continue
            if not valueList or key not in self.goldDict:
                continue
            else:
                bestAnswer = valueList[0]
                if self.goldDict[key].has_key(bestAnswer):
                    score = self.goldDict[key][bestAnswer] / float(self.sumAnswerDict[key])
                    sumNumerator += score
        print 'Best score:', sumNumerator / float(len(testDict))

    def __oot(self,testDict):
        sumNumerator = 0
        for key, valueList in testDict.items():
            # if empty valuelist, score for this item is zero, so we
            # continue
            if not valueList or key not in self.goldDict:
                continue
            else:
                allScore = 0
                if len(valueList) > 10:
                    warnings.warn('Some items contain more than 10 guesses - only taking first 10 into account')
                    valueList = valueList[0:10]
                for answer in valueList:
                    if self.goldDict[key].has_key(answer):
                        score = self.goldDict[key][answer]
                        allScore += score
                sumNumerator += allScore / float(self.sumAnswerDict[key])
        print 'OOT score: ', sumNumerator / float(len(testDict))

    def __detail (self, testDict):
        #Gives details for each sentence (ID, lexelt, number of
        #proposed words, score for best word,  oot score)

        #file name used as submission name
        name=args.testfile
        name=re.sub("^.*\/", "",name)
        name=re.sub("\..*?$","",name) 
        print "ID\tlexelt\t",name+"-Nreponses","\t",name+"-Best","\t",name+"-OOT"
        for key, valueList in sorted(testDict.items()):
            if not valueList or key not in self.goldDict:
                continue
            try:
                bestAnswer = valueList[0]
            except IndexError:
                bestAnswer = ''
            bestScore = float(0)
            if self.goldDict[key].has_key(bestAnswer):
                bestScore = self.goldDict[key][bestAnswer] / float(self.sumAnswerDict[key])
            allScore = float(0)
            for answer in valueList:
                if self.goldDict[key].has_key(answer):
                    score = self.goldDict[key][answer]
                    allScore += score
            ootScore= allScore / float(self.sumAnswerDict[key])
            print key[1],"\t", key[0].encode('utf8'), "\t", len(valueList), "\t", bestScore, "\t", ootScore


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This script calculates \
    the evaluation measures for the Semdis 2014 lexical substitution task for French \
    - http://www.irit.fr/semdis2014/')
    parser.add_argument('-g','--goldfile', help='Gold standard file',required=True)
    parser.add_argument('-t','--testfile',help='File with test results', required=True)
    parser.add_argument('-m','--measure',help='One of "best", "oot", "all", "detail" (default = all)',
                        required=False, default='all')
    parser.add_argument('-nn','--nonormalize',help='Do not apply normalization mapping',
                        required=False, action="store_false")
    args = parser.parse_args()
 
    s = SemdisEvaluation(args.goldfile)
    s.evaluate(args.testfile,args.measure,args.nonormalize)
