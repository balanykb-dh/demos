"""Візуальні теми для ніш. Кожна тема = кольори, шрифти, мотив і додатковий CSS."""
from urllib.parse import quote

GOLOS = "family=Golos+Text:wght@400;500;600"


def _svg_uri(svg: str) -> str:
    return "url(\"data:image/svg+xml," + quote(svg, safe="") + "\")"


# ---------- Шиномонтаж: асфальт, протектор, сигнальний бурштин ----------
_tread = ("<svg xmlns='http://www.w3.org/2000/svg' width='36' height='28'>"
          "<rect width='36' height='28' fill='#2B3035'/>"
          "<path d='M5 0h11l9 14-9 14H5l9-14z' fill='#3D444B'/></svg>")

ASPHALT = dict(
    key="asphalt",
    fonts_url=f"https://fonts.googleapis.com/css2?{GOLOS}&family=Oswald:wght@500;600;700&display=swap",
    display_font='"Oswald","Arial Narrow",sans-serif', h3_font="var(--body)",
    h_weight=600, h_tracking="0", h1_size="clamp(34px,8vw,62px)", h2_size="clamp(30px,4.6vw,44px)",
    brand_size="22px", cta_size="21px",
    bg="#EEEDE9", ink="#1C1F22", muted="#4D5358", line="#D9D7D1",
    primary="#F2B01E", primary_dark="#2B3035", on_primary="#1C1F22", on_primary_hover="#FFFFFF",
    deep="#2B3035", on_deep="#FFFFFF", on_deep_muted="#C9CDD1",
    soft="#F1EEE4", accent="#F2B01E", icon="#2B3035", star="#E0A10E", bullet="#F2B01E", radius="4px",
    wall_bg="#D9D7D1", wall_pad="6px", wall_gap="6px", tile_bg="#FFFFFF",
    band_bg="#2B3035", visit_bg="#EEEDE9",
    after_hero_html='<div class="tread" aria-hidden="true"></div>',
    extra_css=f"""
  .hero{{background:#EEEDE9}}
  .tread{{height:28px;background:{_svg_uri(_tread)} repeat-x;}}
  .tile{{border-top:5px solid var(--accent)}}
  .tile--cta{{border-top-color:var(--accent)}}
  .band{{background:{_svg_uri(_tread)} repeat;}}
  .band__in{{border-color:rgba(242,176,30,.5)}}
  .band .btn--light{{background:var(--accent);color:#1C1F22}}
  .band .btn--light:hover{{background:#FFC93F}}
  .why .why__list h3{{font-size:18px}}
  .hero__art svg{{width:300px;height:auto}}
  .tire{{transform-box:fill-box;transform-origin:center;animation:roll 1.4s cubic-bezier(.2,.8,.2,1) .2s both}}
  @keyframes roll{{from{{transform:translateX(260px) rotate(300deg);opacity:0}}to{{transform:none;opacity:1}}}}
  @media (prefers-reduced-motion:reduce){{.tire{{animation:none}}}}
""",
)

# ---------- Перетяжка меблів: стьобана оббивка, оксамит, гірчичний шов ----------
VELVET = dict(
    key="velvet",
    fonts_url=f"https://fonts.googleapis.com/css2?{GOLOS}&family=Rubik:wght@500;600;700&display=swap",
    display_font='"Rubik",system-ui,sans-serif', h3_font="var(--body)",
    h_weight=600, h_tracking="-0.01em", h1_size="clamp(28px,6.6vw,52px)", h2_size="clamp(24px,3.8vw,36px)",
    brand_size="20px", cta_size="18px",
    bg="#F6F5F3", ink="#26202A", muted="#5C5560", line="#E3DEE4",
    primary="#4A2C4F", primary_dark="#3A2140", on_primary="#FFFFFF", on_primary_hover="#FFFFFF",
    deep="#3A2140", on_deep="#FFFFFF", on_deep_muted="#E2D4E4",
    soft="#F2ECF3", accent="#C9962B", icon="#4A2C4F", star="#C9962B", bullet="#C9962B", radius="10px",
    wall_bg="transparent", wall_pad="0", wall_gap="12px", tile_bg="#FFFFFF",
    band_bg="#F6F5F3", visit_bg="#F6F5F3",
    after_hero_html="",
    extra_css="""
  .hero{background-color:#4A2C4F;
    background-image:
      radial-gradient(circle,rgba(20,8,24,.55) 0 3px,rgba(255,255,255,.10) 4px,transparent 6px),
      radial-gradient(circle,rgba(20,8,24,.55) 0 3px,rgba(255,255,255,.10) 4px,transparent 6px),
      linear-gradient(45deg,transparent calc(50% - 1px),rgba(0,0,0,.22) 50%,transparent calc(50% + 1px)),
      linear-gradient(-45deg,transparent calc(50% - 1px),rgba(0,0,0,.22) 50%,transparent calc(50% + 1px)),
      radial-gradient(circle at 50% 50%,rgba(255,255,255,.07),transparent 70%);
    background-size:64px 64px;background-position:0 0,32px 32px,32px 32px,32px 32px,32px 32px}
  .hero .slab{border-color:transparent;outline:2px dashed rgba(201,150,43,.8);outline-offset:-10px}
  .tile{border:2px solid var(--line)}
  .tile::after{content:"";position:absolute;inset:8px;border:1.5px dashed rgba(201,150,43,.55);border-radius:6px;pointer-events:none}
  .tile--cta{border-color:var(--deep)}
  .tile--cta::after{border-color:rgba(255,255,255,.35)}
  .band__in{outline:2px dashed rgba(201,150,43,.7);outline-offset:-10px}
  .ba{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:22px}
  .ba__frame{aspect-ratio:4/3;border:2px dashed rgba(255,255,255,.45);border-radius:8px;display:flex;flex-direction:column;justify-content:flex-end;padding:12px;background:rgba(255,255,255,.05)}
  .ba__frame b{font:600 16px/1.2 var(--display);color:#fff}
  .ba__frame span{font-size:13px;color:var(--on-deep-muted);margin-top:4px}
  .hero__art svg{width:280px;height:auto}
  .swatch{transform-box:view-box;transform-origin:140px 300px;transform:rotate(var(--r));animation:fan 1.1s cubic-bezier(.2,.8,.2,1) .3s both}
  @keyframes fan{from{transform:rotate(0deg)}}
  @media (prefers-reduced-motion:reduce){.swatch{animation:none}}
""",
)

