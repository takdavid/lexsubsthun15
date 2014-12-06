import sys

def clean(f, w):
    for line in f.readlines():
        try:
            fields = (line.strip().split("\t"))
            if len(fields) == 0:
                continue
            if fields[-1] == "__NA__":
                continue
            lemma = (fields[1].split("|"))[-1]
            w.write(lemma + ' ')
        except:
            pass

if __name__ == "__main__":
    clean(sys.stdin)

