import streamlit as st
import pandas as pd

st.title("🧮 Tariff Impact Calculator")

df = pd.read_csv("StreamlitFinal/data/v3.csv")
country = st.selectbox("Select manufacturing country:", df["Country"])
product = st.text_input("Product name:", placeholder="e.g. mascara")
price = st.number_input("Original product price ($):", min_value=0.0)

tariff_rate = df.loc[df["Country"] == country, "New_Tarriff_Rate"].values[0]
new_price = price * (1 + tariff_rate / 100)

st.success(f"{product} made in {country} now costs **${new_price:.2f}** due to a {tariff_rate}% tariff.")
