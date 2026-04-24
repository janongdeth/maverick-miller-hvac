# Implementation Roadmap — 18-page Build

Execution order. Each page = its own atomic commit (conventional commits).

---

## Phase 1 — Design foundation (1 commit)

**Deliverables:**
- Color palette, type scale, spacing system defined in CSS custom properties
- Shared header + footer components with `<!-- NAV-START -->` / `<!-- NAV-END -->` marker comments for bulk sed edits
- Base page template (any new page = copy template + fill content blocks)
- Shared schema block (HVACBusiness JSON-LD, pulled into every page)

**Skills applied:** ui-ux-audit (read current state) → frontend-design + ui-ux-pro-max (draft distinctive layout)

**Design brief:**
- Avoid AI-trope list (gradient blobs, glassmorphism, rounded-2xl everywhere, centered hero + 3-col features)
- Editorial / local-trade feel: strong typography, real photography, restrained color
- Palette direction: think work-boots not tech-startup. Deep navy or charcoal + a warm accent (copper, brick, sunrise orange). No neon.
- Distinctive home hero: asymmetric layout, not centered hero text over stock photo
- Mobile tap-highlight disabled + image long-press disabled (per global CLAUDE.md)

**Commit:** `feat: design system + shared header/footer for site expansion`

---

## Phase 2 — Build loop (18 commits, one per page)

Build order = value × difficulty (low difficulty + high value first):

### Wave 1 — Foundation pages (required before other pages link to them)
1. `/` Home (trim existing + reflow to new IA)
2. `/contact`
3. `/about`
4. `/services` (overview, placeholder links to service pages until they exist)
5. `/service-area` (overview, placeholder links to city pages until they exist)
6. `/reviews` (placeholder quotes)

### Wave 2 — Service pages (easy wins first)
7. `/air-filtration` (low difficulty)
8. `/hvac-maintenance` (medium, low fluff)
9. `/ac-repair` (high difficulty, required core)
10. `/furnace-repair` (high difficulty, required core)
11. `/water-heater-installation` (medium, plumber-heavy SERP)
12. `/ductless-mini-splits` (medium, underserved by competitors)
13. `/commercial-hvac` (highest difficulty, most entrenched — build last)

### Wave 3 — City pages (quick wins first)
14. `/hvac-whitehouse-oh` (low-med difficulty, opportunity)
15. `/hvac-waterville-oh` (low-med difficulty, opportunity)
16. `/hvac-perrysburg-oh` (high difficulty, highest income city)
17. `/hvac-sylvania-oh` (high difficulty)
18. `/hvac-bowling-green-oh` (medium-high, college town context)

### Per-page workflow (repeat 18x)
1. Copy base template → new file
2. Write HTML structure + fill content blocks
3. Write page-specific CSS additions (if any)
4. Add page-specific JSON-LD schema
5. Run copy through humanizer filter (no em dashes, no buzzwords, no AI vocab, plain prose)
6. Apply seo-page mental checks (title ≤60 char, meta ≤155 char, H1 exact-match intent, 500+ words for service/city pages, internal links present)
7. Apply seo-content mental checks (E-E-A-T signals, AI-citation-readiness, FAQPage schema for service/city pages)
8. Apply seo-schema checks (proper types, valid JSON-LD)
9. Source images from Unsplash (CDN-ID scrape), convert to webp 80% max 1200px, kebab-case
10. Commit: `feat: add [page-name] page`

---

## Phase 3 — Site-wide SEO (5-6 commits)

After all 18 pages exist:

### Commits
1. `chore: generate sitemap.xml + robots.txt` — seo-sitemap pass, submit to GSC later
2. `feat: add GSC verification meta slot + llms.txt` — GSC verification tag placeholder, llms.txt for AI crawler intro
3. `chore: technical SEO audit fixes` — seo-technical pass (Core Web Vitals, crawlability, hreflang check, canonical audit)
4. `chore: GEO / AI SEO optimizations` — seo-geo pass (FAQ schema coverage, structured answer blocks, entity clarity)
5. `chore: image SEO + alt text audit` — seo-images pass across all new images
6. `chore: full-site SEO audit passes` — seo-audit + seo-maps + seo-drift baseline captured

### Skipping
- seo-dataforseo — no API key
- seo-backlinks verify — no backlinks exist yet

### Light touch
- seo-hreflang — English-only, confirms no hreflang issues exist
- seo-google — document GSC setup for Janon, don't execute without his account

---

## Phase 4 — Finalize (2 commits)

1. `chore: run simplify pass across all pages` — simplify skill, catches header/footer drift and duplicated CSS
2. `docs: add project CLAUDE.md` — init skill, encodes brand rules / tokens / nav / future plans for Option B + scroll animation

---

## Phase 5 — Later (NOT this build)

- Real reviews import (Janon fetches from GBP once live)
- Contact form (GHL iframe vs HTML form — client decides)
- Tier 2 programmatic pages (12 cities × 7 services, up to 30 net new pages)
- Scroll animation on home hero (scroll-animation-pipeline skill)
- Blog launch

---

## Total commit count

Phase 1: 1
Phase 2: 18
Phase 3: 5-6
Phase 4: 2

**Total: ~26-27 commits**, all atomic, conventional format, none pushed, none deployed. Janon runs `npx vercel --prod --yes` when ready.

## Time estimate

Conservative, assuming no blockers: this is a full session's work.
Phase 1 ~15 min
Phase 2 ~6-8 min per page × 18 = ~2-2.5 hours
Phase 3 ~30-45 min
Phase 4 ~15 min
**Total: ~3-4 hours of focused build**
