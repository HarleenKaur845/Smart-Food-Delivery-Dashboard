import streamlit as st
from utils import apply_theme, page_hero, icon, animated_counter, stagger_style, ORANGE, HOT, AMBER


def about_page():
    apply_theme("about")

    page_hero(
        "About The Project",
        "The Story Behind The Dashboard",
        "Why this was built, how it works, and who made it."
    )

    # --- THE STORY ---
    st.markdown('<div class="section-title">The Story</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="card" style="text-align:left;">
            Food delivery generates huge amounts of data every day — orders, ratings, delivery times, prices — but
            most of it sits unused in spreadsheets. This project turns that raw data into something people can
            actually look at and act on: a single dashboard covering restaurant performance, delivery speed, pricing,
            and customer sentiment, all in plain, simple language.
        </div>
        """, unsafe_allow_html=True)

    # --- WHAT YOU CAN DO HERE ---
    st.markdown('<div class="section-title">What You Can Do Here</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    features = [
        ("trend-up", "Performance Tracking", "Track how restaurants are doing, check total sales, and see if they're hitting business targets."),
        ("tag", "Cuisine Popularity", "Find out which food items and categories are in high demand across different city areas."),
        ("star", "Rating Analysis", "Read through customer reviews and star ratings to see how happy users are with the service."),
        ("truck", "Delivery Timelines", "Check how long riders take to deliver food and find ways to fix delays during busy hours."),
    ]
    for i, (col, (ic, title, desc)) in enumerate(zip([c1, c2, c1, c2], features)):
        col.markdown(f'<div class="glass-card" {stagger_style(i)}>{icon(ic, ORANGE, 22)}<h4 style="margin-top:10px;">{title}</h4><p>{desc}</p></div><br>', unsafe_allow_html=True)

    # --- HOW IT WAS BUILT ---
    st.markdown('<div class="section-title">How It Was Built</div>', unsafe_allow_html=True)
    w1, w2, w3, w4 = st.columns(4)
    steps = [
        ("01", "download", "Data Collection", "Gathering raw restaurant &amp; order files"),
        ("02", "layers", "Data Cleaning", "Fixing gaps and preparing the dataset"),
        ("03", "search", "Exploration", "Finding patterns and relationships"),
        ("04", "grid", "Interface Build", "Designing this dashboard experience"),
    ]
    for i, (col, (num, ic, title, desc)) in enumerate(zip([w1, w2, w3, w4], steps)):
        col.markdown(f"""
        <div class="roadmap-box" {stagger_style(i)}>
            <span class="roadmap-num">{num}</span>
            {icon(ic, ORANGE, 22)}
            <div style="margin-top:10px; font-weight:700;">{title}</div>
            <small style="opacity:.7; font-weight:400;">{desc}</small>
        </div>
        """, unsafe_allow_html=True)

    # --- DATASET STATISTICS (count-up) ---
    st.markdown('<div class="section-title">Dataset Information</div>', unsafe_allow_html=True)
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        animated_counter(8680, "Total Rows", icon_name="database", suffix="+", color=ORANGE)
    with k2:
        animated_counter(10, "Data Columns", icon_name="grid", color=HOT)
    with k3:
        st.markdown(f'<div class="metric-card" style="height:144px; display:flex; flex-direction:column; align-items:center; justify-content:center;">{icon("pin", AMBER, 26)}<div class="metric-value" style="margin-top:8px;">Multi-City</div><div class="metric-label">Covered Areas</div></div>', unsafe_allow_html=True)
    with k4:
        animated_counter(100, "Live Updates", icon_name="flame", suffix="%", color=ORANGE)

    # --- TECH STACK ---
    st.markdown('<div class="section-title">Tools &amp; Libraries Used</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="tech-pill-container">
        <div class="tech-pill"><div class="tech-dot"></div> Python</div>
        <div class="tech-pill"><div class="tech-dot"></div> Pandas</div>
        <div class="tech-pill"><div class="tech-dot"></div> Plotly</div>
        <div class="tech-pill"><div class="tech-dot"></div> Streamlit</div>
        <div class="tech-pill"><div class="tech-dot"></div> Seaborn</div>
        <div class="tech-pill"><div class="tech-dot"></div> Matplotlib</div>
    </div>
    """, unsafe_allow_html=True)

    # --- DEVELOPER SECTION ---
    st.markdown('<div class="section-title">Developed By</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class='card' style='text-align: center; border: 1px dashed {ORANGE}; max-width: 450px; margin: 0 auto; height:auto;'>
        <p style='color: {ORANGE}; font-weight: 700; margin-bottom: 8px; font-size: 0.8rem; letter-spacing: 2px; text-transform:uppercase;'>Developed By</p>
        <h2 style='margin:0; font-family: "Sora", sans-serif; color:#FFF3E6; font-weight:800; font-size:1.7rem;'>Harleen Kaur</h2>
    </div>
    """, unsafe_allow_html=True)