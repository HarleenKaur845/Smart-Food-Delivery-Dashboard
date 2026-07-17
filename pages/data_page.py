import streamlit as st
import pandas as pd
from utils import load_data, apply_theme, page_hero, icon, animated_counter, styled_table_html, ORANGE, HOT, AMBER


def data_page():
    df = load_data()
    apply_theme("data")

    st.markdown(
        """
        <style>
        .hero-container p, [data-testid="stHeader"] ~ div p {
            text-align: center !important;
        }
        .section-title, .card p, div[data-testid="stMarkdownContainer"] div p {
            text-align: left !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    page_hero(
        "Dataset Explorer",
        "Search, Filter & Inspect The Data",
        "Every restaurant record in one place. Search by name, filter by city or cuisine, and download exactly what you need."
    )

    res_count = df["restaurant"].nunique() if "restaurant" in df.columns else len(df)
    city_count = df["city"].nunique() if "city" in df.columns else 0
    avg_r = df["avg_rating"].mean() if "avg_rating" in df.columns else (df["rating"].mean() if "rating" in df.columns else 0.0)
    avg_d = df["delivery_time"].mean() if "delivery_time" in df.columns else 0.0

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        animated_counter(res_count, "Restaurants", icon_name="database", color=ORANGE)
    with kpi2:
        animated_counter(city_count, "Active Cities", icon_name="pin", color=HOT)
    with kpi3:
        animated_counter(avg_r, "Avg Rating", icon_name="star", decimals=2, color=AMBER)
    with kpi4:
        animated_counter(avg_d, "Avg Delivery", icon_name="clock", suffix="m", color=ORANGE)

    st.markdown('<div class="section-title">Search &amp; Filter</div>', unsafe_allow_html=True)
    search_query = st.text_input("Search by Restaurant Name", "", placeholder="Type a restaurant name to search...")

    col1, col2 = st.columns(2)
    with col1:
        city_options = ["All Cities"] + sorted(df["city"].dropna().unique().tolist()) if "city" in df.columns else ["All Cities"]
        city_filter = st.selectbox("Select City", city_options)
    with col2:
        food_options = ["All Cuisines"] + sorted(df["food_type"].dropna().unique().tolist()) if "food_type" in df.columns else ["All Cuisines"]
        food_filter = st.selectbox("Select Cuisine", food_options)

    filtered_df = df.copy()
    if search_query and "restaurant" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["restaurant"].str.contains(search_query, case=False, na=False)]
    if city_filter != "All Cities" and "city" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["city"] == city_filter]
    if food_filter != "All Cuisines" and "food_type" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["food_type"] == food_filter]

    display_df = filtered_df.rename(columns={
        "id": "ID", "area": "Area", "city": "City", "restaurant": "Restaurant",
        "price": "Price", "avg_rating": "Average Rating", "total_ratings": "Total Ratings",
        "food_type": "Food Type", "address": "Address", "delivery_time": "Delivery Time"
    })

    st.markdown('<div class="section-title">Results</div>', unsafe_allow_html=True)
    csv_data = display_df.to_csv(index=False).encode('utf-8')
    d_col1, d_col2 = st.columns([3, 1])
    with d_col1:
        st.markdown(f'<div class="card" style="text-align:left; height:auto; padding:16px 22px;">Showing <b style="color:{ORANGE};">{len(display_df):,}</b> entries matching your search.</div>', unsafe_allow_html=True)
    with d_col2:
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="food_delivery_data.csv",
            mime="text/csv",
            use_container_width=True
        )

    tab_dataset, tab_stats = st.tabs(["Dataset View", "Statistical Summary"])

    with tab_dataset:
        st.markdown('<div class="section-title" style="margin-top:14px;">Quick Preview</div>', unsafe_allow_html=True)
        if not display_df.empty:
            st.markdown(styled_table_html(display_df, max_rows=8), unsafe_allow_html=True)
        else:
            st.warning("No data matches your filters.")

        st.markdown(f"""
            <div style="background: linear-gradient(90deg, rgba(255,107,53,.12), rgba(255,59,92,.06));
                        border: 1px solid rgba(255,107,53,.3); border-bottom: none;
                        border-radius: 14px 14px 0 0; padding: 14px 20px;
                        display:flex; align-items:center; justify-content:space-between; margin-top:14px;">
                <span style="font-weight:700; color:{ORANGE}; letter-spacing:.5px;">Full Table — Sortable &amp; Scrollable</span>
                <span style="color:#9A8776; font-size:12.5px;">{len(display_df):,} rows</span>
            </div>
        """, unsafe_allow_html=True)

        column_config = {}
        if "Average Rating" in display_df.columns:
            column_config["Average Rating"] = st.column_config.ProgressColumn(
                "Average Rating", format="%.2f ★", min_value=0, max_value=5
            )
        if "Price" in display_df.columns:
            column_config["Price"] = st.column_config.NumberColumn("Price", format="₹ %.0f")
        if "Total Ratings" in display_df.columns:
            column_config["Total Ratings"] = st.column_config.NumberColumn("Total Ratings", format="%d")
        if "Delivery Time" in display_df.columns:
            column_config["Delivery Time"] = st.column_config.NumberColumn("Delivery Time", format="%d min")

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            column_config=column_config,
            height=460,
        )

    with tab_stats:
        st.markdown("<br>", unsafe_allow_html=True)
        if not display_df.empty:
            stats_df = display_df.describe().reset_index().rename(columns={"index": "Metric"})
            st.markdown(styled_table_html(stats_df), unsafe_allow_html=True)
        else:
            st.warning("No data matches your filters, so there's nothing to summarize.")