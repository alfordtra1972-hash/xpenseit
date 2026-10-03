"""Generates SnapStub app icons (run once: python make_icons.py)."""
from PIL import Image, ImageDraw, ImageFilter
import os

S = 1024
here = os.path.dirname(os.path.abspath(__file__))


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


# Diagonal gradient background: cyan -> violet
c1, c2 = (34, 211, 238), (139, 92, 246)
bg = Image.new("RGB", (S, S))
px = bg.load()
for y in range(S):
    for x in range(S):
        px[x, y] = lerp(c1, c2, (x + y) / (2 * S))

# Receipt shape with zigzag bottom
L, R, T, B = 300, 724, 190, 820
tooth = 53
pts = [(L, T), (R, T), (R, B)]
x, up = R, True
while x > L:
    x2 = max(L, x - tooth)
    pts.append(((x + x2) / 2, B - 40 if up else B))
    pts.append((x2, B))
    x = x2
pts.append((L, T))

shadow = Image.new("L", (S, S), 0)
ImageDraw.Draw(shadow).polygon([(p[0] + 14, p[1] + 24) for p in pts], fill=110)
shadow = shadow.filter(ImageFilter.GaussianBlur(28))
bg.paste((30, 20, 70), (0, 0), shadow)

d = ImageDraw.Draw(bg)
d.polygon(pts, fill=(255, 255, 255))

ink = (88, 72, 190)
light = (200, 196, 235)
d.rounded_rectangle((370, 270, 560, 310), 20, fill=ink)
for i, w in enumerate([284, 220, 250]):
    y = 380 + i * 70
    d.rounded_rectangle((370, y, 370 + w, y + 30), 15, fill=light)
d.rounded_rectangle((370, 610, 654, 616), 3, fill=light)
d.rounded_rectangle((370, 650, 470, 690), 18, fill=ink)
d.rounded_rectangle((540, 650, 654, 690), 18, fill=ink)

# Camera shutter badge
cx, cy, r = 700, 760, 130
d.ellipse((cx - r - 14, cy - r - 14, cx + r + 14, cy + r + 14), fill=(255, 255, 255))
grad = Image.new("RGB", (2 * r, 2 * r))
gp = grad.load()
for yy in range(2 * r):
    for xx in range(2 * r):
        gp[xx, yy] = lerp((14, 165, 233), (124, 58, 237), (xx + yy) / (4 * r))
mask = Image.new("L", (2 * r, 2 * r), 0)
ImageDraw.Draw(mask).ellipse((0, 0, 2 * r - 1, 2 * r - 1), fill=255)
bg.paste(grad, (cx - r, cy - r), mask)
d.ellipse((cx - 52, cy - 52, cx + 52, cy + 52), outline=(255, 255, 255), width=22)

for size in (180, 192, 512):
    bg.resize((size, size), Image.LANCZOS).save(os.path.join(here, "icons", f"icon-{size}.png"))
print("icons written")
