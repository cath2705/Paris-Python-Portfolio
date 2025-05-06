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
st.image("StreamlitFinal/images/trump1.png", caption="Source: BCC", use_container_width=True)

# adding link to source
st.markdown(
    """
    <div style='text-align: center;'>
        <a href="https://www.bbc.com/news/articles/c5ypxnnyg7jo" target="_blank">
            <u>Click to read full article</u>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Add historical and usage context
st.markdown(
    "<h3 style='text-align: center;'>In a Nutshell: Trump’s Tariffs</h3>",
    unsafe_allow_html=True
)

st.markdown("""

In the early part of the second Trump administration (January–April 2025), the average effective U.S. tariff rate surged from **2.5% to an estimated 27%** — the highest level in over a century.

This historic increase was fueled by proposed tariffs on imports from **57 countries**, ranging between **11% and 50%**. These tariffs were scheduled to take effect on **April 9, 2025**, but were later **suspended for 90 days — except for China**, where implementation continued.

The visualizations below compare:
- **Old Tariff Rates** (before April 9th, or pre-freeze)
- **New Tariff Rates** (after April 9th, or post-freeze)

---
                        """)

st.markdown(
    "<h3 style='text-align: center;'>How to Use This Tool</h3>",
    unsafe_allow_html=True
)

st.markdown("""
You’ll find **two interactive heat maps** displayed side-by-side:
- The **left map** shows **old (pre-April 9th)** tariff rates.
- The **right map** shows **new (post-April 9th)** tariff rates.

**Darker colors** indicate **higher tariff intensities**. You can:
- **Zoom**, pan, and explore both maps.
- **Hover over any country** to see the specific tariff rate the US imposed on that country

This tool is designed to help users **quickly understand** which regions were most affected.

   ---         
            
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

# adding link to source
st.markdown(
    """
    <div style='text-align: center;'>
        <a href="https://www.theguardian.com/us-news/2025/apr/09/trump-tariffs-list-pause" target="_blank">
            <u>Source of Map Data </u>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    ### 🔍 What’s Really Going On?

    A clear pattern emerges when comparing the pre- and post-April 9th tariffs:

    The new tariff map shows a dramatic reduction or elimination of tariffs for most countries, with China standing out as the sole nation facing a substantial increase. China’s new rate is 125%, represented by the darkest blue. This suggests a deliberate and strategic pivot, concentrating tariff pressure almost exclusively on China while easing trade restrictions elsewhere. 

       ---   

    Even more striking is the **post-freeze uniformity** — nearly **every country except China now faces a flat 10% tariff**. This reset is not based on any specific trade behavior like tariffs, VATs, or digital services taxes. Instead, the new rates are **derived from a formula**:  
    > **Trade deficit ÷ U.S. imports**, with a **minimum tariff of 10%.**

    In short, these rates are mechanically determined by trade aggregates, not policy nuance.

    For example:
    - **Singapore**, a free-trade-oriented nation, and **Brazil**, which uses heavy tariffs and restrictions, both receive the **same 10% tariff** — purely due to their goods trade balances with the U.S.
    - **Vietnam**, a country that has actively sought to align with U.S. policy, also receives no preferential treatment under the new system.

    > 📉 **Exports to the U.S. make up nearly 30% of Vietnam’s GDP.**  
    > Under the proposed formula, Vietnam narrowly avoided a devastating 46% tariff — which could have pushed its economy into recession.  
    > Instead, it will now pay the 10% minimum.

    Meanwhile, even **close U.S. allies** with free trade agreements — like **Australia** and **South Korea** — are affected. Despite having **zero-tariff access** on many exports under past agreements, they now face a **significant shift** in their trade relationships due to the new flat-rate system.

    This reset represents a profound restructuring of U.S. trade policy logic — from politically negotiated rates to formula-driven automation.
    """
)

# adding link to source
st.markdown(
    """
    <div style='text-align: center;'>
        <a href="https://taxfoundation.org/blog/trump-reciprocal-tariffs-calculations/" target="_blank">
            <u>Read More from Tax Foundation </u>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)