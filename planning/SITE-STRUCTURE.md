# Site Structure — Maverick & Miller HVAC

## URL Map (18 pages, flat)

### Core pages
| URL | Purpose | H1 direction |
|---|---|---|
| `/` | Conversion landing | Primary Toledo HVAC value prop |
| `/about` | Founders, trust, story | About Maverick & Miller HVAC |
| `/services` | Service hub, links to all 7 service pages | Heating, Cooling, and Water Heater Services in Toledo |
| `/service-area` | Coverage map, links to 5 city pages | Service Area — Northwest Ohio |
| `/reviews` | Testimonials wall | What Our Customers Say |
| `/contact` | Phone/email CTAs, map, hours | Get in Touch |

### Service pages (7)
| URL | Primary service |
|---|---|
| `/ac-repair` | AC repair + install |
| `/furnace-repair` | Furnace repair + install |
| `/water-heater-installation` | Water heater install |
| `/ductless-mini-splits` | Mini-split install + service |
| `/air-filtration` | IAQ, filtration, purification |
| `/hvac-maintenance` | Tune-ups, seasonal service |
| `/commercial-hvac` | Commercial installs + service |

### City pages (5)
| URL | City |
|---|---|
| `/hvac-perrysburg-oh` | Perrysburg |
| `/hvac-sylvania-oh` | Sylvania |
| `/hvac-whitehouse-oh` | Whitehouse |
| `/hvac-waterville-oh` | Waterville |
| `/hvac-bowling-green-oh` | Bowling Green |

## Internal Linking Graph

### Hub/spoke model
```
             HOME (/)
               │
      ┌────────┼─────────────┐
      ▼        ▼             ▼
 /services   /service-area  /about, /reviews, /contact
      │              │
   7 service     5 city pages
    pages        (each links down to relevant services)
```

### Required links per page
| From | Links to |
|---|---|
| `/` | All 6 core + top 3 services + top 3 cities |
| `/services` | All 7 service pages + back to `/service-area` |
| `/service-area` | All 5 city pages + back to `/services` |
| Each service page | `/services`, 3 related services, top 3 cities, `/contact` |
| Each city page | `/service-area`, all 7 services (contextualized to city), `/contact` |
| `/about` | `/services`, `/contact` |
| `/reviews` | `/services`, `/contact` |
| `/contact` | `/services`, `/service-area` |

### Cross-linking rules (service × city)
- Each service page has a "Service area" section listing the 5 city pages (anchor: "AC repair in Perrysburg", etc.)
- Each city page has a "Services we provide in [city]" section listing all 7 service pages

This creates a square linking matrix (7 services × 5 cities = 35 internal link contexts) that Google reads as comprehensive local coverage.

## Nav / Footer (shared components)

### Header nav
```
[Logo] Home | About | Services ▾ | Service Area ▾ | Reviews | Contact  [📞 (419) 777-6061]
              └ AC Repair           └ Perrysburg
              └ Furnace Repair      └ Sylvania
              └ Water Heaters       └ Whitehouse
              └ Mini-Splits         └ Waterville
              └ Air Filtration      └ Bowling Green
              └ Maintenance
              └ Commercial
```

### Footer (4 columns)
1. **NAP + hours** — Name, phone, Toledo address, M-F 8-6
2. **Services** — 7 service page links
3. **Service Area** — 5 city page links + overview link
4. **Company** — About, Reviews, Contact + social if any

## Schema Plan

| Page | Schema types |
|---|---|
| `/` | HVACBusiness (primary) + BreadcrumbList |
| `/about` | Organization, Person (Shane, Kindle), BreadcrumbList |
| `/services` | HVACBusiness + OfferCatalog, BreadcrumbList |
| `/service-area` | HVACBusiness + areaServed array, BreadcrumbList |
| `/reviews` | Review aggregate (once real reviews in), BreadcrumbList |
| `/contact` | ContactPoint, BreadcrumbList |
| Each service page | Service schema + provider ref to HVACBusiness, BreadcrumbList, FAQPage (3-5 Qs) |
| Each city page | LocalBusiness with areaServed = city, BreadcrumbList, FAQPage (local Qs) |

## Anchor Redirects (old → new)

Current home page has `#services`, `#about`, `#areas`, `#reviews`, `#contact`. Update all `<a href="#x">` to absolute paths (`/services`, `/about`, etc.). Remove anchor fallbacks — the new pages are canonical.

## Quality Gates (against `seo-programmatic` guidance)

City pages risk thin-content penalty if they're near-duplicates. Each city page MUST contain ≥40% unique content. Uniqueness sources per city:
- 2-3 named neighborhoods / subdivisions / ZIP codes
- Housing stock notes (older vs newer builds, common system types)
- Travel time from Toledo 43617
- 1-2 local landmarks / recognizable streets for proximity signals
- City-specific FAQ (e.g., Perrysburg historic homes → mini-split retrofits)
- At least one city-specific stat or observation (avg home age, typical HVAC issues)

No mad-libs. No "Looking for HVAC in {city}? We're the best in {city}!"

## Sitemap structure

```
sitemap.xml
├── / (priority 1.0)
├── /services, /service-area (priority 0.9)
├── 7 service pages (priority 0.8)
├── 5 city pages (priority 0.8)
└── /about, /reviews, /contact (priority 0.7)
```

robots.txt allows all, references sitemap.
