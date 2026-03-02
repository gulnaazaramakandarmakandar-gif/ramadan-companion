import streamlit as st
import base64
import random

st.set_page_config(page_title="Ramadan Companion", layout="centered")

# ---------------- BACKGROUND FUNCTION ----------------
def add_bg():
    with open("background.jpg", "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
    <style>

    /* Hide Sidebar */
    [data-testid="stSidebar"] {{display: none;}}
    [data-testid="collapsedControl"] {{display: none;}}

    /* Premium Background with Dark Overlay */
    .stApp {{
        background:
            linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)),
            url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Force ALL text visible on dark */
    html, body, p, span, div, label {{
        color: #F5F5F5 !important;
    }}

    /* Main Heading */
    h1 {{
        color: #FFD700 !important;
        text-shadow: 0 0 25px rgba(255, 215, 0, 0.7);
    }}

    /* Subheadings */
    h2, h3 {{
        color: #FFCC00 !important;
    }}

    /* Glass Card */
    .glass-card {{
        background: rgba(0, 0, 0, 0.55);
        padding: 50px;
        border-radius: 25px;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 35px rgba(255, 215, 0, 0.25);
        text-align: center;
        margin-bottom: 40px;
    }}

    /* Buttons */
    .stButton>button {{
        background-color: #FFD700;
        color: black;
        border-radius: 12px;
        font-weight: bold;
        height: 60px;
        width: 100%;
    }}

    </style>
    """, unsafe_allow_html=True)

# Call background
add_bg()

# ---------------- UI CONTENT ----------------

st.markdown("""
<div class="glass-card">
    <h1>🌙 Ramadan Companion 🌙</h1>
    <h3>رمضان مبارك</h3>
</div>
""", unsafe_allow_html=True)

quotes = [
    "Ramadan is the month of mercy.",
    "The best among you are those who have the best character.",
    "Indeed, with hardship comes ease.",
    "Whoever fasts Ramadan with faith will have past sins forgiven."
]

st.subheader("✨ Daily Reflection")
st.info(random.choice(quotes))

# Buttons Layout
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    if st.button("📊 Dashboard"):
        st.switch_page("pages/1_Dashboard.py")

with col2:
    if st.button("📅 Calendar"):
        st.switch_page("pages/2_Calendar.py")

with col3:
    if st.button("⚙️ Settings"):
        st.switch_page("pages/3_Settings.py")

with col4:
    if st.button("✅ Checklist"):
        st.switch_page("pages/4_Checklist.py")