# main.py
import streamlit as st

st.set_page_config(page_title="Trump Tariff Explorer", layout="wide")

st.title("🇺🇸 Welcome to Trump-Era Tariff Explorer 🇺🇸")
st.markdown("""
Welcome!
This interactive app explores the global impact of U.S. tariffs implemented during the Trump administration. Use the navigation to dive deeper into the data and context behind these tariffs through the following pages:
- **Timeline Page** – View an interactive timeline featuring images and descriptions of key tariff-related events.
- **Global Map Page** – Explore a hover map displaying the average effective U.S. tariff rate by country.
- **Tariff Calculator Page** – Enter an item’s price and instantly see how tariffs affect the cost based on the selected country's rate.

Enjoy exploring—and uncover the story behind the numbers!
""")

import streamlit as st
import pandas as pd