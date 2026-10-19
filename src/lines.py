# Find text-line baselines on a page image by horizontal ink profile and cut one strip per line.
# Usage: python3 lines.py ../gallica/full/c398_f559.jpg x0 x1 y0 y1 [--cut OUTDIR PREFIX]
#   x0..y1 in % of the page (the cipher block). Prints line centres (px) and spacing.
#   With --cut, writes OUTDIR/PREFIX_L01.jpg ... (strip = centre +- 0.62*spacing) and a contact sheet.
import sys, os
import numpy as np
from PIL import Image

src = sys.argv[1]
x0, x1, y0, y1 = (float(a) for a in sys.argv[2:6])
im = Image.open(src).convert('L')
W, H = im.size
X0, X1, Y0, Y1 = int(x0 / 100 * W), int(x1 / 100 * W), int(y0 / 100 * H), int(y1 / 100 * H)
a = np.asarray(im, dtype=np.float32)[Y0:Y1, X0:X1]
ink = (a < np.percentile(a, 8)).sum(axis=1).astype(float)   # dark pixels per row
k = 15
sm = np.convolve(ink, np.ones(k) / k, mode='same')
# estimate spacing from autocorrelation
s = sm - sm.mean()
ac = np.correlate(s, s, mode='full')[len(s) - 1:]
lo, hi = 50, 200
sp = lo + int(np.argmax(ac[lo:hi]))
# peaks: local maxima at least 0.6*spacing apart, above a floor
floor = sm.mean() * 0.6
peaks = []
for i in range(1, len(sm) - 1):
    if sm[i] >= sm[i - 1] and sm[i] > sm[i + 1] and sm[i] > floor:
        if peaks and i - peaks[-1] < 0.6 * sp:
            if sm[i] > sm[peaks[-1]]:
                peaks[-1] = i
            continue
        peaks.append(i)
cent = [Y0 + p for p in peaks]
print(f'spacing {sp}px, lines {len(cent)}')
print(' '.join(str(c) for c in cent))
if '--cut' in sys.argv:
    j = sys.argv.index('--cut'); out, pre = sys.argv[j + 1], sys.argv[j + 2]
    os.makedirs(out, exist_ok=True)
    rgb = Image.open(src).convert('RGB')
    half = int(0.62 * sp)
    strips = []
    for n, c in enumerate(cent, 1):
        st = rgb.crop((X0, max(0, c - half), X1, min(H, c + half)))
        st.save(os.path.join(out, f'{pre}_L{n:02d}.jpg'), quality=92)
        strips.append(st)
    # contact sheet (half size) for checking
    w = max(s.width for s in strips) // 2; h = sum(s.height // 2 for s in strips)
    sheet = Image.new('RGB', (w + 60, h), 'white')
    y = 0
    from PIL import ImageDraw
    d = ImageDraw.Draw(sheet)
    for n, s in enumerate(strips, 1):
        s2 = s.resize((s.width // 2, s.height // 2))
        sheet.paste(s2, (60, y)); d.text((5, y + 5), f'L{n:02d}', fill='red'); y += s2.height
    sheet.save(os.path.join(out, f'{pre}_sheet.jpg'), quality=85)
