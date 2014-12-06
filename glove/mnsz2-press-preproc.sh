#!/bin/bash
set -e
home=`dirname $0`
home=`cd $home; pwd`
cd $home/glove

make

CORPUS=$home/../corpus/mnsz2_only/press.clean.txt
VOCAB_FILE=$home/tmp/mnsz2-press-vocab.txt
COOCCURRENCE_FILE=$home/tmp/mnsz2-press-cooccurrence.bin
COOCCURRENCE_SHUF_FILE=$home/tmp/mnsz2-press-cooccurrence.shuf.bin
VERBOSE=2
MEMORY=16.0
VOCAB_MIN_COUNT=5
WINDOW_SIZE=15

if [ ! -f $VOCAB_FILE ]; then
    time ./vocab_count -min-count $VOCAB_MIN_COUNT -verbose $VERBOSE < $CORPUS > $VOCAB_FILE
fi
if [ ! -f $COOCCURRENCE_FILE ]; then
    time ./cooccur -memory $MEMORY -vocab-file $VOCAB_FILE -verbose $VERBOSE -window-size $WINDOW_SIZE < $CORPUS > $COOCCURRENCE_FILE
fi
if [ ! -f $COOCCURRENCE_SHUF_FILE ]; then
    time ./shuffle -memory $MEMORY -verbose $VERBOSE < $COOCCURRENCE_FILE > $COOCCURRENCE_SHUF_FILE
fi

