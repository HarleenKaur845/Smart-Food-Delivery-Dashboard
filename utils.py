import uuid
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components


@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_swiggy.csv")


# =========================================================
# PALETTE
# =========================================================
ORANGE = "#FF6B35"
ORANGE2 = "#FF9142"
HOT = "#FF3B5C"
AMBER = "#FFC93C"
RUST = "#C9432E"
CREAM = "#FFF3E6"
CHART_PALETTE = [ORANGE, HOT, AMBER, ORANGE2, "#FF8C5A", "#C9432E"]

BACKDROPS = {
    "home": "https://images.unsplash.com/photo-1544025162-d76694265947?q=80&w=1600&auto=format&fit=crop",
    "data": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?q=80&w=1600&auto=format&fit=crop",
    "analysis": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=1600&auto=format&fit=crop",
    "insights": "https://images.unsplash.com/photo-1424847651672-bf20a4b0982b?q=80&w=1600&auto=format&fit=crop",
    "about": "https://images.unsplash.com/photo-1552566626-52f8b828add9?q=80&w=1600&auto=format&fit=crop",
}

# =========================================================
# ICONS — inline line-art SVGs, no emoji anywhere
# =========================================================
_ICON_PATHS = {
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>',
    "chart": '<line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line>',
    "trend-up": '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline>',
    "trend-down": '<polyline points="23 18 13.5 8.5 8.5 13.5 1 6"></polyline><polyline points="17 18 23 18 23 12"></polyline>',
    "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>',
    "truck": '<rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle>',
    "tag": '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line>',
    "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle>',
    "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path>',
    "target": '<circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>',
    "flag": '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"></path><line x1="4" y1="22" x2="4" y2="15"></line>',
    "clock": '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
    "search": '<circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line>',
    "pie": '<path d="M21.21 15.89A10 10 0 1 1 8 2.83"></path><path d="M22 12A10 10 0 0 0 12 2v10z"></path>',
    "layers": '<polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline>',
    "info": '<circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line>',
    "bulb": '<path d="M9 18h6"></path><path d="M10 22h4"></path><path d="M15.09 14c.18-1 .64-1.9 1.31-2.6A6 6 0 0 0 12 2a6 6 0 0 0-4.4 10.4c.67.7 1.13 1.6 1.31 2.6"></path>',
    "compass": '<circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon>',
    "sparkle": '<path d="M12 2 L14.2 9.3 L22 12 L14.2 14.7 L12 22 L9.8 14.7 L2 12 L9.8 9.3 Z"></path>',
    "grid": '<rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect>',
    "flame": '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.07-2.14-.22-4.05 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.15.43-2.29 1-3a2.5 2.5 0 0 0 2.5 2.5z"></path>',
    "cup": '<path d="M18 8h1a4 4 0 0 1 0 8h-1"></path><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path><line x1="6" y1="1" x2="6" y2="4"></line><line x1="10" y1="1" x2="10" y2="4"></line><line x1="14" y1="1" x2="14" y2="4"></line>',
    "pizza": '<path d="M12 2 L22 20 L2 20 Z"></path><circle cx="12" cy="12" r="1"></circle><circle cx="9" cy="15.5" r="1"></circle><circle cx="15" cy="15.5" r="1"></circle>',
    "utensils": '<path d="M3 2v7a2 2 0 0 0 2 2 2 2 0 0 0 2-2V2"></path><path d="M5 12v10"></path><path d="M19 2c-1.7 0-3 1.8-3 4v4c0 1.5 1 2 2 2h1v10"></path>',
}


def icon(name, color=ORANGE, size=24, stroke=1.8):
    path = _ICON_PATHS.get(name, _ICON_PATHS["star"])
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" '
            f'stroke-linejoin="round">{path}</svg>')


def icon_badge(name, color=ORANGE, size=24):
    return f'<div class="icon-badge">{icon(name, color, size)}</div>'


