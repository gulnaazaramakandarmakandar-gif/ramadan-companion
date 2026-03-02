import streamlit as st
import base64
import os

def add_bg():
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "..", "background.jpg")

    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background: 
            linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
            url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Make all text white */
    html, body, [class*="css"] {{
        color: white !important;
    }}

    /* Input label */
    label {{
        color: #FFD700 !important;
        font-weight: bold;
    }}

    /* Button styling */
    .stButton>button {{
        background-color: #FFD700;
        color: black;
        border-radius: 10px;
        font-weight: bold;
    }}

    /* Input box text */
    input {{
        color: black !important;
    }}

    </style>
    """, unsafe_allow_html=True)

add_bg()

city = st.text_input("Enter your city", st.session_state.get("city", "Gadag"))
iftar_offset = st.number_input("Iftar Adjustment (+/-)", value=st.session_state.get("iftar_offset", 0))
sehri_offset = st.number_input("Sehri Adjustment (+/-)", value=st.session_state.get("sehri_offset", 0))

if st.button("Save Settings"):
    st.session_state.city = city
    st.session_state.iftar_offset = iftar_offset
    st.session_state.sehri_offset = sehri_offset
    st.success("Settings Saved Successfully!")