# encoding: utf-8
import argparse
import glob
import sys
sys.path.append('danielfrg')
import candidates
candidates.load()

def print_output(key, words):
    s = key + ' ' + '; '.join(words)
    print s.encode('utf-8')

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True)
parser.add_argument('-m', '--method', required=False, default='')
args = parser.parse_args()
method = vars(candidates)[args.method]
#files = ['../../evaluation/evaltest.txt']
#files = ['../../evaluation/hybrid.txt']
files = [args.file]
for fn in files:
    with open(fn, 'r') as f:
        for (i, s) in enumerate(f.readlines()):
            i+=1
            s = s.decode('utf-8')
            parts = s.split('::')
            if len(parts) == 3:
                sentence = parts[0]+' '+parts[2]
                candi = parts[1]
            else:
                sentence = ' '.join(parts)
                candi = ''
            sent = candidates.clean_sentence(sentence)
            candidates.set_candidates_now(*candidates.clean_sentence(candi))
            (key, words) = candidates.splitkey(*sent)
            method(*words)
            try:
                print_output(key, method(*words))
            except:
                print_output(key, [])

