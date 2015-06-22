set -e

home=`dirname $0`
home=`cd $home; pwd`

git submodule init
git submodule update

if [ ! -d virtualenv ]; then
    virtualenv virtualenv
fi
. virtualenv/bin/activate

# word2vec/mikolov
cd $home
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
cd $home

# word2vec/danielfrg
cd $home
if [ ! -d word2vec/danielfrg ]; then
    git clone git@github.com:danielfrg/word2vec.git word2vec/danielfrg
fi
cd word2vec/danielfrg
python setup.py install
cd $home

# custom word2vec scripts
pip install argparse

# glove
cd $home
if [ ! -d glove/glove ]; then
    curl http://www-nlp.stanford.edu/software/glove.tar.gz >glove/tmp/glove.tar.gz
    cd glove
    tar -xvzf tmp/glove.tar.gz glove/
    set +e
    patch -t -s -N glove/makefile -i makefile.patch
    set -e
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
