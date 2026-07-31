---
name: JS the WLD
description: South meets the future — matte grotesque, typewriter, and a deep-sea electric pole.
colors:
  paper: "#EDEAE3"
  dusk: "#171512"
  night: "#06080C"
  wire: "#04060B"
  end: "#0A0C10"
  ink: "#1B1916"
  bone: "#E9E4D8"
  rust: "#A8401D"
  amber: "#D99A42"
  lit: "#40C4E8"
  edge: "rgba(64,196,232,0.18)"
  edge-lit: "rgba(64,196,232,0.85)"
typography:
  act:
    fontFamily: "Archivo, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(3.4rem, 17vw, 13rem)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: "-0.055em"
  craft:
    fontFamily: "Archivo, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(2.6rem, 8vw, 5.8rem)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "-0.045em"
  heading:
    fontFamily: "Archivo, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(1.7rem, 4vw, 2.9rem)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.035em"
  body:
    fontFamily: "Courier Prime, ui-monospace, SF Mono, monospace"
    fontSize: "clamp(0.86rem, 1.5vw, 1rem)"
    fontWeight: 400
    lineHeight: 1.9
  tag:
    fontFamily: "Courier Prime, ui-monospace, SF Mono, monospace"
    fontSize: "0.74rem"
    fontWeight: 400
    letterSpacing: "0.24em"
  reel-lead:
    fontFamily: "Archivo, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(1.5rem, 3.4vw, 2.6rem)"
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: "-0.03em"
  reel-caption:
    fontFamily: "Courier Prime, ui-monospace, SF Mono, monospace"
    fontSize: "0.7rem"
    fontWeight: 400
    letterSpacing: "0.2em"
  # The steps that exist between the named roles above. Several of these were
  # already specified in the prose below (the maker sentence at
  # clamp(.9rem,1.9vw,1.14rem) is named in Components), but prose is not
  # machine-readable, so they are enumerated here as well. Clamp endpoints count
  # as steps: a fluid size is only on-ramp if both ends are.
  scale:
    hud: "10px"            # HUD micro-caps and the sound toggle
    micro: "0.8rem"        # smallest label step
    tail-min: "0.82rem"    # hero tail
    tail-max: "0.98rem"
    maker-min: "0.9rem"    # hero maker sentence
    maker-max: "1.14rem"
    slab-min: "1.2rem"     # type-slab cover
    slab-max: "2.3rem"
    close-min: "2.1rem"    # closing word
    close-max: "6.4rem"
    panel-max: "8rem"      # pinned triptych panel word
rounded:
  none: "0px"
  seal: "999px"
spacing:
  act: "clamp(5rem, 12vw, 9rem)"
  stage: "clamp(3rem, 8vw, 6rem)"
components:
  cta:
    backgroundColor: "{colors.lit}"
    textColor: "{colors.night}"
    rounded: "{rounded.none}"
    padding: "1rem 2.2rem"
  hud:
    backgroundColor: "rgba(8,10,14,0.55)"
    textColor: "#EAF2F6"
    rounded: "{rounded.none}"
    padding: "7px 11px"
  link:
    textColor: "{colors.ink}"
    typography: "{typography.tag}"
---

# Design System: JS the WLD

## 1. Overview

**Creative North Star: "South Meets the Future"**

Two poles, held in tension on one page. The **South** is warm, physical, worn: paper grounds, rust and amber, real photographs, cardboard and felt and scratches. The **future** is a deep-sea instrument panel: near-black grounds, one electric cyan, hairline HUD edges, a receding grid that falls away under your feet. The site earns its interest by cutting hard between them rather than blending them into a comfortable middle.

There is **no serif anywhere**. The voice is a matte grotesque (Archivo, at heavy weights, tracked tight) against a typewriter (Courier Prime) for every label and every line of body copy. The one exception is the JS the WLD wordmark itself, which is an image asset — a stacked interlocking Didone lockup, white on transparency, which is why any ground it sits on must be dark.

This system explicitly rejects: the previous editorial/Didone-body world (warm eggshell everywhere, italic serif display, "porch letter" restraint), generic AI-slop SaaS marketing, and any crypto/blockchain visual language.

**Key Characteristics:**
- Contrast flips section to section — paper, dusk, electric, paper, black. Never a gradient between poles.
- Depth is real: CSS `perspective`, `translateZ`, a rotated ground plane, and three independently parallaxing texture layers.
- Things arrive by **growing toward the viewer**, not sliding up the page.
- Type is the artwork; imagery is evidence.

## 2. Colors

Two families that never mix into each other: warm Southern grounds, and one cold electric accent reserved for the future pole.

### Primary
- **Rust** (`#A8401D`): the Southern action color — tags, link underlines, warmth on paper grounds.
- **Electric** (`#40C4E8`): the future. Section 04 (Code), the HUD percent readout, the CTA, the wire lines, the receding grid.

