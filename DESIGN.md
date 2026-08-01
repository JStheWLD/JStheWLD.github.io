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
  rust: "#C1512A"
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

This document governs the brand, not a website. Every rule below is stated so it holds in any medium — page, screen, stage, print, or object. Where a rule needs a particular technique to land in a particular medium, that technique is recorded as an *Implementation note* and is subordinate: the note may be rewritten freely when the medium changes, the doctrine above it may not.

**Parentage (2026-07-31).** This world is a **skin of the light form**. *The Sound of Something More · Light Form Design System* is the genome: it owns the token names, the marks, the shared eighty percent of motion and its living tether, and the Always/Never. Everything below sets that genome's values for one surface. A skin re-values, it never rewrites — so where this document and the genome disagree on a **value**, this document wins for this surface; where they disagree on the **contract**, the genome wins everywhere. What this skin inherits and cannot re-set: the truth-bird and the glass-HUD grammar, the family palette as ancestor, the shared motion, and the standing prohibition on a surface that cannot breathe.

Two poles, held in tension on one page. The **South** is warm, physical, worn: paper grounds, rust and amber, real photographs, cardboard and felt and scratches. The **future** is a deep-sea instrument panel: near-black grounds, one electric cyan, hairline HUD edges, a receding grid that falls away under your feet. The site earns its interest by cutting hard between them rather than blending them into a comfortable middle.

There is **no serif anywhere**. The voice is a matte grotesque (Archivo, at heavy weights, tracked tight) against a typewriter (Courier Prime) for every label and every line of body copy. The one exception is the JS the WLD wordmark itself, which is an image asset — a stacked interlocking Didone lockup, white on transparency, which is why any ground it sits on must be dark.

This system explicitly rejects: the previous editorial/Didone-body world (warm eggshell everywhere, italic serif display, "porch letter" restraint), generic AI-slop SaaS marketing, and any crypto/blockchain visual language.

**Reading the numbers.** Every measurement in this document is a default and a direction, not a permission. Each is written as the value that works and the place it stops working, so a value outside it is a decision to argue with rather than a violation to report — trust your eyes over the figure. The exceptions are marked **load-bearing**: a handful of numbers where crossing the line breaks the render rather than the taste. Those say so in those words, and they mean it.

**Key Characteristics:**
- Contrast flips section to section — paper, dusk, electric, paper, black. Never a gradient between poles.
- Depth is real: CSS `perspective`, `translateZ`, a rotated ground plane, and three independently parallaxing texture layers.
- Things arrive by **growing toward the viewer**, not sliding up the page.
- Type is the artwork; imagery is evidence. Where a surface can be touched, pointed at, or walked past, the evidence answers — but it answers by a few degrees, never by performing.

## 2. Colors

Two families that never mix into each other: warm Southern grounds, and one cold electric accent reserved for the future pole.

### Primary
- **Rust** (`#C1512A`): the Southern action color — tags, link underlines, warmth on paper grounds. Taken from the genome's family palette, which is the ancestor of every skin's warm pole. This skin previously ran `#A8401D`; three documents once shipped three different rusts and this is the one that survived.
- **Electric** (`#40C4E8`): the future. Section 04 (Code), the HUD percent readout, the CTA, the wire lines, the receding grid.

### Secondary
- **Amber** (`#D99A42`): tags and links on dusk grounds only.

### Neutral
- **Paper** (`#EDEAE3`) / **Ink** (`#1B1916`): the reading pole.
- **Dusk** (`#171512`): warm dark, still Southern.
- **Night** (`#06080C`) / **Wire** (`#04060B`) / **End** (`#0A0C10`): the cold darks.
- **Bone** (`#E9E4D8`): text on any dark ground.

### Named Rules
**The Two-Pole Rule.** Every section commits to South or future. Rust and amber do not carry the wire ground; cyan does not carry paper. What the rule forbids is a section spending both palettes as though it never chose — it governs the commitment, not every pixel inside it. A single functional mark that plainly isn't palette (a focus ring, a state colour, an optical effect) is not a section changing its mind.

**The Cut, Not the Fade Rule.** Grounds change by hard edge between sections. No gradient transitions between paper and night — the jolt is the point.

**The One Cyan Rule.** `#40C4E8` is the single value this skin and the genome hold in common, byte for byte. It is the point of contact, so it is never re-tinted to taste at either end — when it moves, it moves in both places or the family breaks. Every other value here is this skin's own.

**The Channel Exemption.** Split-channel effects — chromatic aberration, anaglyph, misregistration — are not palette colour, and the Two-Pole Rule does not govern them. Their red and cyan are two halves of one separated image, not two accents on a ground, so they may run on either pole. They must stay pure channel values (`#FF1F1F` / `#E01B1B` / `#00E5FF` / `#00B7D8`) and never brand rust or brand cyan — the moment a channel is a brand colour, the effect reads as decoration instead of separation. This holds in print misregistration and on screen alike.

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

