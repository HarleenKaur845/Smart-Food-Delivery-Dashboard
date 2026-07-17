import streamlit as st
from streamlit_option_menu import option_menu

from pages.home_page import home_page
from pages.data_page import data_page
from pages.analysis_page import analysis_page
from pages.insights_page import insights_page
from pages.about_page import about_page

st.set_page_config(
    page_title="Smart Food Dashboard",
    page_icon="🍕",
    layout="wide"
)
st.markdown("""
    <style>
        /* Default Streamlit pages navigation links ko hide karne ke liye */
        [data-testid="stSidebarNav"] {display: none !important;}
    </style>
""", unsafe_allow_html=True)

with st.sidebar:

    # Branded header above the menu — plain CSS, lives outside the
    # option_menu iframe so it picks up the site font/colors fine.
    st.markdown("""
        <div style="text-align:center; padding: 6px 0 18px 0;">
            <div style="font-family:'Sora',sans-serif; font-size:22px; font-weight:800;
                        background: linear-gradient(90deg, #FF6B35, #FF3B5C, #FFC93C);
                        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                        letter-spacing:.5px;">
                SMART FOOD
            </div>
            <div style="color:#9A8776; font-size:11px; letter-spacing:2.5px; margin-top:2px;">
                DELIVERY DASHBOARD
            </div>
        </div>
    """, unsafe_allow_html=True)

    # NOTE: option_menu renders inside its own iframe, so global page CSS
    # can't reach it — it has to be themed here, via its own `styles=` dict.
    opt = option_menu(
        menu_title="Main Menu",
        menu_icon="egg-fried",
        options=[
            "Home Page",
            "Data Page",
            "Analysis Page",
            "Insights & Recommendations",
            "About Page"
        ],
        icons=[
            "house-door-fill",
            "database-fill",
            "graph-up-arrow",
            "lightbulb-fill",
            "info-circle-fill"
        ],
        styles={
            "container": {
                "padding": "8px !important",
                "background-color": "#0a0604",
                "border-radius": "14px",
                "border": "1px solid rgba(255,107,53,0.25)",
            },
            "menu-title": {
                "color": "#FF9142",
                "font-weight": "700",
            },
            "icon": {
                "color": "#FF9142",
                "font-size": "17px",
            },
            "nav-link": {
                "font-size": "14.5px",
                "text-align": "left",
                "margin": "4px 0",
                "padding": "12px 14px",
                "border-radius": "10px",
                "color": "#D8C4B0",
                "background-color": "transparent",
                "--hover-color": "#1a0f08",
            },
            "nav-link-selected": {
                "background-color": "#FF6B35",
                "color": "#0a0604",
                "font-weight": "700",
                "box-shadow": "0 4px 15px rgba(255,107,53,0.4)",
            },
        }
    )

if opt == "Home Page":
    home_page()

elif opt == "Data Page":
    data_page()

elif opt == "Analysis Page":
    analysis_page()

elif opt == "Insights & Recommendations":
    insights_page()

elif opt == "About Page":
    about_page()