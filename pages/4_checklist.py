import streamlit as st
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Ramadan Companion", layout="centered")

# ---------------- BACKGROUND FUNCTION ----------------
def add_bg():
    with open("background.jpg", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background:
            linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)),
            url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* FORCE ALL TEXT WHITE */
    html, body, p, span, div, label {{
        color: #F5F5F5 !important;
    }}

    /* Fix st.write and markdown text */
    .stMarkdown, .stText {{
        color: #F5F5F5 !important;
    }}

    /* Headings Gold */
    h1, h2, h3 {{
        color: #FFD700 !important;
    }}

    /* Checkbox text */
    .stCheckbox label {{
        color: #F5F5F5 !important;
    }}

    /* Slider label */
    .stSlider label {{
        color: #F5F5F5 !important;
    }}

    /* Progress bar color */
    .stProgress > div > div > div {{
        background-color: #FFD700;
    }}

    /* Button styling */
    .stButton>button {{
        background-color: #FFD700;
        color: black;
        border-radius: 8px;
        font-weight: bold;
    }}

    /* Input fields readable */
    input, textarea {{
        color: black !important;
    }}

    </style>
    """, unsafe_allow_html=True)

# Call background
add_bg()

# ---------------- CONTENT ----------------

# 🌟 Do's Section
st.subheader("✅ Do's of Ramadan")
st.markdown("""
- 🕌 Pray all 5 daily prayers on time  
- 📖 Recite and reflect on the Qur’an daily  
- 🤲 Make sincere dua frequently  
- 💖 Practice patience and control anger  
- 🤝 Help others and give charity  
- 🧠 Improve yourself 1% daily  
- 💤 Maintain proper sleep cycle  
""")

st.markdown("---")

# 🚫 Don'ts Section
st.subheader("❌ Don'ts of Ramadan")
st.markdown("""
- 🗣 Avoid gossip, backbiting, and arguments  
- 🍔 Don’t overeat at iftar  
- ⏰ Don’t waste time in excessive scrolling  
- 😠 Avoid anger and harsh speech  
- 💤 Don’t sleep away the whole day  
- 📱 Avoid unnecessary distractions  
""")

st.markdown("---")

# Back Button
if st.button("⬅ Back to Home"):
    st.switch_page("main.py")

st.title("🌙 Ramadan Daily Checklist")
st.markdown("---")

# 🕌 Namaz Tracker
st.subheader("🕌 Namaz Tracker")

fajr = st.checkbox("Fajr")
zohr = st.checkbox("Zohr")
asr = st.checkbox("Asr")
maghrib = st.checkbox("Maghrib")
isha = st.checkbox("Isha + Taraweeh")

namaz_count = sum([fajr, zohr, asr, maghrib, isha])
st.progress(namaz_count / 5)

st.markdown("---")

# 📖 Quran Tracker
st.subheader("📖 Quran Tracker")
pages_read = st.number_input("Pages read today", min_value=0, max_value=50)
st.write(f"You read {pages_read} pages today 📖")

st.markdown("---")

# 📝 1% Improvement Section
st.subheader("📝 1% Daily Improvement")
improvement = st.text_area("What did you improve today?")
st.write("Reflection saved in your heart 🌟")

st.markdown("---")

# 🤲 Dua Section
st.subheader("🤲 Today's Dua")
dua = st.checkbox("Is dua made today?")
if dua:
    st.success("May Allah accept your dua 🤍")

st.markdown("---")

# 💧 Hydration Tracker
st.subheader("💧 Hydration Tracker")
glasses = st.slider("How many glasses of water did you drink?", 0, 12)
st.progress(glasses / 12)