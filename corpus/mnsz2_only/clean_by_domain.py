import glob
import clean_mnsz2_for_glove

mnsz1_domains = ['pers', 'lit', 'off', 'press', 'sci', 'spok']
mnsz2_domains = [               'off', 'press', 'sci', 'spok']

for domain in mnsz2_domains:
    with open(domain+".clean.txt", 'w') as w:
        for fn in glob.glob(domain+"_*.ftgd"):
            with open(fn, 'r') as f:
                print fn
                clean_mnsz2_for_glove.clean(f, w)