# ---------- Ательє: сантиметрова стрічка, кравецький папір, синій костюмний ----------
TAPE = dict(
    key="tape",
    fonts_url=f"https://fonts.googleapis.com/css2?{GOLOS}&family=Cormorant+Garamond:wght@600;700&display=swap",
    display_font='"Cormorant Garamond",Georgia,serif', h3_font="var(--body)",
    h_weight=700, h_tracking="-0.005em", h1_size="clamp(36px,8.2vw,64px)", h2_size="clamp(31px,4.8vw,46px)",
    brand_size="25px", cta_size="23px",
    bg="#FAFAF8", ink="#1E1E24", muted="#55555F", line="#E3E2DE",
    primary="#22324D", primary_dark="#17233A", on_primary="#FFFFFF", on_primary_hover="#FFFFFF",
    deep="#22324D", on_deep="#FFFFFF", on_deep_muted="#CFD8E6",
    soft="#EEF1F6", accent="#F0C43A", icon="#22324D", star="#D9A514", bullet="#B23A2E", radius="3px",
    wall_bg="#E3E2DE", wall_pad="2px", wall_gap="2px", tile_bg="#FFFFFF",
    band_bg="#FAFAF8", visit_bg="#FAFAF8",
    after_hero_html='<div class="tape" aria-hidden="true"><div class="tape__roll">{TAPE_SVG}</div></div>',
    extra_css="""
  .hero{background-color:#FAFAF8;
    background-image:
      linear-gradient(rgba(34,50,77,.12) 1px,transparent 1px),
      linear-gradient(90deg,rgba(34,50,77,.12) 1px,transparent 1px),
      linear-gradient(rgba(34,50,77,.06) 1px,transparent 1px),
      linear-gradient(90deg,rgba(34,50,77,.06) 1px,transparent 1px);
    background-size:120px 120px,120px 120px,24px 24px,24px 24px}
  .tape{height:34px;overflow:hidden;background:#F0C43A;border-top:1px solid #D9AE22;border-bottom:1px solid #D9AE22}
  .tape__roll{transform-origin:left center;animation:unroll 1.2s cubic-bezier(.2,.8,.2,1) .2s both}
  .tape__roll svg{height:34px;width:auto}
  @keyframes unroll{from{transform:scaleX(0)}}
  .tile__name{font-size:16px}
  .band__in{border-color:var(--deep);position:relative;overflow:hidden}
  .band__in::before{content:"";position:absolute;left:0;right:0;top:0;height:6px;background:#F0C43A}
  .hero__art svg{width:300px;height:auto}
  .thread{stroke-dasharray:700;stroke-dashoffset:700;animation:sew 1.6s ease-out .3s forwards}
  @keyframes sew{to{stroke-dashoffset:0}}
  @media (prefers-reduced-motion:reduce){.tape__roll{animation:none}.thread{animation:none;stroke-dashoffset:0}}
""",
)


