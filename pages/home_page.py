import streamlit as st
import requests
from streamlit_lottie import st_lottie
from utils import load_data, apply_theme, page_hero, animated_counter, icon_badge, stagger_style, ORANGE, HOT, AMBER


def home_page():
    df = load_data()
    apply_theme("home")

    st.markdown(
        """
        <style>
        div[data-testid="stHorizontalBlock"] {
            display: flex !important;
            align-items: stretch !important;
        }

        div[data-testid="column"],
        div[data-testid="stColumn"] {
            display: flex !important;
            flex-direction: column !important;
            height: 100% !important;
        }

        div[data-testid="column"] > div,
        div[data-testid="stColumn"] > div {
            flex: 1 1 auto !important;
            display: flex !important;
            flex-direction: column !important;
            height: 100% !important;
        }

        div[data-testid="column"] [data-testid="stMarkdownContainer"],
        div[data-testid="stColumn"] [data-testid="stMarkdownContainer"] {
            height: 100% !important;
            display: flex !important;
            flex-direction: column !important;
        }

        .feature-card {
            flex: 1 !important;
            height: 260px !important;
            min-height: 260px !important;
            max-height: 260px !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: flex-start !important;
            box-sizing: border-box !important;
            overflow: hidden !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    page_hero(
        "Smart Food Delivery Intelligence",
        "The Complete Restaurant &amp; Delivery Dashboard",
        "A live, data-driven look at orders, restaurant performance, and city-wide delivery trends."
    )

    st.markdown("<div class='section-title'>Market Snapshot</div>", unsafe_allow_html=True)
    res_count = df["restaurant"].nunique() if "restaurant" in df.columns else len(df)
    avg_r = df["avg_rating"].mean() if "avg_rating" in df.columns else 0.0
    city_count = df["city"].nunique() if "city" in df.columns else 0
    total_orders = df["total_ratings"].sum() if "total_ratings" in df.columns else len(df)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        animated_counter(res_count, "Total Outlets", icon_name="database", suffix="+", color=ORANGE)
    with c2:
        animated_counter(avg_r, "Average Rating", icon_name="star", decimals=1, color=AMBER)
    with c3:
        animated_counter(city_count, "Active Cities", icon_name="pin", color=HOT)
    with c4:
        animated_counter(total_orders / 1000, "Total Orders", icon_name="truck", decimals=0, suffix="K+", color=ORANGE)

    st.markdown("<div class='section-title'>Today's Highlights</div>", unsafe_allow_html=True)
    h1, h2, h3 = st.columns(3)

    if "restaurant" in df.columns and "avg_rating" in df.columns:
        top_row = df.loc[df["avg_rating"].idxmax()]
        top_name, top_rating = top_row["restaurant"], top_row["avg_rating"]
    else:
        top_name, top_rating = "N/A", 0

    if "city" in df.columns and "delivery_time" in df.columns:
        fastest_city = df.groupby("city")["delivery_time"].mean().idxmin()
    else:
        fastest_city = "N/A"

    if "food_type" in df.columns:
        top_cuisine = df["food_type"].value_counts().idxmax()
    else:
        top_cuisine = "N/A"

    highlights = [
        ("star", AMBER, "Highest Rated", top_name, f"{top_rating:.1f} \u2605 average rating"),
        ("truck", HOT, "Fastest City", fastest_city, "Lowest average delivery time"),
        ("tag", ORANGE, "Most Ordered Cuisine", top_cuisine, "Leads order volume across cities"),
    ]
    for i, (col, (ic, color, label, value, note)) in enumerate(zip([h1, h2, h3], highlights)):
        col.markdown(f"""
        <div class="feature-card hover-target" {stagger_style(i)}>
            {icon_badge(ic, color)}
            <div style="text-align:center; color:{color}; font-size:11px; font-weight:800; letter-spacing:1.5px; text-transform:uppercase;">{label}</div>
            <div class="single-line-title" style="margin-top:4px;">{value}</div>
            <p style='text-align:center;'>{note}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Explore The Dashboard</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    modules = [
        ("database", ORANGE, "Dataset Explorer", "Browse raw restaurant records, filter by city or cuisine, and download the data you need."),
        ("chart", HOT, "Analytics Hub", "Visual breakdowns of orders, ratings, and delivery speed — sliced by city and cuisine."),
        ("bulb", AMBER, "Insights &amp; Recommendations", "Business takeaways, a SWOT view, and a practical roadmap based on the data."),
    ]
    for i, (col, (ic, color, title, desc)) in enumerate(zip([col1, col2, col3], modules)):
        col.markdown(f"""
        <div class="feature-card hover-target" {stagger_style(i)}>
            {icon_badge(ic, color)}
            <div class="single-line-title">{title}</div>
            <p style='text-align:center;'>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    try:
        url = "https://lottie.host/89040d89-9a25-4b10-859a-1eb99279dc62/P0Z6G9fVpY.json"
        animation = requests.get(url, timeout=5).json()
        st_lottie(animation, height=220, key="vibrant_lottie")
    except Exception:
        pass

    st.markdown(f"""
        <div class="card" style="text-align:center; border: 1px dashed {ORANGE}; height:auto;">
            <p style="margin:0; color:#C2AF9C;">Want the full story — methodology, tools, and who built this? Head to <b style="color:{ORANGE};">About</b>.</p>
        </div>
        """, unsafe_allow_html=True)