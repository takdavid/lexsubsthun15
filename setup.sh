set -e

home=`dirname $0`
home=`cd $home; pwd`
echo home $home

git submodule init
git submodule update

# word2vec/mikolov
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

# word2vec/danielfrg
cd word2vec/danielfrg
python setup.py install
cd -

#glove
cd $home
if [ ! -d glove/glove ]; then
    curl http://www-nlp.stanford.edu/software/glove.tar.gz >glove/tmp/glove.tar.gz
    cd glove
    tar -xvzf tmp/glove.tar.gz glove/
    cd -
fi
cd glove/glove
make
cd $home

# glove/maciejkula
cd $home
if [ ! -d glove/maciejkula ]; then
    git clone git@github.com:maciejkula/glove-python.git glove/maciejkula
    if [ "$(uname)" == "Darwin" ]; then 
        brew install gcc49
        brew install capnp
    fi
    CFLAGS='-stdlib=libc++' pip install pycapnp
    pip install -U cython
    pip install -U setuptools
fi
cd glove/maciejkula
python setup.py install || echo "ERROR setting up maciejkula/glove"
cd $home

echo
echo OK
