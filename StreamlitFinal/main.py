# main.py
import streamlit as st

st.set_page_config(page_title="Trump Tariff Explorer", layout="wide")

st.title("🇺🇸 Welcome to Trump-Era Tariff Explorer 🇺🇸", layout="centered")
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