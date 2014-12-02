# encoding: utf-8
import sys
from collections import defaultdict
import re

lines = sys.stdin.readlines()

fieldnames = lines[0].split(',')
ans = {}
for f in fieldnames:
    ans[f] = defaultdict(int)
Qi0 = -1
Qi1 = -1
for i in range(len(fieldnames)):
    if fieldnames[i][0] == 'Q' and fieldnames[i][-1].isdigit():
        if Qi0 < 0:
            Qi0 = i
        Qi1 = i
Qi1 += 1

k2w = {
    'alak': u'alak',
    'allas': u'állás',
    'belepo': u'belépő',
    'csod': u'csőd',
    'dij': u'díj',
    'fenntartas': u'fenntartás',
    'ful': u'fül',
    'gazda': u'gazda',
    'gyakorlat': u'gyakorlat',
    'gyumolcs': u'gyümölcs',
    'helyzet': u'helyzet',
    'hitel': u'hitel',
    'hivatal': u'hivatal',
    'ho': u'hó',
    'hozzajarulas': u'hozzájárulás',
    'huvely': u'hüvely',
    'jelentes': u'jelentés',
    'karakter': u'karakter',
    'kep': u'kép',
    'kilatas': u'kilátás',
    'lap': u'lap',
    'lehetoseg': u'lehetőség',
    'oldal': u'oldal',
    'paradicsom': u'paradicsom',
    'pofa': u'pofa',
    'suly': u'súly',
    'szellem': u'szellem',
    'szervezet': u'szervezet',
    'tanacs': u'tanács',
    'targy': u'tárgy',
    'termeszet': u'természet',
    'tetel': u'tétel',
    'utalas': u'utalás',
    'valto': u'váltó',
    'villa': u'villa',
}

for line in lines[2:]:
    fields = line.split(',')
    for i in range(Qi0, Qi1):
        words = filter(len, [w.strip() for w in fields[i].split('/')])
        for w in words:
            ans[fieldnames[i]][w] += 1

for f in fieldnames[Qi0:Qi1]:
    kw = re.sub('^Q(\w+?)(\d+)', '\\1', f)
    ki = re.sub('^Q(\w+?)(\d+)', '\\2', f)
    print k2w[kw].encode('utf-8'), ki, '::',
    pairs = [ (w + ' ' + str(ans[f][w])) for w in sorted(ans[f], key=ans[f].get, reverse=True) ]
    print '; '.join(pairs)

