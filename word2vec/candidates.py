import word2vec
import os
import sys
_sep=os.linesep
import numpy as np

model = None

def load():
    global model
    if not model:
        model = word2vec.load('tmp/press.bin')
        #if os.path.exists('tmp/press.clusters.txt'):
        #    model.clusters = word2vec.load_clusters('tmp/press.clusters.txt')

def latin2(fun):
    def wrap(*words):
        return [s.decode('iso-8859-2') for s in fun(*[u.encode('iso-8859-2') for u in words])]
    return wrap

candidates_now = []

@latin2
def set_candidates_now(*candi):
    global candidates_now
    candidates_now = []
    for w in candi:
        try:
            candidates_now.append(model.ix(w))
        except:
            pass
    return []

@latin2
def cosine(*words):
    indexes, metrics = model.cosine(words[0])
    return [model.vocab[i] for i in indexes]
    #print model.generate_response(indexes, metrics).tolist()

@latin2
def analogy(*words):
    indexes, metrics = model.analogy(pos=[words[0], words[2]], neg=[words[1]], n=10)
    return [model.vocab[i] for i in indexes]
    #print model.generate_response(indexes, metrics).tolist()

def cosinevec(model, vec, n=10):
    metrics = np.dot(model.l2norm, vec.T)
    best = np.argsort(metrics)[::-1][1:n+1]
    best_metrics = metrics[best]
    return best, best_metrics

def closest(vecs, vec, n=10):
    metrics = np.dot(vecs, vec.T)
    best = np.argsort(metrics)[::-1][1:n+1]
    best_metrics = metrics[best]
    return best, best_metrics

def vecs(words):
    vecs = []
    for w in words[1:]:
        try:
            vecs.append(model[w])
        except:
            pass
    return np.array(vecs, ndmin=2)

@latin2
def averagecontext(*words):
    vec0 = model[words[0]]
    npvecs = vecs(words)
    avg = np.average(npvecs, axis=0)
    d = avg - vec0
    q = 1.0 / np.sqrt(len(npvecs))
    vec = vec0 + q * d
    indexes, metrics = cosinevec(model, vec)
    return [model.vocab[i] for i in indexes]

@latin2
def bestcosinecontext(*words):
    vec0 = model[words[0]]
    global candidates_now
    if candidates_now:
        indexes = candidates_now
        m = np.dot(model.l2norm, vec0.T)
        metrics = m[indexes]
    else:
        indexes, metrics = cosinevec(model, vec0, 15)
    npvecs = vecs(words)
    bests = []
    for i in range(len(indexes)):
        idx = indexes[i]
        met = metrics[i]
        vec = model.l2norm[idx]
        val = met*np.dot(npvecs, vec.T).sum()
        #best, best_metrics = closest(npvecs, vec, 1)
        bests.append((val, idx))
    return [model.vocab[i] for v, i in sorted(bests, reverse=True)[:10]]

@latin2
def bestl2context(*words):
    vec0 = model[words[0]]
    global candidates_now
    if candidates_now:
        indexes = candidates_now
        m = np.dot(model.l2norm, vec0.T)
        metrics = m[indexes]
    else:
        indexes, metrics = cosinevec(model, vec0, 15)
    npvecs = vecs(words)
    bests = []
    for i in range(len(indexes)):
        idx = indexes[i]
        met = metrics[i]
        vec = model.l2norm[idx]
        val = sum([np.linalg.norm(v-vec) for v in npvecs])
        bests.append((val, idx))
    return [model.vocab[i] for v, i in sorted(bests)[:10]]

import re
Wsplit = re.compile(ur'\W+', re.UNICODE)

def clean_sentence(s):
    return [(w.lower().split('|'))[0] for w in Wsplit.split(s) if len(w) > 0]

def generate(*words):
    #try:
        if len(words) == 1:
            set_candidates_now()
            return cosine(*words)
        elif len(words) == 3:
            set_candidates_now(*cosine(*words))
            return analogy(*words)
        elif len(words) > 3:
            set_candidates_now(*cosine(*words))
            return averagecontext(*words)
        else:
            return []
    #except Exception as ex:
    #    sys.stderr.write(str(ex)+"\n")
    #    return []

def splitkey(*words):
    if len(words) > 1 and words[1].isdigit():
        return (words[0] + ' ' + words[1] + ' ::', words[0:1]+words[2:])
    else:
        return (words[0] + ' ::', words)

if __name__ == "__main__":
    load()
    while _sep == os.linesep:
        line = sys.stdin.readline()               
        _sep = line[-len(os.linesep):]
        line = line.strip().decode('utf-8')
        sent = clean_sentence(line)
        (key, words) = splitkey(*sent)
        print key + ' ' + '; '.join(generate(*words))

