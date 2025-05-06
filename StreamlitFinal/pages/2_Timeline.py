import streamlit as st
from streamlit_timeline import timeline
import json

st.set_page_config(page_title="Tariff Timeline", layout="centered")
st.title("📅 Interactive Tariff Policy Timeline")
st.markdown("Explore key moments in global tariff policy with this interactive timeline.")

#text explaining the app 
st.markdown("""
Purpose  
This timeline allows you to **visually explore the evolution of major U.S. tariff policies**, especially under the 2025 Trump administration.  
It’s perfect for understanding when and how key decisions were made — including executive orders, retaliatory tariffs, and international responses.

How to Use  
- Tap through the timeline to view an event.  
- Use the arrows or scroll bar to **move through time**.  
- Read summaries of each event, including **tariff increases, policy changes, and exemptions**.  

The Timeline Will Then:  
🗓️ Show you **what happened**, **when**, and **why it matters**  
📌 Highlight key moments like **Trump’s inauguration** and **China retaliation policies**  
🔍 Help you **trace escalation patterns** in the global trade landscape  
🎯 Let you focus on **policy progression** without reading dense government reports
            
 ---

""")

# 🔧 Inject custom CSS to color the bottom timeline bar and axis text
st.markdown("""
    <style>
    .tl-timeaxis {
        background-color: #ffeaea !important;
    }
    .tl-timeaxis-tick,
    .tl-timeaxis-text {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# Your manually created timeline data
data = {
    "title": {
        "text": {
            "headline": "Tariff Policy Timeline 2025"
        }
    },

  "events": [
    {
      "start_date": {
        "year": 2025,
        "month": 1,
        "day": 20
      },
      "text": {
        "headline": "Trump Inaugurated",
        "text": "Donald Trump is sworn in as President of the United States."
      },
     
      "media": {
                "url": "https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2194365306.jpg?c=16x9&q=w_1280,c_fill",
                "caption": "Trump being sworn in",
                "credit": "CNN"
            }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 1,
        "day": 23
      },
      "text": {
        "headline": "Initial Tariff Announcements and Temporary Pauses",
        "text": "President Trump signed executive orders imposing a 25% tariff on all imports from Canada and Mexico, and a 10% tariff on imports from China, citing concerns over illegal immigration and drug trafficking."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 1
      },
      "text": {
        "headline": "Canada Energy Tariff",
        "text": "10% tariff on Canadian energy resources.  Following discussions with Canadian Prime Minister Justin Trudeau and Mexican President Claudia Sheinbaum, the administration agreed to a one-month pause on the implementation of these tariffs, contingent upon enhanced border enforcement measures by both countries."
      },
      "media": {
                "url": "https://images.wsj.net/im-23074905?width=700&height=467",
                "caption": "Ontario’s Doug Ford wearing Cananda not for sale hat",
                "credit": "WSJ"
            }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 4
      },
      "text": {
        "headline": "Tariffs Implemented",
        "text": "The U.S. proceeded to implement the previously announced tariffs: 1) 25% on most goods from Canada and Mexico, with Canadian energy exports facing a reduced 10% tariff. 2) Chinese imports saw an increase from 10% to 20%."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 2
      },
      "text": {
        "headline": "Liberation Day and Introduction of Reciprocal Tariffs",
        "text": "President Trump declared April 2 as Liberation Day, introducing a 10% universal tariff on all imports, effective April 5. Additionally, higher tariffs ranging from 11% to 50% were announced for 57 countries, based on the principle of reciprocal trade practices."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 9
      },
      "text": {
        "headline": " Temporary Suspension of Higher Tariffs",
        "text": "The administration suspended the implementation of the higher tariffs (above the universal 10%) for 90 days for all countries except China, following concerns over potential economic repercussions."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 10
      },
      "text": {
        "headline": "Supply Chain Disruptions Begin",
        "text": "The increased tariffs led to significant disruptions in supply chains, particularly affecting imports from China. Retail experts warned of impending shortages and price increases for various consumer goods, including electronics and clothing."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 30
      },
      "text": {
        "headline": "Presidential Remarks on Consumer Goods",
        "text": "President Trump downplayed concerns over product shortages, suggesting that Americans could manage with fewer imported goods, specifically mentioning that children might have two dolls instead of 30."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 2
      },
      "text": {
        "headline": "Closure of De Minimis Exemption for Chinese Imports",
        "text": "The U.S. closed the de minimis exemption for Chinese imports, which previously allowed goods valued under $800 to enter the country duty-free. This move aimed to further restrict low-cost imports from China and encourage domestic manufacturing."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 5
      },
      "text": {
        "headline": "Regional Responses and Economic Impactst",
        "text": "Governors from six Northeastern U.S. states initiated efforts to strengthen economic ties with Canadian provinces, seeking to mitigate the adverse effects of the tariffs on regional economies. Retailers and consumers continued to experience the consequences of the tariffs, with reports of empty shelves and increased prices for various goods."
      }
    }
  ]
}

# Render the timeline
timeline(data, height=600,)

#adding source for the timeline
st.markdown(
    """
    <div style='text-align: center;'>
        <a href="https://taxfoundation.org/research/all/federal/trump-tariffs-trade-war/#timeline" target="_blank">
            <u>Source for Timeline Information </u>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# 🔧 Inject custom CSS to color the bottom timeline bar and axis text
#    <style>
#    .tl-timeaxis {
 #       background-color: #ffeaea !important;
  #  }
   # .tl-timeaxis-tick,
    #.tl-timeaxis-text {
     #   color: black !important;
    #}
    #</style>
#""", unsafe_allow_html=True)

# Your manually created timeline data
#data = {
 #   "title": {
  #      "text": {
 #           "headline": "Tariff Policy Timeline"
 #       }
 #   },
 #   "events": [
 #       {
 #           "start_date": {"year": 2018, "month": 3},
 #           "text": {
 #               "headline": "Steel & Aluminum Tariffs",
  #              "text": "Trump announces tariffs of 25% on steel and 10% on aluminum imports from all countries."
  #          },
  #          "background": {
  #              "color": "#ffeaea"
  #          },
  #          "media": {
  #              "url": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Steel_mill.jpg",
   #             "caption": "Steel Production",
   #             "credit": "Wikimedia Commons"
   #         }
    #    },
     #   {
      #      "start_date": {"year": 2018, "month": 7},
      #      "text": {
       #         "headline": "First China Tariffs",
        #        "text": "First round of tariffs on $34 billion worth of Chinese goods."
         #   },
         #   "background": {
          #      "color": "#eaffea"
      #      }
       # }
    #]
#}

# Render the timeline
#timeline(data, height=600)

#with st.expander("📌 March 2018 – Steel & Aluminum Tariffs"):
#    st.write("Trump announces tariffs of 25% on steel and 10% on aluminum imports from all countries.")
##
#with st.expander("📌 July 2018 – First China Tariffs"):
#st.write("First round of tariffs on $34 billion worth of Chinese goods.")