**Scope of that rule (genome amendment, 2026-07-31).** The genome locks the display **role**, not the face: every skin declares one display voice and never mixes. This skin declares Archivo; the light form and its installations declare Bodoni Moda. So the No-Serif Rule governs this skin and no further — a Didone on an installation is that skin's declared voice, not a violation of this one. The rule is absolute inside its own world and silent outside it.

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
**The Z-Axis Rule.** Content enters by scale and depth (`translateZ(-520px) scale(.42)` → identity). Things grow out of the screen — that is the house entrance, and it is what a reader should feel most of the time. A vertical slide isn't banned; it is simply not the default, and it earns its place only when the content genuinely arrives from off-page rather than from depth. What the rule is really against is every element on the page rising the same inch.

## 5. Components

Each entry states the behaviour first and the technique second. Passages marked *Implementation note* describe how the behaviour is currently achieved on the web; they are a record, not the rule. A new medium inherits the entry and writes its own note.

### Hero copy scale

The hero runs deliberately **small** against a huge wordmark — the contrast is the point, so nothing here scales with the mark. Name line `clamp(.72rem,1.5vw,.86rem)` tracked `.2em` uppercase in `#9FB0B8`; the maker sentence `clamp(.9rem,1.9vw,1.14rem)` in `#EDE9DF`. The three crafts (Words, Music, Code) are set **plain** — no per-word color, no weight change. An earlier version tinted each one; it read as decoration rather than a sentence.

Because the streams pass behind this copy, the block carries its own soft bed: `radial-gradient(62% 58% at 50% 50%, rgba(4,6,11,.82) → transparent 84%)`. Without it the text is genuinely unreadable over the brighter strands.

### Arrival motions

Entrances are chosen per content type — never one uniform reveal. This is a vocabulary, not a closed set; a new content type may earn a new entrance, but adding one that duplicates an existing feel is drift. So far:
- **Grow** (photographs, the lightform): `translateZ(-520px) scale(.42)` → identity. Comes toward you.
- **Slide** (the music strip): alternating `translate3d(∓90px,0,0) rotate(∓4deg)` → identity, staggered 180ms on the back pair. Arrives from opposite sides.
- **Z-exit** (the pull-quote): `perspective(900px) translateZ(-420px)` → 0. Comes out at the reader.

### The Mark
The wordmark comes apart and reassembles. It **shatters**, it does not slide: irregular angular shards along fracture lines, never equal horizontal bands. Bands read as a technical exploded-view diagram — correct for a parts catalogue, wrong for a mark that should look struck. Shard count sits around 8 to 14 — the count itself matters less than the two ways it fails: too few reads as cut, too many reads as confetti. Each shard carries its own rotation and its own distance from the viewer, and the nearest shards genuinely enlarge. Reassembly is the same fracture run backwards, and arrives with a click rather than a settle.

**The Front-Loaded Rule.** The separation happens in the first third of whatever drives it — a scroll, a cut, a walk past — while the mark is still in frame. Motion saved for the end is spent after the mark has left.

*Implementation note (web).* The shards need a `perspective` on their shared container; without it the rotation flattens into a horizontal squash and the distance does nothing at all. The driving ease must be front-loaded, and the range must complete while the hero is still on screen.

### The Reel (signature)

The Music act turns the page on its side. The section fills the viewport, pins from its top edge, and a rail of nine portraits runs horizontally while the reader keeps using the wheel normally — vertical scroll is spent on horizontal travel before the page advances again. The scrollbar is never hijacked.

Each card also travels **inward** as it reaches the middle of the screen (`z −260 → 0`, scale `.88 → 1`, opacity `.55 → 1`), driven off the rail via ScrollTrigger's `containerAnimation` so depth tracks a card's *sideways* position rather than the page's vertical one. Without that the run is a flat conveyor.

Its own type steps: the lead line `clamp(1.5rem, 3.4vw, 2.6rem)` in the display grotesque, and card captions at `0.7rem` tracked `0.2em` in amber — one step below the standard tag because a caption sits under an image rather than heading a section.

**Constraints.** The section should own the full viewport (`min-height: 100svh`) and pin from `top top`; pinning a short band mid-screen reads as a strip sliding past, not as the page turning. Load-bearing: `invalidateOnRefresh` is required — a stale width strands the rail mid-track on resize. Below 700px and under reduced motion there is no pin at all; the reel degrades to an ordinary swipeable row.

### The Well (signature)
The hero background is a corridor you fall into, not a backdrop. One `perspective: 560px` camera with `transform-style: preserve-3d` holds 14 hairline cyan frames stacked at `translateZ(i × -300px)`, plus a floor and roof plane at `rotateX(±80deg)` converging on the same vanishing point, plus a blurred cyan fog pool that hides the corridor's end. Frames fade with depth (`opacity: .92 − i×.062`) except the farthest four, which brighten so the far end reads as light rather than line. At rest the camera breathes on the genome's 13s cycle; on scroll it pushes forward, so the viewer falls in.

**Hover.** The strands answer the cursor: they lean toward it (harder the nearer they are) and the flow quickens ~90%. Pointer state is eased at 0.05–0.06 per frame so the reaction is fluid rather than twitchy.

