# Maverick & Miller HVAC — project-local rules

Overrides global `~/.claude/CLAUDE.md` on conflict. Static HTML site deployed to Vercel at `maverickandmillerhvac.com`.

## Business facts (do not fabricate or deviate)

- **Legal name**: Maverick & Miller HVAC (alternateName: Maverick HVAC LLC)
- **Never abbreviate to "M&M"** — M&M Heating & Cooling is a separate, established 45-year Toledo company. Brand collision risk. Always use the full name.
- **Phone**: (419) 777-6061
- **Address**: 7628 Trotter Road, Toledo, OH 43617
- **Hours**: Monday to Friday, 8:00 AM to 6:00 PM (emergency service available)
- **Founded**: 2024
- **Founders**: Shane Miller, Kindle VanWormer
- **BBB**: A+ rating

## Copywriting rules

- No em dashes anywhere. Use commas, periods, or "and" instead.
- No AI vocabulary (leverage, streamline, unlock, optimize, empower, robust, dynamic, seamless, cutting-edge, etc.)
- No fabricated specifics. If a service has a price range, warranty, turnaround claim, or certification, confirm with Shane or Kindle before writing it.
- Tone: plain prose, operator-to-operator. No folksy flourishes. No quirky voice.
- Direct answers over marketing fluff. AI answer engines (ChatGPT, Perplexity, Gemini) cite specific and factual, not "we pride ourselves on delivering exceptional service."
- Run new or edited copy through `the-humanizer-from-linkden` skill before committing.

## Design rules

- Palette: cream `#faf7f2`, warm `#f0ebe3`, sand `#ddd7cc`, stone `#b5ad9f`, charcoal `#2c2a26`, ink `#1a1917`, red `#c0392b`, red-deep `#a13125`
- Fonts: Outfit (sans, headers and UI), Source Serif 4 (serif, body prose)
- Editorial feel, not tech-startup feel. No gradient blobs, glassmorphism, rounded-2xl everywhere, or centered hero + 3-col features.
- Mobile tap highlights disabled on interactive elements. Image long-press callouts disabled on content images.

## Site structure

- 18 pages total, flat URLs, `cleanUrls: true` in vercel.json
- 6 core: `/`, `/about`, `/services`, `/service-area`, `/reviews`, `/contact`
- 7 service: `/ac-repair`, `/furnace-repair`, `/water-heater-installation`, `/ductless-mini-splits`, `/air-filtration`, `/hvac-maintenance`, `/commercial-hvac`
- 5 city: `/hvac-perrysburg-oh`, `/hvac-sylvania-oh`, `/hvac-whitehouse-oh`, `/hvac-waterville-oh`, `/hvac-bowling-green-oh`
- Shared header between `<!-- NAV-START -->` and `<!-- NAV-END -->`, shared footer between `<!-- FOOTER-START -->` and `<!-- FOOTER-END -->`. Use `sed` with multiple `-e` flags for bulk edits across all 18 pages.

## Generator tooling

- `_template.html` is the shared skeleton.
- `_content.py` holds service and city page content data.
- `_gen.py` renders HTML. Run with `python _gen.py` after editing `_content.py`.
- Regenerating overwrites the 7 service and 5 city HTML files. Do not hand-edit those HTML files directly, edit the Python data and regenerate.
- The 6 core pages (home, about, services, service-area, reviews, contact) are hand-authored, not generated.

## Schema

- HVACBusiness JSON-LD on every page (shared ID `@id: https://maverickandmillerhvac.com/#business`)
- Page-type-specific schema per page: AboutPage + Organization + Person on /about, ContactPage + ContactPoint on /contact, Service on each service page, LocalBusiness with areaServed on each city page
- FAQPage schema on every service page and city page
- BreadcrumbList on every non-home page
- When adding a new page, include at minimum: HVACBusiness reference, BreadcrumbList, and page-type schema.

## Planning artifacts

All in `/planning/`. Read `planning/README.md` first. Key docs:

- `SEO-STRATEGY.md` — high-level plan, flags M&M brand collision
- `SITE-STRUCTURE.md` — URL map, linking graph, schema plan
- `KEYWORD-MAP.md` — keyword per page, intent, difficulty
- `COMPETITOR-ANALYSIS.md` — top 5 Toledo HVAC competitors
- `LOCAL-SEO.md` — GBP, NAP, citations, map pack, GEO
- `PROGRAMMATIC-PLAN.md` — Tier 2 city × service scaling plan (NOT v1)
- `BACKLINK-STRATEGY.md` — off-site plan (Janon executes post-launch)
- `IMPLEMENTATION-ROADMAP.md` — build sequence

## Known pending items (don't touch without checking)

- **GSC verification**: `<meta name="google-site-verification" content="REPLACE_WITH_GSC_VERIFICATION_CODE">` on every page. Replace content value once Shane/Kindle set up Google Search Console.
- **Reviews**: 8 placeholder testimonials on `/reviews`, 3 on `/`. Replace with real Google reviews once Janon has them. Add `AggregateRating` schema to `/` and `/reviews` once 5+ real reviews exist.
- **Contact form**: plain HTML form on `/contact`, submits nowhere (action=\"#\"). Decision pending on GHL iframe vs HTML form POST. Ask client.
- **GA4**: not installed (matches Big Horn pattern).
- **Map embed on /contact**: placeholder embed URL. Replace with real Google Maps embed URL when Janon has GBP place ID.

## Future work (not v1)

- **Scroll animation pipeline** on home hero (`scroll-animation-pipeline` skill)
- **Tier 2 programmatic pages** (up to 30 net new city × service combos per `planning/PROGRAMMATIC-PLAN.md`)
- **Blog** (separate `/blog/` hub with HVAC maintenance tips, seasonal content, E-E-A-T builders)
- **Real reviews import** with AggregateRating schema
- **Contact form wiring** (GHL vs HTML POST)

## Deploy

- `npx vercel --prod --yes` from project root. `git push` is NOT the deploy trigger — Vercel auto-deploy from GitHub is not reliably connected here.
- Never deploy without user approval.
- `vercel.json` has `cleanUrls: true` so `/ac-repair` serves `ac-repair.html`.
