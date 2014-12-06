# encoding: utf-8
import sys
import candidates
candidates.load()

def print_input(words):
    s = ' '.join(words)
    if sys.stdout.isatty():
        print '\033[94m'+s+'\033[0m'
    else:
        print s.encode('utf-8')

def print_output(key, words):
    s = key + ' ' + '; '.join(words)
    print s.encode('utf-8')

words = [u'állás', u'munkahely', u'helyzet']
(key, words) = candidates.splitkey(*words)
print_input([words[0]])
print_output(key, candidates.generate(words[0]))
print_input(words)
print_output(key, candidates.generate(*words))

words = [u'állás', u'munkahely', u'eredmény']
(key, words) = candidates.splitkey(*words)
print_input(words)
print_output(key, candidates.generate(*words))

concordance = [
    (u'állás 1', u'egyszerű lett volna úgy számol ki van állás mond polgármesterasszony két óvónő három dajka iskola szakácsnő pedagógus Áfész bolt négy alkalmazott'),
    (u'állás 2', u'ugyanis az ügy vétkes talál jegyzőnő már meneszt pályázat ír ki az állás betölt ám jelentkező nem akad'),
    (u'állás 3', u'orosz egység csapás mér muzulmán lázad állás csecsen határ mentén'),
    (u'állás 4', u'ellentámadás régi állás százalék visszafoglal'),
]
for w0, s in concordance:
    sent = candidates.clean_sentence(w0 + ' ' + s)
    (key, words) = candidates.splitkey(*sent)
    print_input(words)
    print_output(key, candidates.generate(*words))

