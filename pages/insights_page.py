import streamlit as st
import pandas as pd
from utils import load_data, apply_theme, page_hero, icon, animated_counter, stagger_style, ORANGE, ORANGE2, HOT, AMBER


def insights_page():
    df = load_data()
    apply_theme("insights")

    total = len(df)
    avg_r = round(df["avg_rating"].mean(), 2)
    avg_d = int(df["delivery_time"].mean())
    top_city = df["city"].value_counts().idxmax()

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
        "Core Insights",
        "What The Data Is Telling Us",
        "Simple, data-driven takeaways on delivery speed, customer happiness, and where to focus next."
    )

    st.markdown(f"""
        <div class="card" style="text-align:left; height:auto;">
            <h3>Executive Summary</h3>
            <p style="font-size: 1rem; color: #C2AF9C;">
                This report looks at {total:,} restaurant records to understand customer ratings, delivery times, and city-wise trends.
                Our biggest market is <b style="color:{ORANGE};">{top_city}</b>. Overall performance is strong, but cutting delivery delays is
                our biggest opportunity. Below are simple steps to improve efficiency, keep customers happy, and grow revenue.
            </p>
        </div>
    """, unsafe_allow_html=True)

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        animated_counter(total, "Total Records", icon_name="database", color=ORANGE)
    with k2:
        animated_counter(avg_r, "Average Rating", icon_name="star", decimals=2, suffix=" / 5", color=AMBER)
    with k3:
        animated_counter(avg_d, "Avg Delivery Time", icon_name="clock", suffix="m", color=HOT)
    with k4:
        st.markdown(f'<div class="metric-card" style="height:144px; display:flex; flex-direction:column; align-items:center; justify-content:center;">{icon("pin", ORANGE, 26)}<div class="metric-value" style="margin-top:8px;">{top_city}</div><div class="metric-label">Top City</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Key Business Findings</div>', unsafe_allow_html=True)
    f1, f2, f3, f4 = st.columns(4)
    findings = [
        ("trend-up", "Customer Reviews", "Customers rate food higher when it arrives under 30 minutes. Ratings drop fast after 45 minutes."),
        ("trend-down", "Delivery Speed", "Most delays happen during dinner peak hours, mainly due to rider shortage and traffic."),
        ("tag", "Cuisine Choice", "Everyday items drive most orders, but premium dishes bring in higher profit per order."),
        ("pin", "City Presence", "Big cities drive high order volume, but smaller emerging areas show strong growth potential."),
    ]
    for i, (col, (ic, title, desc)) in enumerate(zip([f1, f2, f3, f4], findings)):
        col.markdown(f'<div class="feature-card" {stagger_style(i)}>{icon(ic, ORANGE, 22)}<h4 style="margin-top:10px;">{title}</h4><p>{desc}</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">SWOT Analysis</div>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    s1.markdown(f'<div class="feature-card swot-s"><span class="swot-tag">Strengths</span><p>High order volume in major cities and a loyal customer base keeping ratings stable.</p></div>', unsafe_allow_html=True)
    s2.markdown(f'<div class="feature-card swot-w"><span class="swot-tag" style="color:{HOT};">Weaknesses</span><p>Slow delivery during busy hours, which can frustrate regular customers.</p></div>', unsafe_allow_html=True)
    s3.markdown(f'<div class="feature-card swot-o"><span class="swot-tag" style="color:{ORANGE2};">Opportunities</span><p>Giving top-rated restaurants extra visibility and rewards to boost order value.</p></div>', unsafe_allow_html=True)
    s4.markdown(f'<div class="feature-card swot-t"><span class="swot-tag" style="color:{ORANGE};">Threats</span><p>New local food apps offering big discounts in our top-performing areas.</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Detailed Insights</div>', unsafe_allow_html=True)
    with st.expander("Rating Insight — Customer Happiness"):
        st.write(f"Keeping our average rating above {avg_r} is important. When a restaurant's rating drops below 4.0, customers tend to stop ordering from it.")
    with st.expander("Delivery Insight — Speed vs Quality"):
        st.write(f"Our average delivery time is {avg_d} minutes. Setting up small rider hubs in busy areas could easily cut this by 5-10 minutes.")
    with st.expander("Pricing Insight — Order Cost"):
        st.write("Customers are willing to pay a bit more if fast, fresh delivery is guaranteed.")
    with st.expander("Geographic Insight — City Focus"):
        st.write(f"Since {top_city} generates the most orders, adding more delivery partners there first would help manage the heavy load.")
    with st.expander("Cuisine Insight — Popular Food Categories"):
        st.write("Healthy meals and specialty desserts are growing fast. Their order count is low, but they earn more money per order.")

    st.markdown('<div class="section-title">Recommendation Matrix</div>', unsafe_allow_html=True)
    st.table(pd.DataFrame({
        "Recommendation": ["Fix Delivery Delays", "Promote Top Restaurants", "Review Partner Incentives", "Add New Food Categories"],
        "Business Impact": ["High Impact", "High Impact", "Medium Impact", "High Impact"],
        "Priority Level": ["Immediate Action", "Immediate Action", "Medium Priority", "High Priority"]
    }))

    st.markdown('<div class="section-title">Target Outcomes</div>', unsafe_allow_html=True)
    i1, i2, i3, i4 = st.columns(4)
    with i1:
        animated_counter(15, "Customer Satisfaction", icon_name="trend-up", prefix="+", suffix="%", color=ORANGE)
    with i2:
        animated_counter(12, "Delivery Expenses", icon_name="trend-down", prefix="-", suffix="%", color=HOT)
    with i3:
        animated_counter(28, "Restaurant Sales", icon_name="trend-up", prefix="+", suffix="%", color=AMBER)
    with i4:
        animated_counter(22, "Overall Growth", icon_name="trend-up", prefix="+", suffix="%", color=ORANGE)

    st.markdown('<div class="section-title">Project Roadmap</div>', unsafe_allow_html=True)
    r1, r2, r3, r4 = st.columns(4)
    phases = [("01", "Fix Delivery Speed"), ("02", "Boost Engagement"), ("03", "Help Partners Grow"), ("04", "Expand to New Cities")]
    for i, (col, (num, label)) in enumerate(zip([r1, r2, r3, r4], phases)):
        col.markdown(f'<div class="roadmap-box" {stagger_style(i)}><span class="roadmap-num">{num}</span><small style="opacity:.85;">{label}</small></div>', unsafe_allow_html=True)

    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="card" style="text-align:center; border: 1px dashed {ORANGE}; height:auto;">
            <h3>Strategic Outlook</h3>
            <p style="font-size:1rem; max-width:800px; margin:0 auto; color:#C2AF9C;">
                By combining smarter delivery planning with better promotion of top restaurants, we can protect our market share
                and build the financial stability needed to grow into new areas.
            </p>
        </div>
    """, unsafe_allow_html=True)