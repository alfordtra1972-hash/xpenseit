"""Generates XpenseIt app icons (run once: python make_icons.py).

A gold bar and a torn-edge receipt cross to form an X on deep navy.
"""
from PIL import Image, ImageDraw, ImageFilter
import os

S = 2048  # drawn at 2x, downscaled for smooth edges
C = S // 2
here = os.path.dirname(os.path.abspath(__file__))


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(len(a)))


def vertical_gradient(w, h, top, bottom):
    img = Image.new("RGBA", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        d.line([(0, y), (w, y)], fill=lerp(top, bottom, y / max(1, h - 1)) + (255,))
    return img


# Background: deep navy with a faint warm glow
bg = vertical_gradient(S, S, (22, 36, 68), (9, 15, 30))
glow = Image.new("L", (S, S), 0)
ImageDraw.Draw(glow).ellipse((C - 760, C - 820, C + 760, C + 700), fill=34)
glow = glow.filter(ImageFilter.GaussianBlur(320))
bg.paste((214, 176, 98, 255), (0, 0), glow)

# Gold stroke (top-left to bottom-right)
BL, BW = 1480, 270
bar_fill = vertical_gradient(BW, BL, (240, 218, 160), (184, 141, 59))
bar_mask = Image.new("L", (BW, BL), 0)
ImageDraw.Draw(bar_mask).rounded_rectangle((0, 0, BW - 1, BL - 1), BW // 2, fill=255)
bar = Image.new("RGBA", (S, S), (0, 0, 0, 0))
bar.paste(bar_fill, (C - BW // 2, C - BL // 2), bar_mask)
bar = bar.rotate(45, resample=Image.BICUBIC)

# Receipt stroke (top-right to bottom-left) with torn zigzag ends
RW, RL, N, TH = 330, 1500, 5, 46
x0, x1 = C - RW // 2, C + RW // 2
y0, y1 = C - RL // 2, C + RL // 2
tw = RW / N
pts = [(x0, y0 + TH)]
for i in range(N):
    pts += [(x0 + (i + .5) * tw, y0), (x0 + (i + 1) * tw, y0 + TH)]
pts.append((x1, y1 - TH))
for i in range(N - 1, -1, -1):
    pts += [(x0 + (i + .5) * tw, y1), (x0 + i * tw, y1 - TH)]
rec = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(rec)
d.polygon(pts, fill=(251, 246, 234, 255))
ink = (196, 188, 168, 255)
gold = (196, 156, 72, 255)
for y, w in [(-520, 200), (-450, 150), (-380, 180)]:
    d.rounded_rectangle((x0 + 60, C + y, x0 + 60 + w, C + y + 30), 15, fill=ink)
for y, w in [(330, 170), (400, 130)]:
    d.rounded_rectangle((x0 + 60, C + y, x0 + 60 + w, C + y + 30), 15, fill=ink)
d.rounded_rectangle((x0 + 60, C + 480, x1 - 60, C + 510), 15, fill=gold)
rec = rec.rotate(-45, resample=Image.BICUBIC)

# Soft shadow of the receipt onto the gold bar
shadow_alpha = rec.split()[3].filter(ImageFilter.GaussianBlur(40)).point(lambda a: int(a * .55))
shadow = Image.new("RGBA", (S, S), (3, 6, 15, 0))
shadow.putalpha(shadow_alpha)
shadow = shadow.transform(shadow.size, Image.AFFINE, (1, 0, -18, 0, 1, -30))

out = Image.alpha_composite(bg, bar)
out = Image.alpha_composite(out, shadow)
out = Image.alpha_composite(out, rec).convert("RGB")

os.makedirs(os.path.join(here, "icons"), exist_ok=True)
for size in (180, 192, 512):
    out.resize((size, size), Image.LANCZOS).save(os.path.join(here, "icons", f"icon-{size}.png"))
print("icons written")
