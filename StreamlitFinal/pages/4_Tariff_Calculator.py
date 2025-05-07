import streamlit as st
import pandas as pd

# add title
st.title("🧮 Tariff Impact Calculator")

# Add image
st.image("StreamlitFinal/images/make_wealthy1.png", caption="Source: AXIOS",)

#add text
st.markdown(
    "<h3 style='text-align: center;'>Trump’s Tariffs: Who Really Pays the Price?</h3>",
    unsafe_allow_html=True
)

#add text
st.markdown(
    """
    President Trump has stated that the goal of these tariffs is to put pressure on foreign governments and producers that, according to the administration, were engaging in unfair trade practices or flooding U.S. markets with underpriced goods. By imposing additional costs on these imports, the hope was to incentivize fairer trade relationships and create a more level playing field for American businesses.
    """
)

# Add image
st.image("StreamlitFinal/images/Tarriff_Man1.png", caption="Source: AXIOS")

#add text
st.markdown(
    """
    While tariffs are imposed on foreign goods, the cost is often passed on to U.S. importers, retailers, and ultimately, consumers. Because many products sold in the U.S. still come from abroad, American households often experienced higher prices on items ranging from electronics and appliances to clothing and raw materials.

    In some cases, even domestic producers raised their prices, reflecting reduced competition or increased costs for parts and materials they also import. For example, tariffs on steel affected not only foreign producers but also U.S. companies that rely on steel to manufacture goods.
   
      ---         

     """
)

#add text
st.markdown(
    "<h3 style='text-align: center;'>Tariffs Impact Tool</h3>",
    unsafe_allow_html=True
)

# text explaination of the tool
st.markdown("""
 **Purpose**
            
This tool helps you estimate how much more your typical items may cost due to tariffs.  
You don’t need to know the specific tariff rates—just where the product was made.  
We automatically apply the correct tariff percentage based on the country of origin and calculate the final cost for you.

 **How to Use**

1. **Enter the original price** of your product in U.S. dollars.
2. **Select the country** where the product was developed or manufactured.
3. Write the name of the product.
4. **Press Enter.**

**The Tool Will Then:**

- 🔍 Automatically apply the correct tariff rate for that country  
- 💰 Show you the **new total cost** after the tariff  
- ➕ Optionally display the **amount added** due to the tariff  


✅ That’s it!
No need to research tariff rates or do any math — this tool does it all for you.
""")

# Load data once
df = pd.read_csv("StreamlitFinal/data/v3.csv")

# Create two columns
col1, col2 = st.columns(2)

# --- Old Tariff Calculator (Left) ---
with col1:
    st.header("🕰️ Old Tariff Calculator (Pre April 9th)")
    country_old = st.selectbox("Selec manufacturing country (old tariff):", df["Country"], key="country_old")
    price_old = st.number_input("Original product price ($) (old tariff):", min_value=0.0, key="price_old")

    old_tariff_rate = df.loc[df["Country"] == country_old, "Old_Tariff_Rate"].values[0]
    old_price = price_old * (1 + old_tariff_rate / 100)

    st.success(f"A product made in {country_old} used to cost **${old_price:.2f}** due to a {old_tariff_rate}% tariff.")

# --- New Tariff Calculator (Right) ---
with col2:
    st.header("❄️ New Tariff Calculator (Post April 9th Freeze)")
    country = st.selectbox("Select manufacturing country:", df["Country"], key="country_new")
    price = st.number_input("Original product price ($):", min_value=0.0, key="price_new")

    tariff_rate = df.loc[df["Country"] == country, "New_Tarriff_Rate"].values[0]
    new_price = price * (1 + tariff_rate / 100)

    st.success(f"A product made in {country} now costs **${new_price:.2f}** due to a {tariff_rate}% tariff.")

# --- Price Comparison (Bottom) ---
if (
    "country_old" in locals() and
    "country_new" in locals() and
    price_old > 0 and
    price_new > 0 and
    country_old == country_new
):
    price_diff = old_price - new_price
    percent_change = (price_diff / old_price) * 100 if old_price != 0 else 0

    st.markdown("---")
    st.subheader("📊 Price Comparison Summary")
    st.markdown(f"""
    - **Old Tariff Price:** ${old_price:.2f}  
    - **New Tariff Price:** ${new_price:.2f}  
    - **Price Difference:** ${price_diff:.2f}  
    - **Change:** {percent_change:.2f}% {"decrease" if percent_change > 0 else "increase"}
    """)


#adding source
st.markdown(
    """
    <div style='text-align: center;'>
        <a href="https://www.theguardian.com/us-news/2025/apr/09/trump-tariffs-list-pause" target="_blank">
            <u>Source of Tool Percentages </u>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

#adding line break
st.markdown(
    """
      ---         
     """
)

#add text
st.markdown(
    "<h3 style='text-align: center;'>Why This Matters",
    unsafe_allow_html=True
)

# Add image
st.image("StreamlitFinal/images/consume1.png", caption="Source: BCC")

#add text
st.markdown(
    """
Projections of proposed tariffs on tech products reveal significant consequences for U.S. consumers, with sharp increases in retail prices across essential electronics and an estimated 120 billion dollar reduction in consumer **purchasing power.** 
This matters because tariffs, often aimed at protecting domestic industries, **can unintentionally burden everyday consumers—especially** in sectors like technology that touch nearly every aspect of modern life. 
For instance, laptops and tablets would face a 45% price hike, with average costs rising by 357 dollars
and 201 dollars, respectively, while smartphones could go up by 213 dollars. 
Even smaller accessories like headphones and batteries would see noticeable increases. 
These projections show that industry-wide tariffs don’t just affect manufacturers—they ripple through the economy, reducing what consumers can afford, slowing tech adoption, and disproportionately impacting lower- and middle-income households.         

     """
)

# Expandable section for explanation
with st.expander("What Does Purchasing Power Mean👉"):
        st.markdown("""
                    **Purchasing power** refers to the amount of goods or services that a person can buy with a certain amount of money. When prices go up—like in the case of tariffs—your purchasing power goes down because the same amount of money buys you **less** than it did before.
                    
                    For example, if you had 1,000 dollars to spend on tech and laptops used to cost 500 dollars, you could buy two. But if tariffs raise laptop prices to 750 dollar each, now you can only afford one. Your **purchasing power has decreased** even though the amount of money you have hasn’t changed.
                    """)