# Agreement by symbol NAME (not value) between the final transcription and an independent Codex pass.
# Plain-letter groups compare as one item '{}'; "x/y" alternatives take the first; trailing "?" is dropped.
# Usage: python3 src/namecompare.py pass2 [pages...]
import sys, os, re, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vk
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def norm(t):
    if t.startswith('{') or t.startswith('?{'): return '{}'
    t = t.split('/')[0]
    return t[:-1] if t.endswith('?') and len(t) > 1 else t
def first(p):
    return [[norm(t) for t in toks if t != '|'] for l, toks in vk.load(os.path.join(ROOT, 'data', 'transcription', p + '.txt')) if not l.startswith('524.')]
def second(p, ps):
    out = []
    for ln in open(os.path.join(ROOT, 'second', f'{p}_{ps}.txt'), encoding='utf-8'):
        m = re.match(r'(p\d+_L\d+)\s*(.*)', ln.strip())
        if m:
            toks = re.findall(r'\?\{[^}]*\}|\{[^}]*\}|\S+', m.group(2))
            out.append([norm(t if not t.startswith('{') else t) for t in toks])
    return out
ps = sys.argv[1]; pages = sys.argv[2:]
TA = TM = 0
for p in pages:
    A, B = first(p), second(p, ps); na = nm = 0
    for a, b in zip(A, B):
        a2 = ['ucl' if x == 'ucl' else x for x in a]
        b2 = [{'{ucl}': 'ucl', '{plus}': 'plus', '{ros}': 'ros', '{c}': 'c'}.get(x, x) for x in b]
        sm = difflib.SequenceMatcher(None, a2, b2, autojunk=False)
        nm += sum(x.size for x in sm.get_matching_blocks()); na += len(a2)
    TA += na; TM += nm
    print(f'{p} {nm}/{na} {nm / na:.1%}')
print(f'TOTAL {TM}/{TA} {TM / TA:.1%}')
