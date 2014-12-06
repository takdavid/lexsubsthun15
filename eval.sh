cd word2vec
evaldir=../evaluation
resultsdir=tmp
for config in veconly hybrid; do
    for method in bestcosinecontext bestl2context averagecontext cosine; do
        echo $config $method
        python run-evaltest.py -m $method -f $evaldir/$config.txt >$resultsdir/results.$config.$method.txt
    done
done
cd -

cd evaluation
resultsdir=../word2vec/tmp
for config in veconly hybrid; do
    for method in bestcosinecontext bestl2context averagecontext cosine; do
        for measure in all; do #best oot; do
            echo $config $method $measure
            python semdis_hu_eval.py -g gold.hun.lem.ekezet.txt -t $resultsdir/results.$config.$method.txt -nn -m $measure
        done
    done
done
cd -

