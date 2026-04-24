#!/usr/bin/env python3
"""Generate remaining service and city pages from template + content data."""
import os, re, json

TEMPLATE = open("_template.html").read()

def svc_body(s):
    """Build service page body."""
    aside = f"""
      <aside class="sidebar">
        <div class="side-card">
          <h4>Fast response</h4>
          <p>{s['aside_line']}</p>
          <a href="tel:+14197776061" class="btn-r">Call (419) 777-6061</a>
        </div>
        <div class="side-card">
          <h4>We serve</h4>
          <ul>
            <li><a href="/hvac-perrysburg-oh">{s['short']} in Perrysburg</a></li>
            <li><a href="/hvac-sylvania-oh">{s['short']} in Sylvania</a></li>
            <li><a href="/hvac-whitehouse-oh">{s['short']} in Whitehouse</a></li>
            <li><a href="/hvac-waterville-oh">{s['short']} in Waterville</a></li>
            <li><a href="/hvac-bowling-green-oh">{s['short']} in Bowling Green</a></li>
            <li><a href="/service-area">Full service area &rarr;</a></li>
          </ul>
        </div>
        <div class="side-card">
          <h4>Related services</h4>
          <ul>
            {''.join(f'<li><a href="/{r[0]}">{r[1]}</a></li>' for r in s['related'])}
          </ul>
        </div>
      </aside>"""

    price_html = ""
    if s.get("price_ranges"):
        items = "\n            ".join(
            f'<li><span>{label}</span><strong>{val}</strong></li>' for label, val in s["price_ranges"]
        )
        price_html = f"""
        <h2>{s['price_h2']}</h2>
        <p>{s['price_intro']}</p>
        <div class="price-range">
          <h4>{s['price_title']}</h4>
          <ul class="price-range-list">
            {items}
          </ul>
          <p class="price-range-foot">{s['price_foot']}</p>
        </div>"""

    faq_html = ""
    if s.get("faqs"):
        faq_items = "\n          ".join(
            f'<details>\n            <summary>{q}</summary>\n            <p>{a}</p>\n          </details>'
            for q, a in s["faqs"]
        )
        faq_html = f"""
        <h2>Frequently asked</h2>
        <div class="faq">
          {faq_items}
        </div>"""

    steps_html = ""
    if s.get("steps"):
        step_items = "\n          ".join(
            f'<div class="step"><div class="step-num">Step 0{i+1}</div><h4>{t}</h4><p>{d}</p></div>'
            for i, (t, d) in enumerate(s["steps"])
        )
        steps_html = f"""
        <h2>Our process</h2>
        <div class="steps">
          {step_items}
        </div>"""

    body_inner = f"""{s['prose_top']}

        <div class="cta-inline">
          <p><strong>{s['cta_inline_bold']}</strong> {s['cta_inline_text']}</p>
          <a href="tel:+14197776061">Call now &rarr;</a>
        </div>
{steps_html}
{price_html}
{s.get('prose_mid','')}
{faq_html}"""

    return f"""
    <section class="page-hero">
      <div class="page-hero-img"><img src="images/{s['hero_img']}" alt=""></div>
      <div class="page-hero-inner">
        <div class="page-hero-tag">{s['tag']}</div>
        <h1>{s['h1']}</h1>
        <p class="page-hero-p">{s['hero_p']}</p>
      </div>
    </section>

    <div class="split">
      <div class="prose">
{body_inner}
      </div>
{aside}
    </div>"""


def svc_schema(s):
    faq_entities = ",".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}'
        % (json.dumps(q), json.dumps(a)) for q, a in s.get("faqs", [])
    )
    faq_block = ""
    if faq_entities:
        faq_block = f"""
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_entities}]}}
  </script>"""
    areas = """[
      {"@type":"City","name":"Toledo","addressRegion":"OH"},
      {"@type":"City","name":"Perrysburg","addressRegion":"OH"},
      {"@type":"City","name":"Sylvania","addressRegion":"OH"},
      {"@type":"City","name":"Bowling Green","addressRegion":"OH"},
      {"@type":"City","name":"Whitehouse","addressRegion":"OH"},
      {"@type":"City","name":"Waterville","addressRegion":"OH"}
    ]"""
    svc_schema_str = f"""
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Service","name":{json.dumps(s['svc_name'])},"serviceType":"HVAC","provider":{{"@id":"https://maverickandmillerhvac.com/#business"}},"areaServed":{areas},"description":{json.dumps(s['svc_desc'])}}}
  </script>"""
    breadcrumb = f"""
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {{"@type":"ListItem","position":1,"name":"Home","item":"https://maverickandmillerhvac.com/"}},
    {{"@type":"ListItem","position":2,"name":"Services","item":"https://maverickandmillerhvac.com/services"}},
    {{"@type":"ListItem","position":3,"name":{json.dumps(s['bc_name'])},"item":"https://maverickandmillerhvac.com/{s['slug']}"}}
  ]}}
  </script>"""
    return svc_schema_str + faq_block + breadcrumb


def svc_breadcrumb(s):
    return f"""
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a>
      <span class="breadcrumb-sep">/</span>
      <a href="/services">Services</a>
      <span class="breadcrumb-sep">/</span>
      <span aria-current="page">{s['bc_name']}</span>
    </nav>"""