# ---------- Ветклініка: мʼятний, бірюзовий, корал, лапки й пульс ----------
_paw = ("<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'>"
        "<g fill='#1F6F68' fill-opacity='.07' transform='rotate(-18 30 30)'>"
        "<ellipse cx='30' cy='36' rx='10' ry='8'/><ellipse cx='19' cy='25' rx='3.6' ry='4.6'/><ellipse cx='26' cy='20' rx='3.6' ry='4.6'/>"
        "<ellipse cx='34' cy='20' rx='3.6' ry='4.6'/><ellipse cx='41' cy='25' rx='3.6' ry='4.6'/></g>"
        "<g fill='#1F6F68' fill-opacity='.07' transform='rotate(16 90 90)'>"
        "<ellipse cx='90' cy='96' rx='10' ry='8'/><ellipse cx='79' cy='85' rx='3.6' ry='4.6'/><ellipse cx='86' cy='80' rx='3.6' ry='4.6'/>"
        "<ellipse cx='94' cy='80' rx='3.6' ry='4.6'/><ellipse cx='101' cy='85' rx='3.6' ry='4.6'/></g></svg>")

CLINIC = dict(
    key="clinic",
    fonts_url=f"https://fonts.googleapis.com/css2?{GOLOS}&family=Nunito:wght@700;800&display=swap",
    display_font='"Nunito",system-ui,sans-serif', h3_font="var(--body)",
    h_weight=800, h_tracking="-0.01em", h1_size="clamp(32px,7.4vw,58px)", h2_size="clamp(27px,4.2vw,40px)",
    brand_size="21px", cta_size="21px",
    bg="#F2F7F5", ink="#16302E", muted="#4C6461", line="#D8E6E2",
    primary="#1F6F68", primary_dark="#16524D", on_primary="#FFFFFF", on_primary_hover="#FFFFFF",
    deep="#16524D", on_deep="#FFFFFF", on_deep_muted="#CFE5E1",
    soft="#E6F2EF", accent="#F08A6C", icon="#1F6F68", star="#E9A23B", bullet="#F08A6C", radius="18px",
    wall_bg="transparent", wall_pad="0", wall_gap="12px", tile_bg="#FFFFFF",
    band_bg="#F2F7F5", visit_bg="#F2F7F5",
    after_hero_html=('<div class="pulse" aria-hidden="true"><svg viewBox="0 0 1200 56" preserveAspectRatio="none">'
                     '<path class="pulse__line" d="M0 30H520l14-10 12 10h18l10-24 14 46 12-40 10 18h22l12-8 12 8H1200"/></svg></div>'),
    extra_css=f"""
  .hero{{background-color:#EAF4F1;background-image:{_svg_uri(_paw)}}}
  .hero .slab{{border-color:transparent;box-shadow:0 14px 40px rgba(22,82,77,.13)}}
  .pulse{{height:56px;background:#16524D;overflow:hidden}}
  .pulse svg{{width:100%;height:56px}}
  .pulse__line{{fill:none;stroke:#F08A6C;stroke-width:3;stroke-linejoin:round;stroke-linecap:round;vector-effect:non-scaling-stroke;stroke-dasharray:1500;stroke-dashoffset:1500;animation:draw 1.8s ease-out .2s forwards}}
  @keyframes draw{{to{{stroke-dashoffset:0}}}}
  .tile{{border:2px solid var(--line)}}
  .tile svg{{width:54px;height:54px;padding:9px;border-radius:50%;background:var(--soft)}}
  .tile--cta{{border-color:var(--deep)}}
  .tile--cta svg{{width:22px;height:22px;padding:0;background:none}}
  @media (min-width:640px){{ .tile svg{{width:62px;height:62px;padding:11px}} .tile--cta svg{{width:22px;height:22px;padding:0}} }}
  .band__in{{border-radius:24px;border-color:transparent;box-shadow:inset 0 0 0 2px rgba(240,138,108,.35)}}
  .why__list li::before{{border-radius:50%}}
  .hero__art svg{{width:300px;height:auto}}
  .pop{{transform-box:fill-box;transform-origin:center;animation:pop .55s cubic-bezier(.3,1.6,.5,1) both;animation-delay:var(--d,0s)}}
  @keyframes pop{{from{{transform:scale(0)}}}}
  .beat{{transform-box:fill-box;transform-origin:center;animation:beat 1.8s ease-in-out 1.6s infinite}}
  @keyframes beat{{0%,60%,100%{{transform:scale(1)}}15%{{transform:scale(1.22)}}30%{{transform:scale(1)}}45%{{transform:scale(1.12)}}}}
  @media (prefers-reduced-motion:reduce){{.pulse__line{{animation:none;stroke-dashoffset:0}}.pop,.beat{{animation:none}}}}
""",
)

