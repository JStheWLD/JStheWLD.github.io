// @ts-check
import { defineConfig } from 'astro/config';

// Static output. Reading-first, ships no JS unless a page asks for it.
// Deploys as-is to Vercel (or any static host).
export default defineConfig({
  site: 'https://inthewld.com',
  trailingSlash: 'ignore',
  build: {
    format: 'directory',
  },
});
