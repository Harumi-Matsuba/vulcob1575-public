# Word-level majority of independent margin readings (one line per image in each file).
# Readings are aligned word by word to the first file (pivot); each pivot position takes the word with most votes
# (compared after normalisation: lower case, ?/· removed, v->u, j->i, y->i); ties go to the tie-break file.
# Words inserted by a majority of the other readings at the same place are inserted.
# Usage: python3 src/mvote.py OUT TIEBREAK FILE1 FILE2 ... (FILE1 = pivot), e.g. calib/p258_margin_vote.txt calib/p258_margin_adj.txt calib/readers/m258_codex1.txt ... m258_sonnet2.txt
import sys, re, difflib
from collections import Counter


def load(p):
    d = {}
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        lid, _, t = ln.rstrip('\n').partition('\t')
        d[lid.strip()] = t.split()
    return d


def norm(w):
    w = w.lower().replace('?', '').replace('·', '')
    return w.replace('v', 'u').replace('j', 'i').replace('y', 'i')


out_p, tie_p, files = sys.argv[1], sys.argv[2], sys.argv[3:]
R = [load(f) for f in files]
T = load(tie_p)
piv = R[0]
lines = []
for lid in sorted(piv):
    a = piv[lid]; an = [norm(x) for x in a]
    votes = [[x] for x in a]          # candidate words per pivot position
    ins = [Counter() for _ in range(len(a) + 1)]
    for r in R[1:]:
        b = r.get(lid, []); bn = [norm(x) for x in b]
        sm = difflib.SequenceMatcher(None, an, bn, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal' or (op == 'replace' and i2 - i1 == j2 - j1):
                for k in range(i2 - i1):
                    votes[i1 + k].append(b[j1 + k])
            elif op == 'insert' or op == 'replace':
                ins[i1][' '.join(b[j1:j2])] += 1
                if op == 'replace':      # unequal replace: the pivot words get no support from this reader
                    pass
    tie = T.get(lid, [])
    tie_n = set(norm(x) for x in tie)
    res = []
    for i in range(len(a) + 1):
        if ins[i]:
            w, n = ins[i].most_common(1)[0]
            if n >= 3:                    # inserted by a majority of the 5 readers (pivot lacks it)
                res += w.split()
        if i == len(a):
            break
        c = Counter(norm(x) for x in votes[i])
        best = c.most_common()
        if len(votes[i]) < 3 and best[0][1] < 2:
            # pivot word unsupported by others (they aligned elsewhere): keep only if the tie-break has it
            if norm(a[i]) in tie_n:
                res.append(a[i])
            continue
        top = [w for w, n in best if n == best[0][1]]
        pick = top[0] if len(top) == 1 else next((w for w in top if w in tie_n), top[0])
        res.append(next(x for x in votes[i] if norm(x) == pick))
    lines.append(lid + '\t' + ' '.join(res))
open(out_p, 'w').write('# word-level majority of ' + ', '.join(f.split('/')[-1] for f in files) + '\n' + '\n'.join(lines) + '\n')
print(out_p, len(lines), 'lines')