# ---------- Ремонт квартир: теплий тиньк, теракота, паркет «ялинка», план квартири ----------
WARM = dict(
    key="warm",
    fonts_url=f"https://fonts.googleapis.com/css2?{GOLOS}&family=Jost:wght@500;600&display=swap",
    display_font='"Jost",system-ui,sans-serif', h3_font="var(--body)",
    h_weight=600, h_tracking="-0.01em", h1_size="clamp(34px,7.8vw,62px)", h2_size="clamp(28px,4.4vw,42px)",
    brand_size="22px", cta_size="22px",
    bg="#F5F0E9", ink="#221D1A", muted="#5E554E", line="#E2D8CC",
    primary="#B4532A", primary_dark="#8C3D1C", on_primary="#FFFFFF", on_primary_hover="#FFFFFF",
    deep="#2B2420", on_deep="#FFFFFF", on_deep_muted="#D9CCBF",
    soft="#F3E7DC", accent="#D9894B", icon="#8C3D1C", star="#D99A2B", bullet="#B4532A", radius="6px",
    wall_bg="#E2D8CC", wall_pad="2px", wall_gap="2px", tile_bg="#FFFFFF",
    band_bg="#F5F0E9", visit_bg="#F5F0E9",
    after_hero_html='<div class="parquet" aria-hidden="true"></div>',
    extra_css="""
  .hero{background-color:#F5F0E9;background-image:radial-gradient(rgba(140,61,28,.17) 1.2px,transparent 1.7px);background-size:22px 22px}
  .parquet{height:30px;background-color:#CF935F;border-top:1px solid #9E6236;border-bottom:1px solid #9E6236;
    background-image:linear-gradient(135deg,#B9784A 25%,transparent 25%),linear-gradient(225deg,#B9784A 25%,transparent 25%),
      linear-gradient(315deg,#DDA674 25%,transparent 25%),linear-gradient(45deg,#DDA674 25%,transparent 25%);
    background-size:30px 30px;background-position:-15px 0,-15px 0,0 0,0 0}
  .tile::before{content:"";position:absolute;top:12px;right:12px;width:14px;height:14px;border-top:2px solid var(--accent);border-right:2px solid var(--accent)}
  .tile--cta::before{border-color:rgba(255,255,255,.4)}
  .band__in{border-color:transparent}
  .stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:22px}
  .stat{border:2px solid rgba(255,255,255,.18);border-radius:6px;padding:12px 10px}
  .stat b{display:block;font:600 26px/1 var(--display);color:#fff}
  .stat span{display:block;margin-top:6px;font-size:13.5px;line-height:1.3;color:var(--on-deep-muted)}
  @media (min-width:640px){ .stat{padding:16px} .stat b{font-size:32px} }
  .hero__art svg{width:320px;height:auto}
  .plan-wall{stroke-dasharray:1300;stroke-dashoffset:1300;animation:draw 1.7s ease-out .2s forwards}
  .plan-room{opacity:0;animation:warm .9s ease-out forwards;animation-delay:var(--d,1.6s)}
  @keyframes draw{to{stroke-dashoffset:0}}
  @keyframes warm{to{opacity:1}}
  @media (prefers-reduced-motion:reduce){.plan-wall{animation:none;stroke-dashoffset:0}.plan-room{animation:none;opacity:1}}
""",
)

# ---------- LEV: той самий асфальт, але сигнальний помаранчевий ----------
LEV_ORANGE = "#EF6A2E"
ASPHALT_LEV = dict(
    ASPHALT, key="asphalt_lev", primary=LEV_ORANGE, accent=LEV_ORANGE, bullet=LEV_ORANGE,
    extra_css=ASPHALT["extra_css"].replace("rgba(242,176,30,.5)", "rgba(239,106,46,.5)").replace("#FFC93F", "#FF8650"),
)


def tape_svg(cm: int = 200, px_per_cm: int = 12) -> str:
    w = cm * px_per_cm
    parts = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} 34' width='{w}' height='34'>"]
    for mm in range(cm * 10 + 1):
        x = mm * px_per_cm / 10
        if mm % 10 == 0:
            h = 14
        elif mm % 5 == 0:
            h = 9
        else:
            continue
        parts.append(f"<rect x='{x:.1f}' y='0' width='1.2' height='{h}' fill='#1E1E24'/>")
    for c in range(1, cm):
        x = c * px_per_cm
        if c % 2 == 0:
            parts.append(f"<text x='{x}' y='29' font-family='Arial,sans-serif' font-size='10' text-anchor='middle' fill='#1E1E24'>{c}</text>")
    parts.append("</svg>")
    return "".join(parts)


THEMES = {"asphalt": ASPHALT, "velvet": VELVET, "tape": TAPE, "clinic": CLINIC, "warm": WARM, "asphalt_lev": ASPHALT_LEV}
