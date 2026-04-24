# Local SEO Plan — Maverick & Miller HVAC

## Business classification

- **Type**: Hybrid (physical HQ at 7628 Trotter Road, Toledo OH + service-area business across 12 NW Ohio cities)
- **Industry**: Home Services → HVAC
- **GBP primary category**: "HVAC Contractor" (highest-weight local pack signal)
- **GBP secondary categories (4 recommended per BrightLocal)**:
  1. Air Conditioning Contractor
  2. Heating Contractor
  3. Furnace Repair Service
  4. Commercial Refrigerator Supplier *(covers commercial HVAC sub-vertical)*

## NAP consistency

Authoritative NAP (must match across site + GBP + citations exactly):
```
Name:    Maverick & Miller HVAC
Address: 7628 Trotter Road, Toledo, OH 43617
Phone:   (419) 777-6061
Website: https://maverickandmillerhvac.com
Hours:   Mon-Fri 8:00 AM – 6:00 PM
```

NAP placement on site:
- Header: phone only (prominent tel: link)
- Footer: full NAP on every page
- Contact page: full NAP + hours + map embed
- LocalBusiness schema: full NAP on every page (via shared script block)

## Google Business Profile checklist

Janon will handle the GBP itself. The website needs to support it:

- [ ] Website URL in GBP points to `/` (not a sub-page — Sterling Sky guidance)
- [ ] Schema NAP matches GBP NAP exactly (case, punctuation, abbreviations)
- [ ] Hours on website match GBP hours
- [ ] Service list on website matches GBP services
- [ ] Photos on website should be uploadable to GBP (we're using stock — client may want to swap later with real job photos)
- [ ] FAQ sections on service pages mirror questions GBP users actually ask (feeds GBP Ask Maps Gemini AI as of Dec 2025)

## Reviews strategy

v1: Placeholder quotes on `/reviews` and 2-3 on `/`. Placeholder structure:
```html
<blockquote>
  <p>"[Short testimonial placeholder — 1-2 sentences]"</p>
  <cite>— [First Name] [Last Initial], [City] OH</cite>
</blockquote>
```

Janon to replace with real Google reviews later. Once real:
- Add `AggregateRating` schema to `/` and `/reviews` (requires min 5 reviews per Google guidelines)
- Add `Review` schema per testimonial
- Review response strategy (Whitespark 2026: response rate matters — aim for 100%)

## Citation plan (documented, for Janon to execute)

Top-priority citations for home services in NW Ohio:
1. Google Business Profile (anchor)
2. BBB (Maverick has A+ — claim and link it)
3. Yelp
4. Angi (HomeAdvisor merged)
5. Facebook Business Page
6. Nextdoor Business
7. Better Homes & Gardens (TripAdvisor of home services)
8. Houzz
9. Chamber of Commerce — Toledo Regional, Perrysburg Area, Sylvania Area
10. Local newspaper directories — Toledo Blade, Sentinel-Tribune (BG)

All citations must use exact NAP above. Inconsistent NAP is the #2 local pack negative factor.

## Map pack strategy

Goal: rank in the 3-pack for "HVAC Toledo", "AC repair Toledo", "furnace repair [city]" across target cities.

Proximity accounts for 55.2% of ranking variance (Search Atlas). Can't change physical location, but can:
1. Add geo-grid microdata signaling service in each of the 5 target cities (via LocalBusiness `areaServed` on each city page)
2. Embed Google Map on `/contact` centered on Toledo 43617
3. Include specific neighborhood/ZIP mentions on each city page (proximity to specific sub-areas)
4. Service schema per service page with `areaServed` listing all 12 cities

## AI search / ChatGPT optimization (GEO)

BrightLocal LCRS 2026: 45% of local searches now include AI (ChatGPT, Perplexity, Gemini). ChatGPT local conversion: 15.9% vs Google organic 1.76%.

To get cited in AI responses:
1. **Clear structured NAP** on every page (already planned via schema)
2. **FAQ content** that answers natural-language questions ("Who is the best HVAC company in Toledo?", "How much does furnace repair cost in Toledo?", "Does [company] service Perrysburg?")
3. **Specific, factual content** (avoid marketing fluff; AI citations reward specificity: "Founded 2024 by Shane Miller and Kindle VanWormer" ranks better than "experienced team")
4. **Entity linking** — Person schema for founders, Organization schema with `founder` array, BBB accreditation linked via `hasCredential`
5. **llms.txt** file at root — simple plain-text site summary for AI crawlers (low effort, growing signal)

## Business-hours-open factor

Whitespark 2026 ranking factor #5: businesses open at search time rank higher. Hours M-F 8-6 leave gaps evenings + weekends (common emergency HVAC search times). Recommend client consider either:
- Emergency on-call pricing advertised (extends effective hours)
- Saturday hours (even 9-1)

Not a build decision, but worth flagging to Janon.

## Success metrics (for post-launch GSC tracking)

- Impressions on "hvac toledo" variants (target: visible within 8 weeks)
- Local pack appearance for "hvac [city]" queries (target: top 20 within 12 weeks)
- Branded search volume ("maverick miller hvac" + misspellings) — leading indicator
- Click-through rate on local pack impressions