def _ambient_particles():
    """Faint floating food icons drifting in the background — pure CSS, no JS."""
    layout = [
        ("flame", 4, 12, 110, 17),
        ("pizza", 90, 8, 90, 21),
        ("cup", 6, 68, 80, 15),
        ("utensils", 92, 62, 100, 19),
        ("star", 48, 4, 46, 13),
        ("tag", 62, 88, 60, 18),
        ("sparkle", 20, 85, 50, 16),
    ]
    out = []
    for i, (name, left, top, size, dur) in enumerate(layout):
        out.append(
            f'<div class="ambient-icon" style="left:{left}%; top:{top}%; '
            f'animation-duration:{dur}s; animation-delay:{i * 1.1}s;">'
            f'{icon(name, ORANGE, size, stroke=1.2)}</div>'
        )
    return "".join(out)


# =========================================================
# THEME
# =========================================================
def apply_theme(page="home"):
    bg = BACKDROPS.get(page, BACKDROPS["home"])

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    :root {{
        --orange: {ORANGE};
        --orange2: {ORANGE2};
        --hot: {HOT};
        --amber: {AMBER};
        --cream: {CREAM};
        --glass: rgba(18, 12, 8, 0.62);
        --glass-hover: rgba(32, 20, 12, 0.82);
        --hairline: rgba(255, 107, 53, 0.30);
    }}

    [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"], .stApp, .stMain {{
        background: transparent !important;
    }}

    html, body {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background:
            radial-gradient(ellipse at 20% 0%, rgba(255,107,53,0.14) 0%, transparent 55%),
            radial-gradient(ellipse at 90% 90%, rgba(255,59,92,0.10) 0%, transparent 55%),
            linear-gradient(180deg, rgba(5, 3, 2, 0.40) 0%, rgba(5, 3, 2, 0.55) 50%, rgba(5, 3, 2, 0.75) 100%),
            url("{bg}") !important;
        background-size: cover !important;
        background-position: center center !important;
        background-attachment: fixed !important;
        background-repeat: no-repeat !important;
    }}

    [data-testid="stHeader"] {{ background-color: transparent !important; }}
    h1, h2, h3 {{ font-family: 'Sora', sans-serif; }}

    /* Force cards in the same row to match the tallest one */
    [data-testid="stHorizontalBlock"] {{ align-items: stretch !important; }}
    [data-testid="column"] {{ display: flex !important; flex-direction: column !important; }}
    [data-testid="column"] > div {{ height: 100%; }}
    [data-testid="column"] [data-testid="stVerticalBlock"] {{ height: 100%; }}

    /* Sidebar (the part outside the option_menu iframe) */
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child,
    [data-testid="stSidebarUserContent"], [data-testid="stSidebarContent"] {{
        background: linear-gradient(180deg, rgba(10,6,4,0.99), rgba(5,3,2,0.99)) !important;
    }}
    [data-testid="stSidebar"] {{
        border-right: 1px solid var(--hairline) !important;
        box-shadow: 6px 0 30px rgba(255,107,53,0.06);
    }}
    [data-testid="stSidebar"]::before {{
        content: ""; position: absolute; top: 0; left: 0; right: 0; height: 3px;
        background: linear-gradient(90deg, var(--orange), var(--hot), var(--amber), var(--orange));
        background-size: 300% auto; animation: shimmer 6s linear infinite;
    }}
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {{ color: var(--cream) !important; }}
    [data-testid="stSidebarNav"] {{ display: none !important; }}

    /* Floating ambient food icons */
    .ambient-icon {{ position: fixed; opacity: .07; z-index: -1; pointer-events: none; animation-name: floatIcon; animation-timing-function: ease-in-out; animation-iteration-count: infinite; }}
    @keyframes floatIcon {{ 0%, 100% {{ transform: translateY(0) rotate(0deg); }} 50% {{ transform: translateY(-34px) rotate(14deg); }} }}
    .blob1 {{ position: fixed; width: 380px; height: 380px; background: var(--orange); filter: blur(160px); top: 4%; left: 0%; opacity: .16; z-index: -1; animation: pulseBlob 9s ease-in-out infinite; }}
    .blob2 {{ position: fixed; width: 380px; height: 380px; background: var(--hot); filter: blur(160px); bottom: 4%; right: 0%; opacity: .13; z-index: -1; animation: pulseBlob 11s ease-in-out infinite reverse; }}
    @keyframes pulseBlob {{ 0%, 100% {{ transform: scale(1); opacity: .13; }} 50% {{ transform: scale(1.25); opacity: .22; }} }}

    @keyframes fadeInUp {{ from {{ opacity: 0; transform: translateY(26px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    @keyframes shimmer {{ 0% {{ background-position: 0% 50%; }} 100% {{ background-position: 300% 50%; }} }}

    /* ---------- HERO ---------- */
    .hero {{
        position: relative;
        background: linear-gradient(135deg, rgba(255,107,53,0.14) 0%, rgba(255,59,92,0.10) 100%), var(--glass);
        backdrop-filter: blur(26px) saturate(170%);
        -webkit-backdrop-filter: blur(26px) saturate(170%);
        border: 1px solid var(--hairline);
        border-radius: 22px;
        padding: 48px 40px;
        margin-bottom: 38px;
        text-align: center;
        animation: fadeInUp .7s ease both, heroGlow 4s ease-in-out infinite;
        overflow: hidden;
    }}
    @keyframes heroGlow {{
        0%, 100% {{ box-shadow: 0 30px 60px rgba(0,0,0,.45), 0 0 0px rgba(255,107,53,0.0); border-color: var(--hairline); }}
        50% {{ box-shadow: 0 30px 70px rgba(0,0,0,.5), 0 0 55px rgba(255,107,53,0.18); border-color: rgba(255,107,53,0.55); }}
    }}
    .kicker {{
        display: inline-flex; align-items: center; gap: 10px;
        font-size: 12px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase;
        color: var(--amber); margin-bottom: 16px;
    }}
    .kicker-dot {{ width: 7px; height: 7px; border-radius: 50%; background: var(--hot); box-shadow: 0 0 12px var(--hot); animation: blink 1.6s ease-in-out infinite; }}
    @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: .3; }} }}
    .hero-title {{
        font-family: 'Sora', sans-serif;
        font-size: 44px; font-weight: 800; letter-spacing: -0.5px; line-height: 1.18;
        margin: 0 0 14px 0;
        background: linear-gradient(100deg, var(--cream) 0%, var(--orange) 35%, var(--hot) 60%, var(--amber) 80%, var(--cream) 100%);
        background-size: 300% auto;
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        animation: shimmerText 7s ease-in-out infinite;
    }}
    @keyframes shimmerText {{ 0% {{ background-position: 0% 50%; }} 50% {{ background-position: 100% 50%; }} 100% {{ background-position: 0% 50%; }} }}
    .hero p.hero-sub, .hero-sub {{ font-size: 15.5px !important; color: #E9D8C8 !important; max-width: 560px !important; margin: 0 auto !important; opacity: .88 !important; line-height: 1.6 !important; font-weight: 400 !important; text-align: center !important; letter-spacing: .1px !important; }}

    /* ---------- SECTION TITLES ---------- */
    .section-title {{
        font-size: 13px; font-weight: 800; color: var(--orange2);
        margin-top: 48px; margin-bottom: 20px;
        text-transform: uppercase; letter-spacing: 2.2px;
        display: flex; align-items: center; gap: 12px;
        animation: fadeInUp .6s ease both;
    }}
    .section-title::after {{ content: ""; flex: 1; height: 2px; background: linear-gradient(to right, var(--orange), transparent); border-radius: 2px; }}

    /* ---------- CARDS (glow + shine-sweep on hover) ---------- */
    .metric-card, .kpi-container, .feature-card, .glass-card, .card {{
        position: relative; overflow: hidden;
        background: var(--glass);
        backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
        border-radius: 16px;
        border: 1px solid var(--hairline);
        box-shadow: 0 14px 34px rgba(0,0,0,0.4);
        transition: transform .35s cubic-bezier(.2,.8,.2,1), border-color .35s ease, box-shadow .35s ease, background .35s ease;
        height: 100%; margin-bottom: 16px;
        animation: fadeInUp .7s ease both;
    }}
    .metric-card, .kpi-container {{ padding: 26px 16px; text-align: center; }}
    .feature-card, .glass-card, .card {{ padding: 28px 24px; }}
    .feature-card, .glass-card {{ min-height: 210px; display: flex; flex-direction: column; justify-content: flex-start; box-sizing: border-box; }}

    .metric-card::after, .kpi-container::after, .feature-card::after, .glass-card::after, .card::after {{
        content: ""; position: absolute; top: 0; left: -160%; width: 45%; height: 100%;
        background: linear-gradient(120deg, transparent, rgba(255,255,255,.08), transparent);
        transform: skewX(-20deg); transition: left .7s ease;
    }}
    .metric-card:hover::after, .kpi-container:hover::after, .feature-card:hover::after, .glass-card:hover::after, .card:hover::after {{ left: 160%; }}

    .metric-card:hover, .kpi-container:hover, .feature-card:hover, .glass-card:hover, .card:hover {{
        transform: translateY(-12px) scale(1.035);
        border-color: var(--orange);
        background: var(--glass-hover);
        box-shadow: 0 28px 60px rgba(255,107,53,0.32), 0 0 55px rgba(255,59,92,0.16);
    }}

    .metric-value, .kpi-value {{ font-family: 'Sora', sans-serif; font-size: 33px; font-weight: 800; color: var(--orange); line-height: 1.1; }}
    .metric-label, .kpi-label {{ color: #D8C4B0; font-size: 11.5px; font-weight: 600; margin-top: 10px; letter-spacing: 1.2px; text-transform: uppercase; }}

    .card h3 {{ font-family: 'Sora', sans-serif; color: var(--orange); margin: 0 0 10px 0; font-size: 1.5rem; font-weight: 800; }}
    .card h4, .feature-card h4, .glass-card h4 {{ font-family: 'Sora', sans-serif; color: var(--cream); margin: 0 0 8px 0; font-size: 1.05rem; font-weight: 700; }}
    .card p, .feature-card p, .glass-card p {{ color: #C2AF9C; font-size: .92rem; margin: 0; line-height: 1.6; }}
    .single-line-title {{ font-family: 'Sora', sans-serif; font-size: 19px; font-weight: 700; color: var(--cream); text-align: center; margin-bottom: 10px; }}

    .icon-badge {{
        width: 52px; height: 52px; margin: 0 auto 16px auto;
        display: flex; align-items: center; justify-content: center;
        border-radius: 50%; background: rgba(255,107,53,0.10);
        border: 1px solid var(--hairline);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .hover-target:hover .icon-badge {{ transform: scale(1.18) rotate(-8deg); background: rgba(255,107,53,0.22); box-shadow: 0 0 26px rgba(255,107,53,0.35); }}

    .swot-s {{ border-left: 3px solid var(--amber); }}
    .swot-w {{ border-left: 3px solid var(--hot); }}
    .swot-o {{ border-left: 3px solid var(--orange2); }}
    .swot-t {{ border-left: 3px solid var(--orange); }}
    .swot-s h4, .swot-w h4, .swot-o h4, .swot-t h4 {{ color: var(--cream) !important; }}
    .swot-tag {{ display:inline-block; font-size: 10.5px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; color: var(--orange2); margin-bottom: 6px; }}

    /* ---------- PILLS / ROADMAP ---------- */
    .tech-pill-container {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; padding: 22px; background: rgba(15,9,6,.5); border-radius: 16px; border: 1px solid var(--hairline); }}
    .tech-pill {{ background: rgba(255,107,53,0.08); border: 1px solid var(--hairline); padding: 10px 20px; border-radius: 30px; color: var(--cream); font-weight: 600; font-size: 13.5px; display: flex; align-items: center; gap: 9px; transition: all .25s ease; }}
    .tech-pill:hover {{ transform: translateY(-3px) scale(1.05); border-color: var(--orange); background: rgba(255,107,53,0.16); box-shadow: 0 8px 20px rgba(255,107,53,0.25); }}
    .tech-dot {{ width: 7px; height: 7px; background: var(--hot); border-radius: 50%; box-shadow: 0 0 8px var(--hot); }}

    .roadmap-box {{ position: relative; overflow: hidden; background: var(--glass); border: 1px solid var(--hairline); padding: 24px 14px; border-radius: 16px; text-align: center; color: var(--cream); height: 100%; transition: all .35s ease; animation: fadeInUp .7s ease both; }}
    .roadmap-box:hover {{ border-color: var(--orange); transform: translateY(-6px); background: var(--glass-hover); box-shadow: 0 18px 40px rgba(255,107,53,0.2); }}
    .roadmap-num {{ font-family: 'Sora', sans-serif; font-size: 28px; background: linear-gradient(90deg, var(--orange), var(--hot)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900; display: block; margin-bottom: 8px; }}

    /* ---------- WIDGETS ---------- */
    div[data-baseweb="select"] {{ background-color: var(--glass) !important; border: 1px solid var(--hairline) !important; border-radius: 10px !important; }}
    li[role="option"] div, li[role="option"] span {{ color: var(--cream) !important; font-weight: 600 !important; }}
    div[data-testid="stDataFrame"] {{ background: rgba(12,8,5,.7) !important; padding: 16px; border-radius: 0 0 14px 14px; border: 1px solid var(--hairline); border-top: none; margin-top: -1px; }}
    .stTextInput input {{ background: var(--glass) !important; color: var(--cream) !important; border: 1px solid var(--hairline) !important; border-radius: 10px !important; }}

    div.stDownloadButton > button, div.stButton > button {{
        background: linear-gradient(135deg, var(--orange), var(--hot)) !important;
        color: #100C08 !important; font-family: 'Sora', sans-serif; border: none !important; border-radius: 30px !important;
        padding: 11px 26px !important; font-weight: 800 !important; letter-spacing: .3px; transition: all .25s ease !important;
        box-shadow: 0 8px 22px rgba(255,107,53,.3) !important;
    }}
    div.stDownloadButton > button:hover, div.stButton > button:hover {{ transform: translateY(-2px) scale(1.03); box-shadow: 0 12px 30px rgba(255,59,92,.45) !important; }}

    .stTabs [data-baseweb="tab-list"] {{ gap: 26px; border-bottom: 1px solid var(--hairline); }}
    .stTabs [data-baseweb="tab"] {{ font-family: 'Sora', sans-serif; font-size: 13.5px !important; font-weight: 700 !important; letter-spacing: .6px; text-transform: uppercase; color: #9A8776 !important; transition: color .2s ease; }}
    .stTabs [data-baseweb="tab"]:hover {{ color: var(--orange2) !important; }}
    .stTabs [aria-selected="true"] {{ color: var(--orange) !important; border-bottom: 2px solid var(--orange) !important; }}

    [data-testid="stExpander"] {{ background: var(--glass) !important; border: 1px solid var(--hairline) !important; border-radius: 14px !important; transition: border-color .3s ease; }}
    [data-testid="stExpander"]:hover {{ border-color: var(--orange) !important; }}

    /* ---------- STYLED PREVIEW TABLE ---------- */
    .styled-table-wrap {{
        overflow-x: auto; border-radius: 16px; border: 1px solid var(--hairline);
        background: var(--glass); backdrop-filter: blur(18px); margin-bottom: 22px;
        box-shadow: 0 14px 34px rgba(0,0,0,0.35);
    }}
    .styled-table {{ width: 100%; border-collapse: collapse; font-size: 13.5px; }}
    .styled-table thead th {{
        background: linear-gradient(135deg, rgba(255,107,53,.22), rgba(255,59,92,.14));
        color: var(--orange2); text-transform: uppercase; letter-spacing: 1px;
        font-size: 11px; font-weight: 800; padding: 15px 18px; text-align: left;
        border-bottom: 2px solid var(--orange); white-space: nowrap;
    }}
    .styled-table tbody td {{ padding: 12px 18px; color: #D8C4B0; border-bottom: 1px solid rgba(255,255,255,.05); white-space: nowrap; }}
    .styled-table tbody tr {{ animation: fadeInUp .5s ease both; transition: background .2s ease, transform .15s ease; }}
    .styled-table tbody tr:nth-child(even) {{ background: rgba(255,255,255,.02); }}
    .styled-table tbody tr:hover {{ background: rgba(255,107,53,.12); }}
    .styled-table tbody tr:hover td {{ color: var(--cream); }}
    .styled-table-wrap::-webkit-scrollbar {{ height: 8px; }}
    .styled-table-wrap::-webkit-scrollbar-thumb {{ background: var(--orange); border-radius: 8px; }}
    </style>

    <div class='blob1'></div>
    <div class='blob2'></div>
    {_ambient_particles()}
    """, unsafe_allow_html=True)


def apply_dark_plot(fig):
    fig.update_layout(
        font_color=CREAM,
        font_family="Plus Jakarta Sans",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(gridcolor="rgba(255,107,53,.12)", title_font=dict(color=ORANGE)),
        yaxis=dict(gridcolor="rgba(255,107,53,.12)", title_font=dict(color=ORANGE)),
        legend=dict(font=dict(color=CREAM)),
    )
    return fig


def page_hero(kicker, title, subtitle):
    st.markdown(f"""
        <div class="hero">
            <div class="kicker"><span class="kicker-dot"></span>{kicker}</div>
            <div class="hero-title">{title}</div>
            <p class="hero-sub">{subtitle}</p>
        </div>
    """, unsafe_allow_html=True)


def stagger_style(i, base_delay=0.09):
    """Inline style string giving card #i a staggered fade-in-up entrance."""
    return f'style="animation-delay:{i * base_delay:.2f}s;"'


def styled_table_html(df, max_rows=12):
    """A themed HTML preview table — glowing header, hover-lit rows, staggered entrance.
    Use for a short, beautiful preview; keep st.dataframe alongside it for full
    sorting/scrolling on large tables (HTML tables don't scale to thousands of rows)."""
    preview = df.head(max_rows)
    header_html = "".join(f"<th>{c}</th>" for c in preview.columns)
    rows_html = []
    for i, (_, row) in enumerate(preview.iterrows()):
        cells = "".join(f"<td>{row[c]}</td>" for c in preview.columns)
        rows_html.append(f'<tr style="animation-delay:{i * 0.04:.2f}s;">{cells}</tr>')
    return f"""
    <div class="styled-table-wrap">
        <table class="styled-table">
            <thead><tr>{header_html}</tr></thead>
            <tbody>{''.join(rows_html)}</tbody>
        </table>
    </div>
    """


# =========================================================
# LIVE COUNT-UP NUMBER (real JS, runs in its own iframe)
# =========================================================
def animated_counter(value, label, icon_name="star", prefix="", suffix="", decimals=0, color=None, height=168):
    """A KPI card whose number genuinely counts up from 0 on render."""
    color = color or ORANGE
    uid = uuid.uuid4().hex[:8]

    html = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Sora:wght@800&family=Plus+Jakarta+Sans:wght@600&display=swap');
        html, body {{ margin:0; padding:0; background: transparent; }}
        .cc-{uid} {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background: rgba(18,12,8,0.62);
            backdrop-filter: blur(18px);
            border: 1px solid rgba(255,107,53,0.30);
            border-radius: 16px;
            padding: 22px 14px;
            text-align: center;
            box-sizing: border-box;
            height: {height - 24}px;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            transition: all .3s ease;
        }}
        .cc-{uid}:hover {{ border-color: {color}; box-shadow: 0 10px 30px rgba(255,107,53,.25); transform: translateY(-4px); }}
        .cc-num-{uid} {{ font-family: 'Sora', sans-serif; font-size: 32px; font-weight: 800; color: {color}; }}
        .cc-label-{uid} {{ color: #D8C4B0; font-size: 11px; font-weight: 600; letter-spacing: 1.1px; text-transform: uppercase; margin-top: 8px; }}
    </style>
    <div class="cc-{uid}">
        <div>{icon(icon_name, color, 26)}</div>
        <div class="cc-num-{uid}" id="num-{uid}">0</div>
        <div class="cc-label-{uid}">{label}</div>
    </div>
    <script>
    (function() {{
        var el = document.getElementById("num-{uid}");
        var target = {value};
        var decimals = {decimals};
        var prefix = "{prefix}";
        var suffix = "{suffix}";
        var duration = 1400;
        var start = null;
        function ease(t) {{ return t === 1 ? 1 : 1 - Math.pow(2, -10 * t); }}
        function step(ts) {{
            if (!start) start = ts;
            var p = Math.min((ts - start) / duration, 1);
            var cur = target * ease(p);
            el.textContent = prefix + cur.toFixed(decimals) + suffix;
            if (p < 1) requestAnimationFrame(step);
            else el.textContent = prefix + target.toFixed(decimals) + suffix;
        }}
        requestAnimationFrame(step);
    }})();
    </script>
    """
    components.html(html, height=height)