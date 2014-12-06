#!/bin/bash
set -e
home=`dirname $0`
home=`cd $home; pwd`
cd $home/glove

CORPUS=$home/../corpus/mnsz2_only/press.clean.txt
VOCAB_FILE=$home/tmp/mnsz2-press-vocab.txt
COOCCURRENCE_FILE=$home/tmp/mnsz2-press-cooccurrence.bin
COOCCURRENCE_SHUF_FILE=$home/tmp/mnsz2-press-cooccurrence.shuf.bin
SAVE_FILE=$home/tmp/mnsz2-press-vectors-200
VERBOSE=2
MEMORY=4.0
VOCAB_MIN_COUNT=5
VECTOR_SIZE=200
MAX_ITER=10
WINDOW_SIZE=15
BINARY=2
NUM_THREADS=8
X_MAX=10

time ./glove -save-file $SAVE_FILE -threads $NUM_THREADS -input-file $COOCCURRENCE_SHUF_FILE -x-max $X_MAX -iter $MAX_ITER -vector-size $VECTOR_SIZE -binary $BINARY -vocab-file $VOCAB_FILE -verbose $VERBOSE

