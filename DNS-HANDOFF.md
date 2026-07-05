# Pointing inthewld.com at the site

The steps to move inthewld.com from the preview onto the real domain, once you've
greenlit the build and the old B2B content is down. This is your manual step. I don't
touch DNS. Hand this to whoever manages the domain at the registrar if it isn't you.

The preview stays live at https://jsthewld.github.io/ as staging the whole time, so
nothing is at risk while the switch is coordinated.

## The order of operations

1. **Confirm the old site is down.** Per the firewall, the B2B / crypto content comes
   off inthewld.com before author work points at it. Make sure the current deployment
   is retired and you know which DNS records it left behind (see step 4).

2. **Put the site on Vercel.** The repo is `JStheWLD/JStheWLD.github.io` (or a renamed
   copy if you'd rather not keep the author site in your github.io namespace). In Vercel:
   New Project, import the repo, framework preset **Astro**, build command `npm run build`,
   output directory `dist`. Deploy. You get a `*.vercel.app` URL. Confirm it looks right.
   (This is the one step that needs your Vercel login. Once it's connected, every push to
   `main` redeploys on its own.)

3. **Add the domain in Vercel.** Project → Settings → Domains → add `inthewld.com` and
   `www.inthewld.com`. Vercel then shows you the exact DNS records to create. Use the
   values Vercel displays, not the ones written from memory below, since Vercel's target
   addresses change. The shape is always one of these two:

   - **Records at your current registrar (simplest, keeps email and other records where
     they are):**
     - Apex `inthewld.com`: an **A** record to the IP Vercel shows (historically
       `76.76.21.21`).
     - `www`: a **CNAME** to the host Vercel shows (historically `cname.vercel-dns.com`).
   - **Or hand the whole zone to Vercel:** change the domain's **nameservers** to the two
     Vercel gives you. Cleaner long term, but only do this if nothing else important is
     running on the domain's DNS, because it moves all records, email included.

   Recommended: the A + CNAME approach, so email and anything else on the domain stay put.

4. **Remove the old records first.** Delete any A, AAAA, or CNAME on the apex and `www`
   that pointed at the old B2B host. Two live answers for the same name is the usual cause
   of a switch that half-works.

5. **Pick the canonical form.** Decide whether the site lives at `inthewld.com` with `www`
   redirecting to it, or the reverse. Apex-canonical is the norm. Vercel sets the redirect
   for you once both are added.

6. **Wait for propagation and SSL.** DNS changes take anywhere from a few minutes to a few
   hours depending on the old TTL. Vercel issues the HTTPS certificate automatically once
   it sees the records resolve. The domain shows "Valid Configuration" in Vercel when it's
   done.

## How to know it worked

- `https://inthewld.com` loads the site with a valid padlock.
- `https://www.inthewld.com` redirects to the canonical form (or the reverse, whichever
  you chose).
- `dig inthewld.com +short` returns the Vercel target, not the old host.

## A note on the preview

Keep `jsthewld.github.io` up until inthewld.com is confirmed live and correct. After that
it can be deleted or left as a mirror. If you kept the author site in the `JStheWLD.github.io`
repo, renaming that repo later is a two-minute change and doesn't affect the Vercel domain.
