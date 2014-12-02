set -e

git submodule init
git submodule update

if [ ! -d word2vec/mikolov ]; then
    svn checkout http://word2vec.googlecode.com/svn/trunk/ word2vec/mikolov
fi
if [ "$(uname)" == "Darwin" ]; then 
    set +e
    patch -t -s -N word2vec/mikolov/word-analogy.c -i word2vec/word-analogy.c.patch
    patch -t -s -N word2vec/mikolov/distance.c -i word2vec/distance.c.patch
    patch -t -s -N word2vec/mikolov/compute-accuracy.c -i word2vec/compute-accuracy.c.patch
    set -e
fi
cd word2vec/mikolov
make
cd -

echo
echo OK!

