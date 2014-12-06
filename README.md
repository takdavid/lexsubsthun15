lexsubsthun15
=============

Experiments on the *lexical substitution* task in Hungarian, for the MSZNY 2015 conference.

Install
-------
```
git clone --recursive git@github.com:takdavid/lexsubsthun15.git
cd lexsubsthun15
./setup.sh
```

**Do not forget** the `./setup.sh` command, it downloads and sets up the required tools.

Corpus
------

To run the trainings with `./train.sh`, copy corpus files to the `corpus/*` subdirectories.

Evaluation
----------

The `./eval.sh` runs our experiments on the goldstandard corpus, evaluates them with the SemDis script, and prints the results.
