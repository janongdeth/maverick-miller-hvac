# Programmatic SEO Plan — Future City × Service Scaling

## This build: 5 city pages manually built

We're NOT doing programmatic generation in this build. 5 city pages × 7 services = 35 service-city combinations exist in theory, but publishing 35 pages at launch triggers:
- Scaled Content Abuse policy risk (Google March 2024, enforced Jun 2025, Aug 2025)
- Thin content penalty (<40% unique content between pages)
- Quality-gate HARD STOP at 30% uniqueness (seo-programmatic)

## Future scaling option (after v1 ships)

Once the 5 core city pages prove they rank, programmatic expansion path:

### Tier 2 (12 cities × 7 services = 84 pages max, but only ~30 worth building)

Only build city-service combos where:
1. Search volume exists (not every combo does — "commercial hvac elmore oh" has zero demand)
2. Maverick actively wants the business (not every service in every city)
3. We can write ≥40% unique content per page

Estimated viable Tier 2 combos:
| City | Likely services with demand |
|---|---|
| Toledo | All 7 (home base) |
| Perrysburg | AC, furnace, maintenance, water heater, mini-split |
| Sylvania | AC, furnace, maintenance, water heater |
| Bowling Green | AC, furnace, maintenance |
| Whitehouse | AC, furnace, maintenance |
| Waterville | AC, furnace, maintenance |
| Oregon | AC, furnace |
| Northwood | AC, furnace |
| Port Clinton | AC, furnace, water heater |
| Point Place, Elmore, Woodville | skip — demand too thin |

Rough Tier 2 target: ~25-30 pages added progressively.

### Template design (for future)

URL pattern: `/[service]-[city]-oh` (e.g., `/ac-repair-perrysburg-oh`)

Unique content sources per page (must hit ≥40%):
1. City + housing stock context (2-3 sentences, unique per combo)
2. Specific neighborhoods/subdivisions in city (pulled from a data file)
3. Local response time from Toledo HQ (minutes, unique per city)
4. Sample recent job description for this service in this city (ghost-written placeholder until real)
5. City-specific FAQ (2-3 Qs, unique per combo)
6. Service-specific benefit that matches city demographics
7. Local trust signal (neighbor testimonial, chamber membership, etc.)

Shared (static) content:
- Service technical details
- Safety / warranty language
- CTA blocks
- Header / footer

### Quality gates (enforce before launch)

Per seo-programmatic guidance:
- [ ] Publish in batches of 5-10 pages, not all 30 at once
- [ ] Monitor GSC for 2-4 weeks between batches
- [ ] Human review ≥10% of generated pages
- [ ] Every page passes "would this be worth publishing even if no others existed?" test
- [ ] Unique content ≥40% between any two pages (diff check)

### Data file structure (for future template engine)

```json
{
  "cities": [
    {
      "slug": "perrysburg-oh",
      "name": "Perrysburg",
      "neighborhoods": ["Levis Commons", "Three Meadows", "Ford Street Historic District"],
      "drive_time_min": 15,
      "median_income": 95000,
      "housing_notes": "Mix of 1920s-era historic homes and newer subdivisions",
      "common_systems": "Older homes often have boilers or original ductwork; newer builds have modern split systems"
    }
  ],
  "services": [
    {
      "slug": "ac-repair",
      "name": "AC Repair",
      "technical_depth": "...",
      "typical_issues": "..."
    }
  ]
}
```

## Not doing in this build

- No template engine / static-site generator (vanilla HTML, hand-authored)
- No programmatic generation script
- No Tier 2 pages

## Doing in this build

- 5 hand-written city pages (Perrysburg, Sylvania, Whitehouse, Waterville, Bowling Green)
- Each gets 100% unique content, no shared city blocks
- This sets quality bar for future programmatic expansion

## When to revisit

- After GSC shows 3+ months of data
- After client confirms v1 is driving leads
- After at least 5 real Google reviews (so AggregateRating schema unlocks)
- Then: generate data file, build template, ship Tier 2 in batches
