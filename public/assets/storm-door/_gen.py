#!/usr/bin/env python3
"""Generate The Storm Door Substack brand assets from the JS the WLD identity.
Daylight = charcoal ink on warm eggshell. Lamplit = warm-white ink on charcoal / photo.
Marks: charcoal-disc bird (daylight), disc-less white bird (lamplit/photo).
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../website/assets
OUT = os.path.join(A, "storm-door")
FONT = os.path.join(A, "fonts", "BodoniModa.ttf")
os.makedirs(OUT, exist_ok=True)

# --- brand palette ---
GROUND      = (237, 234, 227)   # #EDEAE3 warm eggshell
GROUND2     = (230, 226, 217)
INK         = (57, 53, 51)       # #393533 warm charcoal
CHAR_DEEP   = (44, 41, 38)       # #2C2926 lamplit ground
WARMWHITE   = (243, 239, 231)    # #F3EFE7 lamplit ink
BONE        = (210, 205, 187)    # #D2CDBB
RUST        = (165, 59, 31)      # #A53B1F  (true deck rust / orange-shoe tone)

WORD = "The Storm Door"
SS = 2  # supersample factor for text crispness

# --- sans for tracked labels (Helvetica Neue register per DESIGN.md) ---
def load_label_font(px):
    for p in ["/System/Library/Fonts/HelveticaNeue.ttc",
              "/System/Library/Fonts/Helvetica.ttc",
              "/Library/Fonts/Arial.ttf"]:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, px)
            except Exception:
                pass
    return ImageFont.load_default()

def display_font(px, wght=500, opsz=96):
    f = ImageFont.truetype(FONT, px)
    try:
        f.set_variation_by_axes([opsz, wght])
    except Exception:
        pass
    return f

def render_text(text, px, color, wght=500, tracking=0.0, font=None):
    """Render text to a tightly-cropped RGBA image. tracking is a fraction of px."""
    big = px * SS
    f = font(big) if font else display_font(big, wght)
    track = tracking * big
    widths = [f.getlength(c) for c in text]
    total = int(sum(widths) + track * (len(text) - 1)) + 8
    asc, desc = f.getmetrics()
    h = asc + desc + 8
    img = Image.new("RGBA", (total, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x = 4.0
    for c, w in zip(text, widths):
        d.text((x, 4), c, font=f, fill=color + (255,))
        x += w + track
    bb = img.getbbox()
    img = img.crop(bb)
    img = img.resize((max(1, round(img.width / SS)), max(1, round(img.height / SS))), Image.LANCZOS)
    return img

def load_bird(name, target_h):
    im = Image.open(os.path.join(A, name)).convert("RGBA")
    im = im.crop(im.getbbox())
    scale = target_h / im.height
    return im.resize((round(im.width * scale), target_h), Image.LANCZOS)

def paste_center(canvas, img, cx, cy):
    canvas.alpha_composite(img, (round(cx - img.width / 2), round(cy - img.height / 2)))

# ------------------------------------------------------------------
# 1. HORIZONTAL LOCKUP : bird + wordmark on one line
# ------------------------------------------------------------------
def horizontal(bird_name, ink, bg, fname, label=None, label_color=None,
               text_px=240, bird_ratio=1.46, gap_ratio=0.34, pad_ratio=0.62):
    txt = render_text(WORD, text_px, ink, tracking=0.005)
    th = txt.height
    bird_h = round(th * bird_ratio)
    bird = load_bird(bird_name, bird_h)
    gap = round(bird_h * gap_ratio)
    pad = round(bird_h * pad_ratio)

    lab = None
    if label:
        lab = render_text(label, round(text_px * 0.135), label_color, font=load_label_font, tracking=0.30)

    content_h = max(bird_h, th)
    W = pad * 2 + bird.width + gap + txt.width
    H = pad * 2 + content_h + (round(lab.height * 2.4) if lab else 0)
    canvas = Image.new("RGBA", (W, H), (bg + (255,)) if bg else (0, 0, 0, 0))

    mid_y = pad + content_h / 2
    paste_center(canvas, bird, pad + bird.width / 2, mid_y)
    tx = pad + bird.width + gap
    canvas.alpha_composite(txt, (tx, round(mid_y - th / 2)))
    if lab:
        ly = round(pad + content_h + lab.height * 0.9)
        canvas.alpha_composite(lab, (tx + 4, ly))
    canvas.save(os.path.join(OUT, fname))
    return canvas.size

# ------------------------------------------------------------------
# 2. STACKED LOCKUP : bird centered above wordmark
# ------------------------------------------------------------------
def stacked(bird_name, ink, bg, fname, label=None, label_color=None,
            text_px=210, bird_ratio=2.0, gap_ratio=0.42, pad_ratio=0.7):
    txt = render_text(WORD, text_px, ink, tracking=0.01)
    th = txt.height
    bird_h = round(th * bird_ratio)
    bird = load_bird(bird_name, bird_h)
    gap = round(th * gap_ratio)
    pad = round(th * pad_ratio)

    lab = None
    if label:
        lab = render_text(label, round(text_px * 0.16), label_color, font=load_label_font, tracking=0.32)
        lab_gap = round(th * 0.5)

    W = pad * 2 + max(bird.width, txt.width)
    H = pad * 2 + bird.height + gap + th + (lab.height + lab_gap if lab else 0)
    canvas = Image.new("RGBA", (W, H), (bg + (255,)) if bg else (0, 0, 0, 0))
    cx = W / 2
    y = pad
    paste_center(canvas, bird, cx, y + bird.height / 2)
    y += bird.height + gap
    canvas.alpha_composite(txt, (round(cx - txt.width / 2), y))
    y += th
    if lab:
        y += lab_gap
        canvas.alpha_composite(lab, (round(cx - lab.width / 2), y))
    canvas.save(os.path.join(OUT, fname))
    return canvas.size

# ------------------------------------------------------------------
# 2b. WORDMARK ONLY : title text, no bird (Substack header)
# ------------------------------------------------------------------
def wordmark_only(ink, bg, fname, text_px=260, pad_x_ratio=0.16, pad_y_ratio=0.34):
    txt = render_text(WORD, text_px, ink, tracking=0.006)
    px = round(text_px * pad_x_ratio)
    py = round(text_px * pad_y_ratio)
    W = txt.width + px * 2
    H = txt.height + py * 2
    canvas = Image.new("RGBA", (W, H), (bg + (255,)) if bg else (0, 0, 0, 0))
    canvas.alpha_composite(txt, (px, py))
    canvas.save(os.path.join(OUT, fname))
    return canvas.size

# ------------------------------------------------------------------
# 3. SQUARE AVATAR / FAVICON : charcoal disc + white bird
# ------------------------------------------------------------------
def avatar(size, fname, bg=None):
    canvas = Image.new("RGBA", (size, size), (bg + (255,)) if bg else (0, 0, 0, 0))
    disc = load_bird("bird-primary.png", round(size * 0.9))
    paste_center(canvas, disc, size / 2, size / 2)
    canvas.save(os.path.join(OUT, fname))
    return canvas.size

# ------------------------------------------------------------------
# 4. WIDE COVER / HEADER BANNER : photo + scrim + white lockup
# ------------------------------------------------------------------
def _soft_dark(canvas, cx, cy, rw, rh, alpha=150):
    """A blurred dark blob to guarantee a white mark reads over any photo area."""
    blob = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(blob).ellipse([cx - rw, cy - rh, cx + rw, cy + rh], fill=(15, 13, 11, alpha))
    canvas.alpha_composite(blob.filter(ImageFilter.GaussianBlur(rw * 0.55)))

def banner(fname, W, H, crop_box, text_px=134, label="Jonathan Sexton", bird_pos="stack"):
    """bird_pos: 'stack' (bird above wordmark, left) | 'top-right' | 'none'."""
    src = Image.open(os.path.join(A, "hero.jpg")).convert("RGBA")
    photo = src.crop(crop_box).resize((W, H), Image.LANCZOS)
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    canvas.alpha_composite(photo)

    # left-darkening + bottom scrim for text legibility
    scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    for x in range(W):
        a = int(165 * max(0.0, 1 - x / (W * 0.62)) ** 1.4)
        sd.line([(x, 0), (x, H)], fill=(20, 18, 16, a))
    for y in range(H):
        a = int(120 * max(0.0, (y / H - 0.45) / 0.55)) if y / H > 0.45 else 0
        sd.line([(0, y), (W, y)], fill=(20, 18, 16, a))
    canvas.alpha_composite(scrim)

    txt = render_text(WORD, text_px, WARMWHITE, tracking=0.005)
    lab = render_text(label.upper(), round(text_px * 0.2), BONE, font=load_label_font, tracking=0.34)
    rule_w = round(txt.width * 0.18)
    left = round(W * 0.085)
    rd = ImageDraw.Draw(canvas)

    if bird_pos == "stack":
        bird = load_bird("bird-white.png", round(text_px * 1.5))
        block_h = bird.height + round(text_px * 0.3) + txt.height + round(text_px * 0.5) + lab.height
        y = round((H - block_h) / 2)
        canvas.alpha_composite(bird, (left, y)); y += bird.height + round(text_px * 0.3)
    else:
        block_h = txt.height + round(text_px * 0.5) + lab.height
        y = round((H - block_h) / 2)

    canvas.alpha_composite(txt, (left - 2, y)); y += txt.height + round(text_px * 0.34)
    rd.line([(left, y), (left + rule_w, y)], fill=RUST + (255,), width=max(2, round(text_px * 0.022)))
    canvas.alpha_composite(lab, (left + rule_w + round(text_px * 0.22), round(y - lab.height / 2)))

    if bird_pos == "top-right":
        b = load_bird("bird-white.png", round(text_px * 1.28))
        bx = W - round(W * 0.05) - b.width
        by = round(H * 0.13)
        _soft_dark(canvas, bx + b.width / 2, by + b.height / 2, b.width * 0.95, b.height * 0.95, 130)
        canvas.alpha_composite(b, (bx, by))

    canvas.convert("RGB").save(os.path.join(OUT, fname), quality=92)
    return canvas.size

# ------------------------------------------------------------------
# 4b. BANNER with byline using the ornate JS the WLD logotype mark
# ------------------------------------------------------------------
def banner_byline(fname, W, H, crop_box, text_px=120):
    src = Image.open(os.path.join(A, "hero.jpg")).convert("RGBA")
    photo = src.crop(crop_box).resize((W, H), Image.LANCZOS)
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    canvas.alpha_composite(photo)
    scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    for x in range(W):
        a = int(170 * max(0.0, 1 - x / (W * 0.60)) ** 1.4)
        sd.line([(x, 0), (x, H)], fill=(20, 18, 16, a))
    for y in range(H):
        a = int(120 * max(0.0, (y / H - 0.45) / 0.55)) if y / H > 0.45 else 0
        sd.line([(0, y), (W, y)], fill=(20, 18, 16, a))
    canvas.alpha_composite(scrim)

    txt = render_text(WORD, text_px, WARMWHITE, tracking=0.005)
    by = render_text("BY", round(text_px * 0.20), BONE, font=load_label_font, tracking=0.34)
    mark = load_bird("logotype-white.png", round(text_px * 1.42))   # ornate JS the WLD mark
    rule_w = round(txt.width * 0.16)
    left = round(W * 0.085)

    gap1 = round(text_px * 0.40)   # wordmark -> rule
    gap2 = round(text_px * 0.42)   # rule -> byline row
    bygap = round(text_px * 0.34)  # BY -> mark
    block_h = txt.height + gap1 + gap2 + mark.height
    y = round((H - block_h) / 2)

    canvas.alpha_composite(txt, (left - 2, y)); y += txt.height + gap1
    rd = ImageDraw.Draw(canvas)
    rd.line([(left, y), (left + rule_w, y)], fill=RUST + (255,), width=max(2, round(text_px * 0.022)))
    y += gap2
    # byline row: "BY" vertically centered against the ornate mark
    canvas.alpha_composite(by, (left, round(y + mark.height / 2 - by.height / 2)))
    canvas.alpha_composite(mark, (left + by.width + bygap, y))
    canvas.convert("RGB").save(os.path.join(OUT, fname), quality=92)
    return canvas.size

# ------------------------------------------------------------------
# 4c. BANNER: wordmark lower-third, "by" + ornate JS the WLD mark top-right
# ------------------------------------------------------------------
def banner_corner(fname, W, H, crop_box, wm_px=132, mark_h_frac=0.40):
    src = Image.open(os.path.join(A, "hero.jpg")).convert("RGBA")
    photo = src.crop(crop_box).resize((W, H), Image.LANCZOS)
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    canvas.alpha_composite(photo)
    # left-darken + a heavier bottom scrim (wordmark lives in the lower third)
    scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(scrim)
    for x in range(W):
        a = int(150 * max(0.0, 1 - x / (W * 0.58)) ** 1.5)
        sd.line([(x, 0), (x, H)], fill=(20, 18, 16, a))
    for y in range(H):
        a = int(175 * max(0.0, (y / H - 0.38) / 0.62)) if y / H > 0.38 else 0
        sd.line([(0, y), (W, y)], fill=(20, 18, 16, a))
    canvas.alpha_composite(scrim)

    # --- top-right byline unit: "BY" + ornate mark, on a soft dark cushion ---
    mark = load_bird("logotype-white.png", round(H * mark_h_frac))
    by = render_text("BY", round(wm_px * 0.17), BONE, font=load_label_font, tracking=0.34)
    mr, mt = round(W * 0.055), round(H * 0.11)
    mark_x, mark_y = W - mr - mark.width, mt
    bygap = round(wm_px * 0.30)
    by_x = mark_x - bygap - by.width
    by_y = mark_y + mark.height // 2 - by.height // 2
    cx = (by_x + mark_x + mark.width) / 2
    cy = mark_y + mark.height / 2
    _soft_dark(canvas, cx, cy, (mark_x + mark.width - by_x) * 0.72, mark.height * 0.74, 120)
    canvas.alpha_composite(by, (by_x, by_y))
    canvas.alpha_composite(mark, (mark_x, mark_y))

    # --- lower-third wordmark + short rust rule ---
    txt = render_text(WORD, wm_px, WARMWHITE, tracking=0.005)
    left = round(W * 0.085)
    ty = round(H * 0.585)
    canvas.alpha_composite(txt, (left - 2, ty))
    ry = ty + txt.height + round(wm_px * 0.34)
    ImageDraw.Draw(canvas).line([(left, ry), (left + round(txt.width * 0.16), ry)],
                                fill=RUST + (255,), width=max(2, round(wm_px * 0.022)))
    canvas.convert("RGB").save(os.path.join(OUT, fname), quality=92)
    return canvas.size

# ------------------------------------------------------------------
# contact sheet for review
# ------------------------------------------------------------------
def contact_sheet(files, fname, cols=2, cell=820, bg=(120,116,110)):
    rows = (len(files) + cols - 1) // cols
    pad = 26
    sheet = Image.new("RGBA", (cols * cell + pad * (cols + 1), rows * cell + pad * (rows + 1)), bg + (255,))
    # checker so transparency is visible
    ch = Image.new("RGBA", sheet.size, (0,0,0,0))
    cd = ImageDraw.Draw(ch)
    s = 24
    for yy in range(0, sheet.height, s):
        for xx in range(0, sheet.width, s):
            if (xx // s + yy // s) % 2 == 0:
                cd.rectangle([xx, yy, xx+s, yy+s], fill=(135,131,125,255))
    sheet.alpha_composite(ch)
    for i, f in enumerate(files):
        im = Image.open(os.path.join(OUT, f)).convert("RGBA")
        sc = min((cell - 40) / im.width, (cell - 40) / im.height, 1.0)
        im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
        r, c = divmod(i, cols)
        x = pad + c * (cell + pad) + (cell - im.width) // 2
        y = pad + r * (cell + pad) + (cell - im.height) // 2
        sheet.alpha_composite(im, (x, y))
    sheet.convert("RGB").save(os.path.join(OUT, fname), quality=90)

# ================= RUN =================
sizes = {}
# horizontal lockups
sizes['h-day-tr'] = horizontal("bird-primary.png", INK, None, "wordmark-horizontal-daylight-transparent.png", bird_ratio=1.52)
sizes['h-day']    = horizontal("bird-primary.png", INK, GROUND, "wordmark-horizontal-daylight.png", bird_ratio=1.52)
sizes['h-lit-tr'] = horizontal("bird-white.png", WARMWHITE, None, "wordmark-horizontal-lamplit-transparent.png", bird_ratio=1.62)
sizes['h-lit']    = horizontal("bird-white.png", WARMWHITE, CHAR_DEEP, "wordmark-horizontal-lamplit.png", bird_ratio=1.62)
# stacked lockups
sizes['s-day-tr'] = stacked("bird-primary.png", INK, None, "wordmark-stacked-daylight-transparent.png")
sizes['s-day']    = stacked("bird-primary.png", INK, GROUND, "wordmark-stacked-daylight.png")
sizes['s-lit-tr'] = stacked("bird-white.png", WARMWHITE, None, "wordmark-stacked-lamplit-transparent.png", bird_ratio=2.2)
sizes['s-lit']    = stacked("bird-white.png", WARMWHITE, CHAR_DEEP, "wordmark-stacked-lamplit.png", bird_ratio=2.2)
# wordmark only (no bird) — Substack header
sizes['w-day-tr'] = wordmark_only(INK, None, "wordmark-only-daylight-transparent.png")
sizes['w-day']    = wordmark_only(INK, GROUND, "wordmark-only-daylight.png")
sizes['w-lit-tr'] = wordmark_only(WARMWHITE, None, "wordmark-only-lamplit-transparent.png")
sizes['w-lit']    = wordmark_only(WARMWHITE, CHAR_DEEP, "wordmark-only-lamplit.png")
# avatar / favicon
sizes['avatar']   = avatar(1024, "avatar-square-1024.png")
sizes['favicon']  = avatar(512, "favicon-512.png")
# banner  (hero.jpg is 1800x2700; crop a horizontal slice across the lit doorway)
sizes['banner']   = banner("cover-banner-1600x600.png", 1600, 600, (0, 150, 1800, 825))
sizes['banner_jswld_tr'] = banner("cover-banner-jswld-bird-topright-1600x600.png", 1600, 600, (0, 150, 1800, 825), label="JS the WLD", bird_pos="top-right")
sizes['banner_jswld_nb'] = banner("cover-banner-jswld-nobird-1600x600.png", 1600, 600, (0, 150, 1800, 825), label="JS the WLD", bird_pos="none")
sizes['banner_byline']   = banner_byline("cover-banner-by-jswld-logo-1600x600.png", 1600, 600, (0, 150, 1800, 825))
sizes['banner_corner']   = banner_corner("cover-banner-storm-lower-jswld-topright-1600x600.png", 1600, 600, (0, 150, 1800, 825))

for k, v in sizes.items():
    print(f"{k:10s} {v}")

contact_sheet([
    "wordmark-horizontal-daylight.png", "wordmark-horizontal-lamplit.png",
    "wordmark-stacked-daylight.png", "wordmark-stacked-lamplit.png",
    "avatar-square-1024.png", "favicon-512.png",
], "_review-lockups.png")
print("done")
