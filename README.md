# In the Wld

The house Jonathan Sexton's work lives in. One writer and musician, one question, many forms.

Static site built with [Astro](https://astro.build). Reading-first, ships no JavaScript unless a page asks for it.

## The rooms

- `/` — the story house (one-page long scroll)
- `/book` — The Sound of Something More (held quiet, no cover yet)
- `/field` — interactive pieces and the 11:11 essays
- `/field/first-family/` — the Lomax "First Family of American Roots Music" pod (a standalone piece under `public/`)
- `/about` — Jonathan
- The Storm Door (the letter) lives on Substack at https://thestormdoor.substack.com and is linked out, not mirrored here.

## Working on it

```
npm install
npm run dev      # http://localhost:4321
npm run build    # outputs to dist/
npm run preview  # serve the build
```

## Design

Palette, type, and marks follow the JS the WLD identity. Daylight is the reading skin (eggshell `#EDEAE3`, warm charcoal ink `#393533`, rust accent `#A53B1F`). Lamplit (charcoal ground, white Truth Bird, filmic photography) carries the hero and section breaks. Bodoni Moda for display, Libre Baskerville for body. Full system in the SSM project at `.agents/context/DESIGN.md`.

## Deploy

Target is Vercel (static, zero-config for Astro). The domain `inthewld.com` is not wired yet; deploy to a preview URL first and repoint DNS only after the current site is cleared.
