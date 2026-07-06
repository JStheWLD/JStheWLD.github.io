# The Storm Door — Substack brand graphics

Built from the JS the WLD identity (Truth Bird + Bodoni Moda Didone), in the two brand
skins: **Daylight** (warm charcoal ink on eggshell `#EDEAE3`) and **Lamplit** (warm white
`#F3EFE7` on charcoal `#2C2926` / photography). Regenerate any time with `python3 _gen.py`.

## What goes where on Substack

| Substack slot | File | Notes |
|---|---|---|
| **Logo** (Settings → Publication details) | `avatar-square-1024.png` | Charcoal disc + white bird. Substack masks it to a circle; the disc fills it. |
| **Favicon** | `favicon-512.png` | Same mark, smaller export. |
| **Header / title only, no bird** (light theme) | `wordmark-only-daylight-transparent.png` | The title alone. Primary Substack header. |
| **Header / title only, no bird** (dark) | `wordmark-only-lamplit-transparent.png` | White title for dark headers, email, social. |
| **Header / lockup with bird** (light theme) | `wordmark-horizontal-daylight-transparent.png` | If you want the bird beside the title. |
| **Header / lockup with bird** (dark surfaces) | `wordmark-horizontal-lamplit-transparent.png` | White ink, transparent ground. |
| **Welcome / cover banner** | `cover-banner-storm-lower-jswld-topright-1600x600.png` | Lamplit shoot frame, the silhouette in the lit doorway. "The Storm Door" wordmark in the lower third, ornate JS·THE·WLD logo mark top-right. |

## Full file list

**Horizontal lockup** (bird beside wordmark — the primary masthead form)
- `wordmark-horizontal-daylight.png` — on eggshell
- `wordmark-horizontal-daylight-transparent.png`
- `wordmark-horizontal-lamplit.png` — on charcoal
- `wordmark-horizontal-lamplit-transparent.png`

**Stacked lockup** (bird above wordmark — for square / centered crops, email headers)
- `wordmark-stacked-daylight.png` / `-transparent.png`
- `wordmark-stacked-lamplit.png` / `-transparent.png`

**Mark only**
- `avatar-square-1024.png` — logo / avatar
- `favicon-512.png`

**Banner**
- `cover-banner-storm-lower-jswld-topright-1600x600.png` — "The Storm Door" wordmark lower-third + ornate JS·THE·WLD logo mark top-right

## Source

- Marks: `../bird-primary.png` (charcoal disc + white bird), `../bird-white.png` (white bird).
- Photo: `../hero.jpg` (silhouette in a lit doorway).
- Type: Bodoni Moda (`../fonts/BodoniModa.ttf`), the brand `--display` Didone, optical size 96.
- Label sans: system Helvetica Neue (the `--ui` register), tracked caps.
