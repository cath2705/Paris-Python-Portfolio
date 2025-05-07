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
st.image("StreamlitFinal/images/trump1.png", caption="Source: BBC")

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

---
                        """)


# Create average column
df["Average_Tariff_Rate"] = (df["Old_Tariff_Rate"] + df["New_Tarriff_Rate"]) / 2

# Custom hover text for average
df["Avg_Hover"] = df.apply(
    lambda row: f"The average U.S. tariff rate for {row['Country']} is {row['Average_Tariff_Rate']:.1f}%.",
    axis=1
)

# making map with averages
st.markdown("<h3 style='text-align: center;'>📊 Average Tariff Rate Map</h3>", unsafe_allow_html=True)

st.markdown(
    """
This interactive map will help you better understand the aforementioned average effective U.S. tariff rate (27% globally) on a country-by-country basis. It’s a hover map: simply move your mouse over any country to see the average effective tariff rate that the United States has imposed on that nation.

Please note that this map reflects **average** effective tariff rates of each country. This is important because, during the Trump administration's second term, tariffs were frequently adjusted—some were increased, then quickly withdrawn, as shown in the tariff timeline on the previous page. As a result, rather than displaying a real-time tariff rate (which may differ at this exact moment), the map presents an average rate to give a more stable and meaningful view of U.S. trade policy over time.
    """) 
# explaining how to use tool 
st.markdown(
    "**How to Use This Tool**"
)

st.markdown("""
- Use your mouse to zoom, pan, and explore both maps.
- Hover over any country to view the specific average tariff rate the U.S. has imposed on that nation.

**Color Scale Guide:**
- Dark blue indicates the highest tariff intensity
- Dark red indicates the lowest tariff intensity

This tool is designed to help users **quickly understand** which regions were most affected.      
            
            """)

#creating map
fig_avg = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="Average_Tariff_Rate",
    color_continuous_scale="RdBu",  # Red-Blue diverging scale
    title="Average Tariff Rate by Country",
    width=1000,
    height=600
)
#adding hover effect
fig_avg.update_traces(
    hovertemplate="<b>%{customdata[0]}</b><br><br>%{customdata[1]}<extra></extra>",
    customdata=df[["Country", "Avg_Hover"]]
)

fig_avg.update_coloraxes(colorbar_title="Average Tariff Rate")

st.plotly_chart(fig_avg)

st.markdown("""
        Note: This map is current as of **May 6th,** but developments may have occurred since then. **Be sure to consult multiple sources for the most up-to-date information.** """)

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

st.markdown("""
            ---
                        """)


with st.expander("Curious About Tariffs at a Specific Point in Time? 👉"):
        st.markdown("""

                    Averages are helpful—but what if you want to see how Trump-era tariffs looked at a **particular** moment? Great question! If you're interested in how U.S. effective tariff rates evolved, especially during key policy shifts, you're in luck.

                    
                    One of the most important dates to focus on is **April 9th.** As noted in the timeline, on this day President Trump implemented a **temporary 90-day freeze on all tariffs,** except those targeting China.
                  
                    To understand the impact of this freeze, you can compare **two maps:** one showing tariff rates **before April 9th** and one showing them **after.** This will help illustrate the dramatic shift in tariff intensity that **would have remained in effect if not for the pause.**

                    ---
                    
                    - The **first map** shows **Old Tariff Rates** (before April 9th, or pre-freeze)
                    - The **second map** shows **New Tariff Rates** (after April 9th, or post-freeze)
                     
                    **Darker colors** indicate **higher tariff intensities**. You can:
                    - **Zoom**, pan, and explore both maps.
                    - **Hover over any country** to see the specific tariff rate the US imposed on that country

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
        
        st.subheader("Old Tariff Rate (Pre-April 9th) Map")
        st.plotly_chart(fig_old,)
        
        # NEW Tariff Map
        with col2:
            fig_new = px.choropleth(
            df,
            locations="Country",
            locationmode="country names",
            color="New_Tarriff_Rate",  # Spelling intentional
            hover_name="Country",
            hover_data={"New_Hover": True},
            color_continuous_scale="Reds",
            title="New Tariff Intensity by Country",
            width=1000,
            height=600
        )
            
        fig_new.update_traces(
             hovertemplate="<b>%{customdata[0]}</b><br><br>%{customdata[1]}<extra></extra>",
             customdata=df[["Country", "New_Hover"]]
        )
        
        fig_new.update_coloraxes(colorbar_title="New Tariff Rate")
        
        st.subheader("New Tariff Rate Map (Post-April 9th)")
        st.plotly_chart(fig_new)
        
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
        # explaining insights from map
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