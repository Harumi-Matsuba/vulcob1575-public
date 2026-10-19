# Majority vote of three independent Codex transcriptions, in VALUE space, without using our transcription.
# Runs b and c are aligned to run a (difflib); at each position of a the value with >=2 votes wins (ties: a).
# A segment present in both b and c but not in a (same content) is inserted.
# Output: xcheck/out/<page>_pass3vote.txt, one line per image, items written as "v:<value>" (read by xcompare.tv).
# Usage: python3 vote.py p525 [...]
import sys, os, re, difflib
from xcompare import tv, HERE


def run(page, r):
    out = {}
    for ln in open(os.path.join(HERE, '..', 'xcheck', 'out', f'{page}_pass3{r}.txt'), encoding='utf-8'):
        m = re.match(r'(p\d+_L\d+)\s*(.*)', ln.strip())
        if not m:
            continue
        toks = re.findall(r'\?\{[^}]*\}|\{[^}]*\}|\S+', m.group(2))
        out[m.group(1)] = [x for x in (tv(t) for t in toks) if x is not None]
    return out


def project(a, b):
    """for each index of a: the aligned item of b (or None); plus insertions of b before index i."""
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    at = [None] * len(a); ins = {}
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ('equal',) or (op == 'replace' and i2 - i1 == j2 - j1):
            for k in range(i2 - i1):
                at[i1 + k] = b[j1 + k]
        elif op == 'insert':
            ins[i1] = tuple(b[j1:j2])
        elif op == 'replace':           # unequal lengths: treat as delete + insert
            ins[i1] = tuple(b[j1:j2])
    return at, ins


def vote(a, b, c):
    ab, ib = project(a, b); ac, ic = project(a, c)
    out = []
    for i in range(len(a) + 1):
        if i in ib and i in ic and ib[i] == ic[i]:
            out += list(ib[i])
        if i == len(a):
            break
        cand = [a[i], ab[i], ac[i]]
        if ab[i] is not None and ab[i] == ac[i] and ab[i] != a[i]:
            out.append(ab[i])
        elif ab[i] is None and ac[i] is None:
            continue                     # a alone has it, both others lack it: drop
        else:
            out.append(a[i])
    return out


if __name__ == '__main__':
    for page in sys.argv[1:]:
        A, B, C = run(page, 'a'), run(page, 'b'), run(page, 'c')
        lines = []
        for lid in sorted(A):
            v = vote(A[lid], B.get(lid, []), C.get(lid, []))
            lines.append(lid + '\t' + ' '.join('v:' + x for x in v))
        open(os.path.join(HERE, '..', 'xcheck', 'out', f'{page}_pass3vote.txt'), 'w').write('\n'.join(lines) + '\n')
        print(page, 'lines', len(lines))