**`variant="bed"`.** The same generative field runs quietly behind the dark acts (Code, Music, the close) at 55% opacity with stroke alpha halved, no fog. It ties the sections together without competing with content. Only dark grounds get a bed — never paper.

**Load-bearing (legacy CSS corridor, now replaced):** the earlier CSS-transform well capped camera Z at **300px** against a 560px perspective. As the camera approaches the perspective plane, projected scale goes asymptotic and the corridor detonates rather than receding — a nearest frame measured 8154px wide before the cap was added. Any change to `perspective` must move the cap with it, keeping a wide margin.

### The Answer
Surfaces answer the hand, and each answers in its own medium: the strands sound, the strings bend, a photograph tilts, a layered figure separates. A surface that answers in a way unrelated to what it *is* is decoration.

**The Small-Answer Rule.** Tilt sits around **6 degrees**, separation around **3% of the element's own width**, and both come home within about 700ms of being left alone. Somewhere past ten degrees the surface stops answering and starts performing — that crossing is the real rule, and the figures are only where it comfortably sits. The answer should be noticed on the second look, not the first.

### The Instrument
The brand has one instrument, and it is a plucked string. However many playable surfaces exist, they are registers of that one instrument rather than separate voices — and there is one permission, asked once. Sound never begins on its own, in any medium: not on a page, not on a stand, not in a room someone walked into.

Everything is tuned to **G mixolydian**, the key and mode Southern rock lives in. This is a key and a mode, never a melody: no song is encoded anywhere in this brand. Registers stack rather than transpose — high strings against low ones — so any two surfaces struck together stay inside the harmony.

*Implementation note (web).* One AudioContext, one unlock gesture, one toggle. A second context would mean a second permission the reader never agreed to.

### Act Word
Full-bleed section word, edge-clipped, 13% opacity on Southern grounds and fully lit with a double glow on wire.

Each act word may carry **one** optical treatment and only one — chromatic aberration, decode, anaglyph depth, or none. The treatment is driven by the reader's own movement through the work, so the word is doing it *because* someone is moving. Separation runs from 0 at rest to around **0.06em**: far enough to read as a deliberate optical split at a glance, short enough that the word stays a word. The failure is the moment the eye reads two words instead of one split word, and that is the line to watch rather than the figure. Channel opacity sits near **0.5** against light grounds; much below and the fringes vanish into the ground, so the effect exists only for whoever made it.

### Grow Figure
Photograph or type slab that enters from `translateZ(-520px) scale(.42)` and settles with a small per-instance tilt (`--tilt`).

### The Stamp

Two marks, and this skin restyles neither — they come down from the genome intact. The **truth-bird** is a spread-wing bird held in a dark roundel, pressed into a corner of every world like wax; it is the most literal signature the brand has. It sits at an edge rather than in the composition, small and constant, and it is never enlarged into decoration or knocked out to match a section's palette — the roundel carries its own dark so it reads on any ground. The **wordmark** is the stacked interlocking lockup, white on transparency, which is why any ground beneath it must be dark; what it *does* is described under The Mark.

**The One Stamp Rule.** One truth-bird per surface, as a rule of thumb — a second one in the same view starts turning a signature into a pattern.

*Implementation note (web).* The bird ships as `/assets/bird-white.png` at 18px inside the top-left seal, which doubles as the home link, so the stamp and the way home are the same object. The wordmark is `/assets/jswld-wordmark.png`, tiled across the shards of The Mark. `Seal.astro` (a ring-text badge) and `Bird.astro` (pen-and-ink line art) are separate marks in the repo and are currently used by no page.

### HUD Console
Fixed corner panels: blurred dark fill, hairline inset edge, Courier micro-caps. Bottom-left names the current section; bottom-right is a live scroll percentage in cyan.

### CTA
Solid cyan block, black text, square corners, cyan bloom. The only filled button in the system.

## 6. Do's and Don'ts

### Do:
- **Do** flip ground and text color completely at every section boundary.
- **Do** enter content along Z (grow toward the viewer) with 1100–1400ms ease-out.
- **Do** keep texture around 0.11 opacity or under — the line is where it starts reading as pattern instead of depth.
- **Do** reserve cyan for the future pole and the CTA.
- **Do** let a surface answer the hand in its own medium, within the Small-Answer Rule.
- **Do** keep split-channel effects on pure channel values, never on brand colours.

### Don't:
- **Don't** use a serif anywhere.
- **Don't** slide content up the page as the default entrance.
- **Don't** put rust/amber on the wire ground or cyan on paper.
- **Don't** reintroduce the retired editorial world (eggshell-everywhere, italic Didone body, taped-photo motif as the primary language).
- **Don't** use crypto/blockchain visual language.
- **Don't** gradient between the two poles to "ease" the transition.
- **Don't** let the future pole drift to neon-on-black. It is a deep-sea instrument panel — one cyan, warm ink, real photography — never cyberpunk.
