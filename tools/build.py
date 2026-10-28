"""Збирає демо-сайти з tools/sites.py у папки <slug>/index.html + og-image.png.

Запуск з кореня репозиторію:  python3 tools/build.py [slug ...]
OG-картинки рендеряться через Playwright (локальні шрифти)."""
import json
import sys
from pathlib import Path
from urllib.parse import quote

from jinja2 import Environment, FileSystemLoader, select_autoescape

sys.path.insert(0, str(Path(__file__).parent))
from sites import SITES  # noqa: E402
from themes import THEMES, tape_svg  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://balanykb-dh.github.io/demos/"
DAY_LABELS = {1: "Понеділок", 2: "Вівторок", 3: "Середа", 4: "Четвер", 5: "Пʼятниця", 6: "Субота", 0: "Неділя"}
SCHEMA_DAYS = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 0: "Sunday"}

ICONS = dict(
    phone='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
    chat='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg>',
)


def hours_model(h):
    """-> (rows, hours_json, always_open, schema_spec)"""
    if h == "24/7":
        rows = [dict(day=None, label="Щодня", value="цілодобово")]
        spec = [{"@type": "OpeningHoursSpecification", "dayOfWeek": list(SCHEMA_DAYS.values()), "opens": "00:00", "closes": "23:59"}]
        return rows, {d: [0, 24] for d in range(7)}, True, spec
    vals = {d: h.get(d) for d in range(7)}
    if len({vals[d] for d in range(7)}) == 1 and vals[0]:
        o, c = vals[0]
        rows = [dict(day=None, label="Щодня", value=f"{o}:00–{c}:00")]
    else:
        rows = [dict(day=d, label=DAY_LABELS[d], value=(f"{vals[d][0]}:00–{vals[d][1]}:00" if vals[d] else "вихідний"))
                for d in (1, 2, 3, 4, 5, 6, 0)]
    spec = []
    for d in (1, 2, 3, 4, 5, 6, 0):
        if vals[d]:
            spec.append({"@type": "OpeningHoursSpecification", "dayOfWeek": SCHEMA_DAYS[d],
                         "opens": f"{vals[d][0]:02d}:00", "closes": f"{vals[d][1]:02d}:00"})
    return rows, {d: (list(vals[d]) if vals[d] else None) for d in range(7)}, False, spec


def render(site, env):
    t = dict(THEMES[site["theme"]])
    t["after_hero_html"] = t["after_hero_html"].replace("{TAPE_SVG}", tape_svg())
    rows, hours_json, always, spec = hours_model(site["hours"])
    n = len(site["tiles"])
    lat, lng = site["geo"]
    schema = {
        "@context": "https://schema.org", "@type": site["schema_type"], "name": site["name"],
        "telephone": site["phone_e164"],
        "address": {"@type": "PostalAddress", "streetAddress": site["street"], "addressLocality": site["locality"],
                    "postalCode": site["postal"], "addressCountry": "UA"},
        "geo": {"@type": "GeoCoordinates", "latitude": lat, "longitude": lng},
        "openingHoursSpecification": spec,
    }
    ctx = dict(
        s=site, t=t, icons=ICONS, base_url=BASE_URL,
        schema=json.dumps(schema, ensure_ascii=False, indent=1).replace("</", "<\\/"),
        hours_rows=rows, hours_json=json.dumps(hours_json), always_open=always,
        cta_span_mobile=2 if n % 2 == 0 else 1,
        cta_span_desktop=3 if n % 3 == 0 else 3 - n % 3,
        maps_place_url=f"https://www.google.com/maps/search/?api=1&query={quote(site['name'] + ', ' + site['street'])}&query_place_id={site['place_id']}",
        maps_dir_url=f"https://www.google.com/maps/dir/?api=1&destination={lat},{lng}&destination_place_id={site['place_id']}",
        maps_embed_url=f"https://www.google.com/maps?q={lat},{lng}&z=16&output=embed",
    )
    return env.get_template("template.html.j2").render(**ctx)


OG_HTML = """<!doctype html><html lang="uk"><head><meta charset="utf-8"><style>
*{{box-sizing:border-box;margin:0}}
body{{width:1200px;height:630px;font-family:"Inter Display","Inter",sans-serif;color:{ink};background:{deep};position:relative;overflow:hidden}}
.slab{{position:absolute;left:0;top:0;width:800px;height:630px;background:#fff;padding:60px 64px;display:flex;flex-direction:column}}
.brand{{display:flex;align-items:center;gap:16px}} .brand svg{{width:52px;height:52px}}
.brand b{{font-weight:800;font-size:32px;color:{primary_dark}}}
h1{{margin-top:34px;font-weight:800;font-size:60px;line-height:1.05;letter-spacing:-.5px}}
.addr{{margin-top:22px;font-size:26px;color:{muted}}}
.bottom{{margin-top:auto;display:flex;align-items:center;justify-content:space-between}}
.rating{{font-size:24px;color:{muted}}} .rating span{{color:{star};letter-spacing:3px;margin-right:10px}} .rating strong{{color:{ink}}}
.demo{{font-size:20px;font-weight:600;color:{primary_dark};background:{soft};border-radius:6px;padding:8px 14px}}
.art{{position:absolute;right:30px;top:120px;width:340px;height:390px;display:flex;align-items:center;justify-content:center}}
.art svg{{width:340px;height:auto}}
</style></head><body>
<div class="slab">
  <div class="brand">{logo}<b>{name}</b></div>
  <h1>{h1}</h1>
  <p class="addr">{address}</p>
  <div class="bottom"><p class="rating"><span>★★★★★</span><strong>{rating}</strong> у Google, {reviews}</p><p class="demo">Демо сайту</p></div>
</div>
<div class="art">{art}</div>
</body></html>"""


def render_og(site, out_png: Path):
    from playwright.sync_api import sync_playwright
    t = THEMES[site["theme"]]
    html = OG_HTML.format(ink=t["ink"], deep=t["deep"], primary_dark=t["primary_dark"], muted=t["muted"], star=t["star"],
                          soft=t["soft"], logo=site["logo_svg"], name=site["name"], h1=site["h1"],
                          address=site["address_display"], rating=site["rating_text"], reviews=site["reviews_text"],
                          art=site["hero_svg"].replace('class="', 'data-c="'))
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        pg.set_content(html)
        pg.wait_for_timeout(300)
        pg.screenshot(path=str(out_png))
        b.close()


ROOT_INDEX = """<!doctype html><html lang="uk"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Демо</title></head>
<body style="font-family:system-ui,sans-serif;padding:40px;color:#333">Тут немає публічного змісту.</body></html>
"""


def main(only):
    env = Environment(loader=FileSystemLoader(str(Path(__file__).parent)), autoescape=select_autoescape(["html", "j2"]))
    (ROOT / ".nojekyll").write_text("")
    (ROOT / "index.html").write_text(ROOT_INDEX, encoding="utf-8")
    for site in SITES:
        if only and site["slug"] not in only:
            continue
        d = ROOT / site["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(render(site, env), encoding="utf-8")
        render_og(site, d / "og-image.png")
        print("built", site["slug"])


if __name__ == "__main__":
    main(set(sys.argv[1:]))