def city_body(c):
    """City page body."""
    meta_html = f"""
        <div class="city-meta">
          <div class="city-meta-item"><strong>{c['drive_min']} min</strong><span>from our Toledo shop</span></div>
          <div class="city-meta-item"><strong>{c['zip']}</strong><span>ZIP code</span></div>
          <div class="city-meta-item"><strong>{c['population']}</strong><span>Residents</span></div>
          <div class="city-meta-item"><strong>{c['housing_age']}</strong><span>Typical build era</span></div>
        </div>"""

    svc_grid_items = "\n            ".join(
        f'<a href="/{s_slug}" class="city-card"><h3>{s_name}</h3><p>{s_desc}</p><span class="link">{s_name} in {c["name"]} &rarr;</span></a>'
        for s_slug, s_name, s_desc in c["services_grid"]
    )

    faq_items = "\n          ".join(
        f'<details>\n            <summary>{q}</summary>\n            <p>{a}</p>\n          </details>'
        for q, a in c["faqs"]
    )

    return f"""
    <section class="page-hero">
      <div class="page-hero-img"><img src="images/hero-bg.webp" alt=""></div>
      <div class="page-hero-inner">
        <div class="page-hero-tag">HVAC in {c['name']}, OH</div>
        <h1>{c['h1']}</h1>
        <p class="page-hero-p">{c['hero_p']}</p>
      </div>
    </section>

    <div class="prose-wrap">
      <div style="max-width:1120px">
{meta_html}
      </div>
    </div>

    <div class="split" style="padding-top:0">
      <div class="prose">
        <h2>{c['about_h2']}</h2>
        {c['about_body']}

        <h2>Services in {c['name']}</h2>
        <p>Full HVAC service for {c['name']} homes. Pick a service for details and pricing.</p>

        <div class="svc-index" style="margin-top:24px">
            {svc_grid_items}
        </div>

        <h2>Common {c['name']} HVAC questions</h2>
        <div class="faq">
          {faq_items}
        </div>
      </div>

      <aside class="sidebar">
        <div class="side-card">
          <h4>Fast to {c['name']}</h4>
          <p>Our shop is {c['drive_min']} minutes away at 7628 Trotter Road. Same-day service often available.</p>
          <a href="tel:+14197776061" class="btn-r">Call (419) 777-6061</a>
        </div>
        <div class="side-card">
          <h4>{c['name']} neighborhoods we cover</h4>
          <ul>
            {''.join(f'<li>{n}</li>' for n in c['neighborhoods'])}
          </ul>
        </div>
        <div class="side-card">
          <h4>Also nearby</h4>
          <ul>
            {''.join(f'<li><a href="/{n_slug}">{n_name}</a></li>' for n_slug, n_name in c['nearby'])}
            <li><a href="/service-area">Full service area &rarr;</a></li>
          </ul>
        </div>
      </aside>
    </div>"""


def city_schema(c):
    faq_entities = ",".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}'
        % (json.dumps(q), json.dumps(a)) for q, a in c["faqs"]
    )
    biz = f"""
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"HVACBusiness","@id":"https://maverickandmillerhvac.com/#business","name":"Maverick & Miller HVAC","url":"https://maverickandmillerhvac.com/","telephone":"+1-419-777-6061","address":{{"@type":"PostalAddress","streetAddress":"7628 Trotter Road","addressLocality":"Toledo","addressRegion":"OH","postalCode":"43617","addressCountry":"US"}},"areaServed":{{"@type":"City","name":{json.dumps(c['name'])},"addressRegion":"OH"}}}}
  </script>"""
    faq = f"""
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_entities}]}}
  </script>"""
    breadcrumb = f"""
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {{"@type":"ListItem","position":1,"name":"Home","item":"https://maverickandmillerhvac.com/"}},
    {{"@type":"ListItem","position":2,"name":"Service Area","item":"https://maverickandmillerhvac.com/service-area"}},
    {{"@type":"ListItem","position":3,"name":{json.dumps(c['name'])},"item":"https://maverickandmillerhvac.com/{c['slug']}"}}
  ]}}
  </script>"""
    return biz + faq + breadcrumb


def city_breadcrumb(c):
    return f"""
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a>
      <span class="breadcrumb-sep">/</span>
      <a href="/service-area">Service Area</a>
      <span class="breadcrumb-sep">/</span>
      <span aria-current="page">{c['name']}</span>
    </nav>"""


def render(page):
    body = page["body_fn"](page)
    schema = page["schema_fn"](page)
    bc = page["bc_fn"](page)
    html = TEMPLATE
    html = html.replace("{{TITLE}}", page["title"])
    html = html.replace("{{META_DESC}}", page["meta_desc"])
    html = html.replace("{{SLUG}}", page["slug"])
    html = html.replace("{{OG_TITLE}}", page.get("og_title", page["title"]))
    html = html.replace("{{OG_DESC}}", page.get("og_desc", page["meta_desc"]))
    html = html.replace("{{HERO_IMG}}", page.get("hero_img", "hero-bg.webp"))
    html = html.replace("{{SCHEMA}}", schema)
    html = html.replace("{{BREADCRUMB}}", bc)
    html = html.replace("{{BODY}}", body)
    html = html.replace("{{CTA_H2}}", page["cta_h2"])
    html = html.replace("{{CTA_P}}", page["cta_p"])
    return html


# === Import content definitions ===
from _content import SERVICE_PAGES, CITY_PAGES

for p in SERVICE_PAGES:
    p["body_fn"] = svc_body
    p["schema_fn"] = svc_schema
    p["bc_fn"] = svc_breadcrumb
    out = render(p)
    with open(f"{p['slug']}.html", "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    print(f"Wrote {p['slug']}.html ({len(out)} bytes)")

for p in CITY_PAGES:
    p["body_fn"] = city_body
    p["schema_fn"] = city_schema
    p["bc_fn"] = city_breadcrumb
    out = render(p)
    with open(f"{p['slug']}.html", "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    print(f"Wrote {p['slug']}.html ({len(out)} bytes)")
