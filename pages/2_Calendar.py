import streamlit as st
import requests
import pandas as pd
import datetime
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Ramadan Calendar", layout="centered")

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

    /* Make all normal text white */
    html, body, [class*="css"] {{
        color: white !important;
    }}

    /* Headings gold */
    h1 {{
        color: #FFD700 !important;
        text-shadow: 0 0 20px rgba(255,215,0,0.6);
    }}

    h2, h3 {{
        color: #ffcc00 !important;
    }}

    /* Dataframe styling */
    .stDataFrame {{
        background-color: rgba(255,255,255,0.05);
        color: white;
    }}

    </style>
    """, unsafe_allow_html=True)

# Call background
add_bg()

# ---------------- ORIGINAL CALENDAR LOGIC ----------------

st.title("📅 Ramadan Calendar")

city = st.session_state.get("city", "Gadag")

# Get current Hijri year
hijri_url = f"http://api.aladhan.com/v1/gToH?date={datetime.datetime.now().strftime('%d-%m-%Y')}"
hijri_data = requests.get(hijri_url).json()

hijri_year = hijri_data['data']['hijri']['year']

# Ramadan is month 9
ramadan_url = f"http://api.aladhan.com/v1/hijriCalendarByCity?city={city}&country=India&method=1&month=9&year={hijri_year}"

data = requests.get(ramadan_url).json()

calendar_data = []

for day in data['data']:
    calendar_data.append({
        "Hijri Date": day['date']['hijri']['day'],
        "Gregorian Date": day['date']['gregorian']['date'],
        "Fajr": day['timings']['Fajr'],
        "Maghrib": day['timings']['Maghrib']
    })

df = pd.DataFrame(calendar_data)

st.dataframe(df)