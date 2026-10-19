# Re-cut line images at the SAME line centres as before (detected with the old x-range) but with a wider x-range,
# so that symbols at the right edge are no longer cut. Writes ../xcheck/img_wide/<page>/<page>_LNN.jpg.
# Usage: python3 recut.py <view> <old_x0> <old_x1> <new_x0> <new_x1> <page> <first_index> <n_lines>
import sys, os, subprocess
from PIL import Image
f, ox0, ox1, nx0, nx1, page, first, n = sys.argv[1], *map(float, sys.argv[2:6]), sys.argv[6], int(sys.argv[7]), int(sys.argv[8])
src = f'../gallica/full/c398_f{f}.jpg'
out = subprocess.run(['python3', 'lines.py', src, str(ox0), str(ox1), '5', '92'], capture_output=True, text=True).stdout.strip().split('\n')
sp = int(out[0].split()[1].rstrip(',').rstrip('px')); cent = list(map(int, out[-1].split()))
im = Image.open(src).convert('RGB'); W, H = im.size
half = int(0.62 * sp); d = f'../xcheck/img_wide/{page}'; os.makedirs(d, exist_ok=True)
for i in range(n):
    c = cent[first - 1 + i]
    im.crop((int(nx0 / 100 * W), max(0, c - half), int(nx1 / 100 * W), min(H, c + half))).save(f'{d}/{page}_L{i + 1:02d}.jpg', quality=92)
print(page, n, 'lines from centre index', first, 'spacing', sp)
