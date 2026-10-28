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


THEMES = {"asphalt": ASPHALT, "velvet": VELVET, "tape": TAPE}
