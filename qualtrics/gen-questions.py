# encoding: utf-8

import sys
import glob
import random

set1 = [ "hozzajarulas", "fenntartas", "helyzet", "huvely", "lap", "suly", "utalas", "allas", "csod", "valto" ]
set2 = [ "jelentes", "gyumolcs", "szellem", "tetel", "belepo", "gazda", "hivatal", "karakter", "oldal", "szervezet" ]
set3 = [ "termeszet", "ful", "gyakorlat", "ho", "kep", "paradicsom", "tanacs", "hitel", "dij", "lehetoseg", "alak", "kilatas", "pofa", "targy", "villa" ]

def process_word(w):
    fn = "../corpus/sentences/%s.txt" % w
    with open(fn, 'r') as f:
        i = 0
        lines = f.readlines()
        for line in lines:
            i += 1
            clean = line.strip("\r\n ").replace("õ", "ő").replace("û", "ű")
            if clean == "":
                continue
            parts = clean.split("\t")
            if len(parts) == 3:
                pass
            else:
                sys.stderr.write("ERROR: "+str(len(parts)-1)+" tabs in "+fn+" in line "+str(i)+":\n"+line)
                continue
            out =            parts[0] + "<strong>" + parts[1] + "</strong>" + parts[2]
            out = w + str(i) + "\t" + parts[0] + "<strong>" + parts[1] + "</strong>" + parts[2]
            yield out

def print_lines(lines):
    for line in lines:
        print line

def do_word(wset):
    out = []
    for w in wset:
        out.extend(list(process_word(w)))
    random.shuffle(out)
    print_lines(out)

do_word(set1)
do_word(set2)
do_word(set3)

