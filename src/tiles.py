# Cut a page image into overlapping tiles for reading.
# Usage: python3 -I tiles.py ../gallica/full/c398_f559.jpg x0 x1 y0 y1 ncols nrows [scale]
#   x0..y1 are percentages of the page; output: ../gallica/tiles/<stem>_r<row>c<col>.jpg
import sys, os
from PIL import Image

src = sys.argv[1]
x0, x1, y0, y1 = (float(a) for a in sys.argv[2:6])
nc, nr = int(sys.argv[6]), int(sys.argv[7])
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.5
im = Image.open(src)
W, H = im.size
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'gallica', 'tiles')
os.makedirs(out, exist_ok=True)
stem = os.path.splitext(os.path.basename(src))[0]
cw = (x1 - x0) / nc; rh = (y1 - y0) / nr
ov_x, ov_y = cw * 0.08, rh * 0.25          # overlap so no symbol/line is cut at a seam
for r in range(nr):
    for c in range(nc):
        a = max(x0, x0 + c * cw - ov_x); b = min(x1, x0 + (c + 1) * cw + ov_x)
        t = max(y0, y0 + r * rh - ov_y); u = min(y1, y0 + (r + 1) * rh + ov_y)
        box = (int(a / 100 * W), int(t / 100 * H), int(b / 100 * W), int(u / 100 * H))
        tile = im.crop(box)
        tile = tile.resize((int(tile.width * scale), int(tile.height * scale)), Image.LANCZOS)
        p = os.path.join(out, f'{stem}_r{r + 1}c{c + 1}.jpg')
        tile.save(p, quality=90)
        print(p, box)
