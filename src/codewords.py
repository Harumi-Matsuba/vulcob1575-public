# Find what the contemporary margin decipherment writes at the place of each plain-letter code group.
# The decode (vk.py decode output) is split at each {group}; the letters just before and after are
# located in the margin text (fuzzy, difflib), and the margin letters between the two anchors are reported.
# Usage: python3 src/codewords.py calib/p258_decode.tsv calib/p258_margin_vote_text.txt
import sys, re, difflib, unicodedata


def norm(s):
    s = unicodedata.normalize('NFD', s); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub('[^a-z]', '', s.lower().replace('j', 'i').replace('v', 'u'))


dec_raw = ' '.join(l.split('\t', 1)[1].rstrip('\n') for l in open(sys.argv[1], encoding='utf-8') if '\t' in l)
dec_raw = re.sub(r'\[([a-z]+)\]', r'\1', dec_raw)
dec_raw = re.sub(r'\[(?:VOSTRE MAJESTE|EST|POUR|QUE)\]', lambda m: m.group(0)[1:-1].lower(), dec_raw)
mar_words = [w for l in open(sys.argv[2], encoding='utf-8') if not l.startswith('#') for w in l.split()]
mar = norm(' '.join(w.replace('?', '') for w in mar_words))
K = int(sys.argv[3]) if len(sys.argv) > 3 else 7

# split into alternating text / group tokens (consecutive groups are merged)
parts = re.split(r'((?:\{[^}]*\}\s*)+)', dec_raw)
pos = 0
plain = ''
items = []
for p in parts:
    if p.startswith('{'):
        items.append(('G', re.findall(r'\{([^}]*)\}', p), len(plain)))
    else:
        plain += norm(p)
sm = difflib.SequenceMatcher(None, plain, mar, autojunk=False)
# map each plain index to a margin index via matching blocks
mp = {}
for b in sm.get_matching_blocks():
    for k in range(b.size):
        mp[b.a + k] = b.b + k


def near(i, step):
    j = i
    while 0 <= j < len(plain):
        if j in mp:
            return mp[j], abs(j - i)
        j += step
    return None, None


for _, groups, at in items:
    bef = plain[max(0, at - K):at]; aft = plain[at:at + K]
    mb, db = near(at - 1, -1); ma, da = near(at, +1)
    gap = mar[mb + 1:ma] if mb is not None and ma is not None and ma > mb else ''
    ok = (db is not None and da is not None and db <= 2 and da <= 2)
    print(f"{'+'.join(groups):22} | ...{bef} [{gap if len(gap) < 60 else gap[:60] + '…'}] {aft}... | anchors {'ok' if ok else 'weak'} (d={db},{da})")
