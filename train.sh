set -e
cd corpus/mnsz2_only
python clean_by_domain.py
cd -

cd word2vec/mikolov
time ./word2vec -train ../../corpus/mnsz2_only/press.clean.txt -output press.bin -cbow 1 -size 200 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 20 -binary 1 -iter 15
cd -

cd glove/
./mnsz2-press-preproc.sh
./mnsz2-press-50.sh
./mnsz2-press-200.sh

