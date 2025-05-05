import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Global Tariff Impact Map")

df = pd.read_csv("data/Cleaned_Trump_Tariffs.csv")
fig = px.choropleth(df,
                    locations="Country",
                    locationmode="country names",
                    color="New_Tariff_Rate",
                    hover_name="Country",
                    hover_data=["Old_Tariff_Rate", "Share_US_Import"],
                    color_continuous_scale="Reds",
                    title="Tariff Intensity by Country")

st.plotly_chart(fig, use_container_width=True)