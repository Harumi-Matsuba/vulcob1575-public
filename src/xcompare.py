# Compare a transcription (data/transcription/pNNN.txt) with an independent one by Codex (second/pNNN_pass1.txt or _pass2.txt)
# in VALUE space: each symbol is replaced by its plaintext value via vk.TOKENS, so naming differences
# (e.g. 4 vs 7, both 'a') do not count. Plain-letter groups {..} become one placeholder '#'.
# Alignment per line with difflib on the value sequences (one item per symbol).
# Usage: PASS=pass2 python3 src/xcompare.py p525 [p526 ...]  -> per-page counts and xcheck/compare_<page>..tsv
import sys, re, difflib, os
from vk import TOKENS, load

KEY = {k: v for k, (v, s) in TOKENS.items()}
HERE = os.path.dirname(os.path.abspath(__file__))


def tv(tok):
    """token -> value item ('#' for plain groups, '?' unknown)."""
    t = tok.strip()
    if not t or t == '|':
        return None
    if t.startswith('{') or t.startswith('?{'):
        return '#' if t.startswith('{') else '?'
    if '/' in t:                       # "i/dl": take the first alternative
        t = t.split('/')[0]
    if t.endswith('?') and len(t) > 1:
        t = t[:-1]
    if t in KEY:
        v = KEY[t]
        if v in ('est', 'pour', 'que', 'guerre', 'Vostre Majeste'):
            return '#'                 # nomenclature groups compare as placeholders
        return v if v else None        # null 'c' dropped
    if t == 'gn':
        return 'gn'
    return '?'


FIRST_SUFFIX = os.environ.get('FIRST', '')      # '' = adjudicated (final), '_first' = first pass
SECOND_PASS = os.environ.get('PASS', 'pass1')    # 'pass1' or 'pass2'


def first(page):
    d = os.environ.get('FIRST_DIR', os.path.join('data', 'transcription'))
    rows = load(os.path.join(HERE, '..', d, page + FIRST_SUFFIX + '.txt'))
    return [(lid, [x for x in (tv(t) for t in toks) if x is not None]) for lid, toks in rows
            if not lid.startswith('524.')]   # 524.99 = cipher tail on p.524, not in the line images


def second(page):
    p = os.path.join(HERE, '..', 'second', f'{page}_{SECOND_PASS}.txt')
    out = []
    for ln in open(p, encoding='utf-8'):
        m = re.match(r'(p\d+_L\d+)\s*(.*)', ln.strip())
        if not m:
            continue
        toks = re.findall(r'\?\{[^}]*\}|\{[^}]*\}|\S+', m.group(2))   # empty line -> no symbols
        out.append((m.group(1), [x for x in (tv(t) for t in toks) if x is not None]))
    return out


if __name__ == '__main__':
    tot_a = tot_m = 0
    for page in sys.argv[1:]:
        A, B = first(page), second(page)
        rows = []
        na = nm = 0
        for (la, a), (lb, b) in zip(A, B):
            sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
            m = sum(bl.size for bl in sm.get_matching_blocks())
            na += len(a); nm += m
            diffs = [f'{op}:{"".join(a[i1:i2])}>{"".join(b[j1:j2])}' for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']
            rows.append(f'{la}\t{lb}\t{len(a)}\t{len(b)}\t{m}\t' + ' '.join(diffs))
        open(os.path.join(HERE, '..', 'xcheck', f'compare_{page}{FIRST_SUFFIX}_{SECOND_PASS}.tsv'), 'w').write(
            'first_line\tsecond_line\tn_first\tn_second\tmatched\tdiffs(first>second)\n' + '\n'.join(rows) + '\n')
        print(f'{page}: lines {len(A)}/{len(B)}, first-pass symbols {na}, matched {nm} ({nm / na:.1%})')
        tot_a += na; tot_m += nm
    if len(sys.argv) > 2:
        print(f'TOTAL: {tot_m}/{tot_a} ({tot_m / tot_a:.1%})')