### Secondary
- **Amber** (`#D99A42`): tags and links on dusk grounds only.

### Neutral
- **Paper** (`#EDEAE3`) / **Ink** (`#1B1916`): the reading pole.
- **Dusk** (`#171512`): warm dark, still Southern.
- **Night** (`#06080C`) / **Wire** (`#04060B`) / **End** (`#0A0C10`): the cold darks.
- **Bone** (`#E9E4D8`): text on any dark ground.

### Named Rules
**The Two-Pole Rule.** Every section commits to South or future. Rust and amber never appear on the wire ground; cyan never appears on paper. A section that uses both is a section that has decided nothing.

**The Cut, Not the Fade Rule.** Grounds change by hard edge between sections. No gradient transitions between paper and night — the jolt is the point.

## 3. Typography

**Display:** Archivo (400–900) — matte grotesque, used at 800/900 with tight negative tracking.
**Body / Label:** Courier Prime — typewriter, used for all body copy, tags, and HUD chrome.
**Wordmark:** an image asset, not a font.

**Character:** Industrial and plain-spoken. A hardware label maker and a typewriter, not a magazine.

### Hierarchy
- **Act** (900, `clamp(3.4rem,17vw,13rem)`, tracking -0.055em): the section words (WORDS / SONGS / CODE / SOUTH). Set at 13% opacity as a watermark on Southern grounds; full strength and glowing on the wire ground.
- **Craft** (900, `clamp(2.6rem,8vw,5.8rem)`): the hero's rotating word in its slot.
- **Heading** (800, `clamp(1.7rem,4vw,2.9rem)`): section headings.
- **Body** (Courier Prime, `clamp(0.86rem,1.5vw,1rem)`, line-height 1.9): all reading copy. The generous leading is what keeps a typewriter face readable at length.
- **Tag** (Courier Prime, 0.74rem, tracking 0.24em, uppercase): numbered section tags and HUD labels.

### Named Rules
**The No-Serif Rule.** No serif face ships on a surface built in this world. Not for quotes, not for emphasis, not for "warmth." The warmth comes from color, texture, and photography.

### Migration status (accurate as of this revision)

This world currently governs **the homepage only**. `/about`, `/book`, and `/field` still render the retired editorial world — Bodoni Moda display over Libre Baskerville body, eggshell grounds, the taped-photo motif — served from the shared `src/styles/global.css`. Those pages are **not** yet compliant with the No-Serif Rule or the two-pole palette.

Consequence for anyone working here: do not treat `global.css` as this system's stylesheet. It still carries the old type ramp (`1.12rem` body, `1.15rem` lede, `1.4rem` notecard) and the old motif classes, because inner pages depend on them. Migrating those pages means moving them onto Archivo/Courier and retiring the motif block — until that happens, this document describes the homepage and the direction, not the whole site.

## 4. Elevation

Depth is spatial, not decorative. Sections that hold imagery declare `perspective` (900–1100px) and elements arrive along the Z axis. Shadows are deep and soft (`0 40px 90px -28px rgba(0,0,0,.7)`) because objects are genuinely closer to the viewer, not because a card needed a border.

### Shadow Vocabulary
- **Object** (`0 40px 90px -28px rgba(0,0,0,.7)`): photographs and slabs that have grown into place.
- **Glow** (`0 0 40px rgba(64,196,232,.4)`): the CTA and any lit element on the wire ground.
- **HUD hairline** (`inset 0 0 0 1px rgba(255,255,255,.16)`): corner consoles.

### Depth alphas (not palette)

Inside the well, **cyan alpha encodes distance** — it is the depth cue, not decoration, so these values are a ladder rather than a set of loose colors. Frame borders run `rgba(64,196,232,.5)` near and `.85` on the farthest four (the far end reads as light, not line); frame bloom `.13` outer / `.07` inner, rising to `.4` / `.14` at depth; floor and roof grid lines `.30` horizontal / `.16` vertical; fog pool `.30 → .10 → transparent`. Changing one rung in isolation breaks the read of distance — move the ladder, not a step.

### Scrims and hairlines (not palette)

Chrome uses neutral alpha values that are deliberately **not** brand colors — they tint whatever ground they sit on rather than introducing a hue: seal fill `rgba(0,0,0,.62)`, seal ring `rgba(255,255,255,.22)`, HUD fill `rgba(8,10,14,.55)`, HUD hairline `rgba(255,255,255,.16)`, slab inner edge `rgba(255,255,255,.08)`. Treat these as a functional scrim set. Adding a *hue* to chrome is drift; adjusting a neutral alpha is not.

### Named Rules
**The Z-Axis Rule.** Content enters by scale and depth (`translateZ(-520px) scale(.42)` → identity), never by `translateY` alone. Things grow out of the screen.

## 5. Components

### Hero copy scale

