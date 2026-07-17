import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, apply_theme, page_hero, animated_counter, apply_dark_plot, ORANGE, HOT, AMBER, CHART_PALETTE


def analysis_page():
    df = load_data()
    apply_theme("analysis")

    # Custom CSS to make the background image lighter/more transparent so graphs are highly visible
    st.markdown(
        """
        <style>
        /* Target Streamlit main content container and apply a semi-transparent dark/light mask over the background image */
        .stApp {
            background-blend-mode: overlay !important;
            background-color: rgba(14, 17, 23, 0.85) !important; /* Adjust transparency here */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    page_hero(
        "Performance Analytics",
        "Orders, Ratings & Delivery — In Detail",
        "A closer look at restaurant orders, customer ratings, delivery times, and pricing trends across every city."
    )

    city = st.selectbox("Select City", ["All Cities"] + sorted(df["city"].unique().tolist()))
    if city != "All Cities":
        df = df[df["city"] == city]
    if df.empty:
        st.warning("No data found for this city.")
        return

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Performance", "Ratings", "Delivery", "Pricing", "City Overview"])

    # ================= TAB 1: PERFORMANCE =================
    with tab1:
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            animated_counter(df["restaurant"].nunique(), "Restaurants", icon_name="database", color=ORANGE)
        with m_col2:
            animated_counter(df["total_ratings"].sum(), "Total Reviews", icon_name="star", color=HOT)
        with m_col3:
            animated_counter(df["food_type"].nunique(), "Cuisines", icon_name="tag", color=AMBER)

        st.markdown('<div class="section-title">Top 10 Restaurants by Reviews</div>', unsafe_allow_html=True)
        r_rat = df.groupby("restaurant")["total_ratings"].sum().sort_values(ascending=False).head(10).reset_index()
        fig = apply_dark_plot(px.bar(r_rat, x="total_ratings", y="restaurant", orientation="h",
                                      color_discrete_sequence=[ORANGE],
                                      labels={"total_ratings": "Reviews", "restaurant": "Restaurant"}))
        st.plotly_chart(fig.update_yaxes(categoryorder="total ascending"), use_container_width=True)

        st.markdown('<div class="section-title">Popular Cuisines</div>', unsafe_allow_html=True)
        pop_f = df.groupby("food_type")["total_ratings"].sum().sort_values(ascending=False).head(10).reset_index()
        fig = apply_dark_plot(px.bar(pop_f, x="total_ratings", y="food_type", orientation="h",
                                      color_discrete_sequence=[AMBER],
                                      labels={"total_ratings": "Reviews", "food_type": "Cuisine"}))
        st.plotly_chart(fig.update_yaxes(categoryorder="total ascending"), use_container_width=True)

        st.markdown('<div class="section-title">Review Share by Cuisine (Top 10)</div>', unsafe_allow_html=True)
        share_cuisine = df.groupby("food_type")["total_ratings"].sum().sort_values(ascending=False).head(10).reset_index()
        fig = apply_dark_plot(px.pie(share_cuisine, names="food_type", values="total_ratings", hole=0.4,
                                      color_discrete_sequence=CHART_PALETTE,
                                      labels={"total_ratings": "Reviews", "food_type": "Cuisine"}))
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

        price_col = [c for c in df.columns if "cost" in c or "price" in c]
        if price_col:
            st.markdown('<div class="section-title">Price vs Reviews</div>', unsafe_allow_html=True)
            fig = apply_dark_plot(px.scatter(df, x=price_col[0], y="total_ratings",
                                              color="city" if city == "All Cities" else "food_type",
                                              color_discrete_sequence=CHART_PALETTE,
                                              hover_name="restaurant",
                                              labels={price_col[0]: "Price", "total_ratings": "Reviews"}))
            st.plotly_chart(fig, use_container_width=True)

    # ================= TAB 2: RATINGS =================
    with tab2:
        r_cols = [c for c in df.columns if "rating" in c and c != "total_ratings"]
        if r_cols:
            r_col = r_cols[0]
            st.markdown('<div class="section-title">Ratings by Cuisine</div>', unsafe_allow_html=True)
            top_foods = df["food_type"].value_counts().head(8).index
            fig = apply_dark_plot(px.strip(df[df["food_type"].isin(top_foods)], x="food_type", y=r_col, color="food_type",
                                            color_discrete_sequence=CHART_PALETTE,
                                            labels={"food_type": "Cuisine", r_col: "Rating"}))
            st.plotly_chart(fig.update_layout(showlegend=False), use_container_width=True)

            st.markdown('<div class="section-title">Ratings vs Popularity</div>', unsafe_allow_html=True)
            fig = apply_dark_plot(px.scatter(df, x=r_col, y="total_ratings", size="total_ratings", color=r_col,
                                              color_continuous_scale=[HOT, ORANGE, AMBER],
                                              hover_name="restaurant",
                                              labels={r_col: "Rating", "total_ratings": "Reviews"}))
            st.plotly_chart(fig, use_container_width=True)

            st.markdown('<div class="section-title">Rating Distribution by City</div>', unsafe_allow_html=True)
            fig = apply_dark_plot(px.violin(df, x="city", y=r_col, color="city", box=True,
                                              color_discrete_sequence=CHART_PALETTE,
                                              labels={"city": "City", r_col: "Rating"}))
            st.plotly_chart(fig.update_layout(showlegend=False), use_container_width=True)
        else:
            st.warning("No rating data found in this dataset.")

    # ================= TAB 3: DELIVERY =================
    with tab3:
        if "delivery_time" in df.columns:
            st.markdown('<div class="section-title">Delivery Time Distribution</div>', unsafe_allow_html=True)
            fig = apply_dark_plot(px.histogram(df, x="delivery_time", nbins=20, color_discrete_sequence=[ORANGE],
                                                labels={"delivery_time": "Minutes", "count": "Orders"}))
            st.plotly_chart(fig.update_layout(showlegend=False), use_container_width=True)

            r_cols = [c for c in df.columns if "rating" in c and c != "total_ratings"]
            if r_cols:
                st.markdown('<div class="section-title">Delivery Speed vs Rating</div>', unsafe_allow_html=True)
                fig = apply_dark_plot(px.scatter(df, x="delivery_time", y=r_cols[0],
                                                  color="city" if city == "All Cities" else "food_type",
                                                  color_discrete_sequence=CHART_PALETTE,
                                                  hover_name="restaurant",
                                                  labels={"delivery_time": "Minutes", r_cols[0]: "Rating"}))
                st.plotly_chart(fig, use_container_width=True)

            st.markdown('<div class="section-title">Average Delivery Time by City</div>', unsafe_allow_html=True)
            city_delivery = df.groupby("city")["delivery_time"].mean().sort_values(ascending=False).reset_index()
            fig = apply_dark_plot(px.bar(city_delivery, x="delivery_time", y="city", orientation="h",
                                          color_discrete_sequence=[AMBER],
                                          labels={"delivery_time": "Minutes", "city": "City"}))
            st.plotly_chart(fig.update_yaxes(categoryorder="total ascending"), use_container_width=True)

            st.markdown('<div class="section-title">Delivery Time Ranges by City</div>', unsafe_allow_html=True)
            fig = apply_dark_plot(px.box(df, x="city", y="delivery_time", color="city",
                                          color_discrete_sequence=CHART_PALETTE,
                                          labels={"city": "City", "delivery_time": "Minutes"}))
            st.plotly_chart(fig.update_layout(showlegend=False), use_container_width=True)
        else:
            st.warning("No delivery time data found in this dataset.")

    # ================= TAB 4: PRICING =================
    with tab4:
        p_cols = [c for c in df.columns if "price" in c or "cost" in c]
        r_cols = [c for c in df.columns if "rating" in c and c != "total_ratings"]
        if p_cols and r_cols:
            p_col, r_col = p_cols[0], r_cols[0]

            st.markdown('<div class="section-title">Price Distribution</div>', unsafe_allow_html=True)
            fig = apply_dark_plot(px.histogram(df, x=p_col, nbins=25, color_discrete_sequence=[ORANGE],
                                                labels={p_col: "Price", "count": "Count"}))
            st.plotly_chart(fig.update_layout(showlegend=False), use_container_width=True)

            st.markdown('<div class="section-title">Price vs Rating</div>', unsafe_allow_html=True)
            fig = apply_dark_plot(px.scatter(df, x=p_col, y=r_col,
                                              color="city" if city == "All Cities" else "food_type",
                                              color_discrete_sequence=CHART_PALETTE,
                                              hover_name="restaurant",
                                              labels={p_col: "Price", r_col: "Rating"}))
            st.plotly_chart(fig, use_container_width=True)

            st.markdown('<div class="section-title">Average Price by City</div>', unsafe_allow_html=True)
            city_price = df.groupby("city")[p_col].mean().sort_values(ascending=False).reset_index()
            fig = apply_dark_plot(px.bar(city_price, x=p_col, y="city", orientation="h",
                                          color_discrete_sequence=[HOT],
                                          labels={p_col: "Price", "city": "City"}))
            st.plotly_chart(fig.update_yaxes(categoryorder="total ascending"), use_container_width=True)

            st.markdown('<div class="section-title">Price Ranges by City</div>', unsafe_allow_html=True)
            fig = apply_dark_plot(px.box(df, x="city", y=p_col, color="city",
                                          color_discrete_sequence=CHART_PALETTE,
                                          labels={"city": "City", p_col: "Price"}))
            st.plotly_chart(fig.update_layout(showlegend=False), use_container_width=True)
        else:
            st.warning("No price data found in this dataset.")

    # ================= TAB 5: CITY OVERVIEW =================
    with tab5:
        st.markdown('<div class="section-title">Market Share by City</div>', unsafe_allow_html=True)
        city_count = df["city"].value_counts().reset_index()
        city_count.columns = ["city", "restaurants"]
        fig = apply_dark_plot(px.pie(city_count, names="city", values="restaurants", hole=0.5,
                                      color_discrete_sequence=CHART_PALETTE))
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

        st.markdown('<div class="section-title">Review Traffic by City</div>', unsafe_allow_html=True)
        city_engagement = df.groupby("city")["total_ratings"].sum().sort_values(ascending=False).reset_index()
        fig = apply_dark_plot(px.funnel(city_engagement, x="total_ratings", y="city",
                                         color_discrete_sequence=[ORANGE],
                                         labels={"total_ratings": "Reviews", "city": "City"}))
        st.plotly_chart(fig, use_container_width=True)

        st.markdown('<div class="section-title">Restaurant Count by City</div>', unsafe_allow_html=True)
        fig = apply_dark_plot(px.histogram(df, x="city", color_discrete_sequence=[AMBER]))
        st.plotly_chart(fig.update_layout(yaxis_title="Restaurants", showlegend=False), use_container_width=True)

        r_cols = [c for c in df.columns if "rating" in c and c != "total_ratings"]
        if r_cols:
            st.markdown('<div class="section-title">Satisfaction by City</div>', unsafe_allow_html=True)
            fig = apply_dark_plot(px.box(df, x="city", y=r_cols[0], color="city",
                                          color_discrete_sequence=CHART_PALETTE,
                                          labels={"city": "City", r_cols[0]: "Rating"}))
            st.plotly_chart(fig.update_layout(showlegend=False), use_container_width=True)