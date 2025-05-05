import streamlit as st
import pandas as pd
import plotly.express as px

# fixing layout
st.set_page_config(layout="wide")
# add title 
st.title("🌍 Global Tariff Impact Map")

# Load the dataset
df = pd.read_csv("StreamlitFinal/data/v3.csv")

# Add a news image 
st.image("path/to/your/news_image.jpg", caption="Source: News Outlet", use_column_width=True)

# Add historical and usage context
st.markdown("""
### 📈 Context

In the early part of the second Trump administration (January–April 2025), the average effective U.S. tariff rate surged from **2.5% to an estimated 27%** — the highest level in over a century.

This historic increase was fueled by proposed tariffs on imports from **57 countries**, ranging between **11% and 50%**. These tariffs were scheduled to take effect on **April 9, 2025**, but were later **suspended for 90 days — except for China**, where implementation continued.

The visualizations below compare:
- **Old Tariff Rates** (before April 9th, or pre-freeze)
- **New Tariff Rates** (after April 9th, or post-freeze)

---

### How to Use This Tool

You’ll find **two interactive heat maps** displayed side-by-side:
- The **left map** shows **pre-April 9th (old)** tariff rates.
- The **right map** shows **post-April 9th (new)** tariff rates.

**Darker colors** indicate **higher tariff intensities**. You can:
- **Zoom**, pan, and explore both maps.
- **Hover over any country** to see a detailed breakdown of the U.S. tariff rate imposed on that country and its share of U.S. imports.

This tool is designed to help users **quickly understand** which regions were most affected and how U.S. trade policy shifted during this critical time.
""")

# Custom hover text
df["Old_Hover"] = df.apply(
    lambda row: f"The US has placed a {row['Old_Tariff_Rate']}% tariff rate on {row['Country']}.\n",
    axis=1
)

df["New_Hover"] = df.apply(
    lambda row: f"The US has placed a {row['New_Tarriff_Rate']}% tariff rate on {row['Country']}.\n",
    axis=1
)

# Create columns for side-by-side layout
col1, col2 = st.columns(2)

# OLD Tariff Map 
with col1:
    fig_old = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color="Old_Tariff_Rate",
        hover_name="Country",
        hover_data={"Old_Hover": True},
        color_continuous_scale="Reds",
        title="Old Tariff Intensity by Country",
        width=1000,
        height=600
    )

    fig_old.update_traces(
        hovertemplate="<b>%{customdata[0]}</b><br><br>%{customdata[1]}<extra></extra>",
        customdata=df[["Country", "Old_Hover"]]
    )

    fig_old.update_coloraxes(colorbar_title="Old Tariff Rate")

    st.subheader("Old Tariff Rate Map")
    st.plotly_chart(fig_old, use_container_width=False)

# NEW Tariff Map
with col2:
    fig_new = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color="New_Tarriff_Rate",  # Spelling intentional
        hover_name="Country",
        hover_data={"New_Hover": True},
        color_continuous_scale="Blues",
        title="New Tariff Intensity by Country",
        width=1000,
        height=600
    )

    fig_new.update_traces(
        hovertemplate="<b>%{customdata[0]}</b><br><br>%{customdata[1]}<extra></extra>",
        customdata=df[["Country", "New_Hover"]]
    )

    fig_new.update_coloraxes(colorbar_title="New Tariff Rate")

    st.subheader("New Tariff Rate Map")
    st.plotly_chart(fig_new, use_container_width=False)