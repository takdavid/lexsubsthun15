import sys
sys.path.append('danielfrg')
import os
os.environ['PATH'] += ':mikolov'
import word2vec
word2vec.word2clusters('../corpus/mnsz2_only/press.clean.txt', 'tmp/press.clusters.txt', 100, verbose=True)

