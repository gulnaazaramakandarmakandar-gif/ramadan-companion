import streamlit as st
import requests
import datetime
import random
import base64

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Ramadan Dashboard", layout="centered")

# -------------------- BACKGROUND FUNCTION --------------------
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

    /* All normal text white */
    html, body, [class*="css"] {{
        color: white !important;
    }}

    /* Title gold */
    h1 {{
        color: #FFD700 !important;
        text-shadow: 0 0 20px rgba(255,215,0,0.6);
    }}

    /* Subheaders */
    h2, h3 {{
        color: #ffcc00 !important;
    }}

    /* Buttons */
    .stButton>button {{
        background-color: #FFD700;
        color: black;
        border-radius: 8px;
        font-weight: bold;
    }}

    /* Alert boxes readable */
    .stAlert {{
        color: black !important;
    }}

    </style>
    """, unsafe_allow_html=True)

# Call background
add_bg()

# -------------------- MAIN DASHBOARD --------------------

st.title("🌙 Ramadan Dashboard")

city = st.session_state.get("city", "Gadag")
iftar_offset = st.session_state.get("iftar_offset", 0)
sehri_offset = st.session_state.get("sehri_offset", 0)

url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country=India&method=1"

try:
    data = requests.get(url, timeout=5).json()
except:
    st.error("Unable to fetch prayer timings. Check internet.")
    st.stop()

timings = data['data']['timings']
hijri = data['data']['date']['hijri']

# Roza number
roza_number = int(hijri['day']) - 1
if roza_number <= 0:
    roza_number = 1

st.subheader(f"🌟 {roza_number}th Roza")

maghrib = timings['Maghrib']
fajr = timings['Fajr']

now = datetime.datetime.now()

# -------------------- IFTAR COUNTDOWN --------------------
iftar_hour = int(maghrib.split(":")[0])
iftar_min = int(maghrib.split(":")[1]) + iftar_offset
iftar_target = now.replace(hour=iftar_hour, minute=iftar_min, second=0)

if now > iftar_target:
    iftar_target += datetime.timedelta(days=1)

iftar_remaining = iftar_target - now
st.success(f"Iftar Countdown: {str(iftar_remaining).split('.')[0]}")

# -------------------- SEHRI COUNTDOWN --------------------
sehri_hour = int(fajr.split(":")[0])
sehri_min = int(fajr.split(":")[1]) + sehri_offset
sehri_target = now.replace(hour=sehri_hour, minute=sehri_min, second=0)

if now > sehri_target:
    sehri_target += datetime.timedelta(days=1)

sehri_remaining = sehri_target - now
st.info(f"Sehri Countdown: {str(sehri_remaining).split('.')[0]}")

# -------------------- RAMADAN PROGRESS --------------------
st.subheader("🌙 Ramadan Progress")
st.progress(roza_number / 30)
st.write(f"Day {roza_number} of 30")

# -------------------- DAILY REFLECTION --------------------


# -------------------- EID COUNTDOWN --------------------
eid_date = datetime.date(2026, 3, 20)
today = datetime.date.today()
days_left = (eid_date - today).days

st.subheader("🌙 Eid Countdown")
st.success(f"{days_left} days left until Eid")