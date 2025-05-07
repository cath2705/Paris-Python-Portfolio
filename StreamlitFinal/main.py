# main.py
import streamlit as st

st.set_page_config(page_title="Trump Tariff Explorer", layout="wide")

st.title("🇺🇸 Trump-Era Tariff Explorer")
st.markdown("""
Welcome to the interactive app that explores the global impact of U.S. tariffs implemented during the Trump administration.
Use the sidebar to navigate between pages:
- 📊 Overview & Visuals
- 📅 Timeline
- 🌍 Global Tariff Map
- 🧮 Tariff Calculator
""")

import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("StreamlitFinal/data/v3.csv")

# --- User Input (shared for both tariffs) ---
st.header("💼 Tariff Calculator (Old vs. New)")
country = st.selectbox("Select manufacturing country:", df["Country"])
price = st.number_input("Original product price ($):", min_value=0.0)

# --- Get tariff rates ---
old_tariff = df.loc[df["Country"] == country, "Old_Tariff_Rate"].values[0]
new_tariff = df.loc[df["Country"] == country, "New_Tarriff_Rate"].values[0]

# --- Calculate prices ---
old_price = price * (1 + old_tariff / 100)
new_price = price * (1 + new_tariff / 100)

# --- Layout: side-by-side results ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🕰️ Pre April 9th Tariff")
    st.success(f"A product made in {country} used to cost **${old_price:.2f}** due to a {old_tariff}% tariff.")

with col2:
    st.subheader("❄️ Post April 9th Tariff Freeze")
    st.success(f"A product made in {country} now costs **${new_price:.2f}** due to a {new_tariff}% tariff.")

# --- Source ---
st.markdown(
    """
    <div style='text-align: center; margin-top: 30px;'>
        <a href="https://www.theguardian.com/us-news/2025/apr/09/trump-tariffs-list-pause" target="_blank">
            <u>Source of Tool Percentages</u>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)