The hero runs deliberately **small** against a huge wordmark — the contrast is the point, so nothing here scales with the mark. Name line `clamp(.72rem,1.5vw,.86rem)` tracked `.2em` uppercase in `#9FB0B8`; the maker sentence `clamp(.9rem,1.9vw,1.14rem)` in `#EDE9DF`. The three crafts (Words, Music, Code) are set **plain** — no per-word color, no weight change. An earlier version tinted each one; it read as decoration rather than a sentence.

Because the streams pass behind this copy, the block carries its own soft bed: `radial-gradient(62% 58% at 50% 50%, rgba(4,6,11,.82) → transparent 84%)`. Without it the text is genuinely unreadable over the brighter strands.

### Arrival motions

Three distinct entrances, chosen per content type — never one uniform reveal:
- **Grow** (photographs, the lightform): `translateZ(-520px) scale(.42)` → identity. Comes toward you.
- **Slide** (the music strip): alternating `translate3d(∓90px,0,0) rotate(∓4deg)` → identity, staggered 180ms on the back pair. Arrives from opposite sides.
- **Z-exit** (the pull-quote): `perspective(900px) translateZ(-420px)` → 0. Comes out at the reader.

### The Reel (signature)

The Music act turns the page on its side. The section fills the viewport, pins from its top edge, and a rail of nine portraits runs horizontally while the reader keeps using the wheel normally — vertical scroll is spent on horizontal travel before the page advances again. The scrollbar is never hijacked.

Each card also travels **inward** as it reaches the middle of the screen (`z −260 → 0`, scale `.88 → 1`, opacity `.55 → 1`), driven off the rail via ScrollTrigger's `containerAnimation` so depth tracks a card's *sideways* position rather than the page's vertical one. Without that the run is a flat conveyor.

Its own type steps: the lead line `clamp(1.5rem, 3.4vw, 2.6rem)` in the display grotesque, and card captions at `0.7rem` tracked `0.2em` in amber — one step below the standard tag because a caption sits under an image rather than heading a section.

**Hard constraints.** The section must own the full viewport (`min-height: 100svh`) and pin from `top top`; pinning a short band mid-screen reads as a strip sliding past, not as the page turning. `invalidateOnRefresh` is required — a stale width strands the rail mid-track on resize. Below 700px and under reduced motion there is no pin at all; the reel degrades to an ordinary swipeable row.

### The Well (signature)
The hero background is a corridor you fall into, not a backdrop. One `perspective: 560px` camera with `transform-style: preserve-3d` holds 14 hairline cyan frames stacked at `translateZ(i × -300px)`, plus a floor and roof plane at `rotateX(±80deg)` converging on the same vanishing point, plus a blurred cyan fog pool that hides the corridor's end. Frames fade with depth (`opacity: .92 − i×.062`) except the farthest four, which brighten so the far end reads as light rather than line. At rest the camera breathes on the genome's 13s cycle; on scroll it pushes forward, so the viewer falls in.

**Hover.** The strands answer the cursor: they lean toward it (harder the nearer they are) and the flow quickens ~90%. Pointer state is eased at 0.05–0.06 per frame so the reaction is fluid rather than twitchy.

**`variant="bed"`.** The same generative field runs quietly behind the dark acts (Code, Music, the close) at 55% opacity with stroke alpha halved, no fog. It ties the sections together without competing with content. Only dark grounds get a bed — never paper.

**Hard constraint (legacy CSS corridor, now replaced):** the earlier CSS-transform well capped camera Z at **300px** against a 560px perspective. As the camera approaches the perspective plane, projected scale goes asymptotic and the corridor detonates rather than receding — a nearest frame measured 8154px wide before the cap was added. Any change to `perspective` must move the cap with it, keeping a wide margin.

### Act Word
Full-bleed section word, overflow-clipped, 13% opacity on Southern grounds and fully lit with a double glow on wire.

### Grow Figure
Photograph or type slab that enters from `translateZ(-520px) scale(.42)` and settles with a small per-instance tilt (`--tilt`).

### HUD Console
Fixed corner panels: blurred dark fill, hairline inset edge, Courier micro-caps. Bottom-left names the current section; bottom-right is a live scroll percentage in cyan.

### CTA
Solid cyan block, black text, square corners, cyan bloom. The only filled button in the system.

## 6. Do's and Don'ts

### Do:
- **Do** flip ground and text color completely at every section boundary.
- **Do** enter content along Z (grow toward the viewer) with 1100–1400ms ease-out.
- **Do** keep texture below 0.11 opacity — depth, never pattern.
- **Do** reserve cyan for the future pole and the CTA.

### Don't:
- **Don't** use a serif anywhere.
- **Don't** slide content up the page as the default entrance.
- **Don't** put rust/amber on the wire ground or cyan on paper.
- **Don't** reintroduce the retired editorial world (eggshell-everywhere, italic Didone body, taped-photo motif as the primary language).
- **Don't** use crypto/blockchain visual language.
- **Don't** gradient between the two poles to "ease" the transition.
