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
        "headline": "Canada/Mexico Tariff Separation",
        "text": "Updated to separate out 25% tariffs on Canada and Mexico given threats these could begin February 1."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 1,
        "day": 31
      },
      "text": {
        "headline": "Analysis of 25% Tariffs",
        "text": "Additional analysis of proposed 25% tariffs on Canada and Mexico."
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
        "text": "10% tariff on Canadian energy resources."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 4
      },
      "text": {
        "headline": "Historical Analysis",
        "text": "Distributional and historical analysis of proposed tariffs."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 6
      },
      "text": {
        "headline": "Duty-Free Ended",
        "text": "Revenue effects of ending duty-free de minimis treatment from China."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 10
      },
      "text": {
        "headline": "Export Estimate Update",
        "text": "Estimate of value of US exports targeted by China\u2019s retaliatory tariffs."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 11
      },
      "text": {
        "headline": "Trump-Biden Revenue Data",
        "text": "New revenue collection data for the Trump-Biden tariffs."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 13
      },
      "text": {
        "headline": "Expanded Steel Tariffs",
        "text": "Analysis of expanded steel and aluminum tariffs."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 19
      },
      "text": {
        "headline": "Trade War Details",
        "text": "Details on 2025 trade war timeline and Trump's auto, steel, and aluminum tariffs."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 27
      },
      "text": {
        "headline": "EU & China Tariff Update",
        "text": "25% tariff on EU imports and increased China tariffs modeled with new economic data."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 3
      },
      "text": {
        "headline": "Lumber & Agriculture",
        "text": "Threatened tariffs on lumber and agriculture added."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 4
      },
      "text": {
        "headline": "Tariffs on Major Partners",
        "text": "Trump imposes new tariffs on Canada, Mexico, and China."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 7
      },
      "text": {
        "headline": "Revenue Estimate Update",
        "text": "Updates on revenue estimates for tariffs on Canada, Mexico, and China."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 12
      },
      "text": {
        "headline": "IEEPA Tariff Forecast",
        "text": "Revenue/economic estimates for IEEPA tariffs and Section 232."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 21
      },
      "text": {
        "headline": "EU Retaliation Update",
        "text": "Timeline for EU retaliation against US Section 232 tariffs."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 25
      },
      "text": {
        "headline": "Venezuela Tariff Threat",
        "text": "New 'secondary' tariff threat on Venezuela and nations that import its oil or gas."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 1
      },
      "text": {
        "headline": "Auto Tariff Modeling",
        "text": "New Section 232 auto tariff modeling and Venezuelan import tariffs."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 3
      },
      "text": {
        "headline": "Exemption List",
        "text": "Exemption list released for April 2 universal tariffs."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 3
      },
      "text": {
        "headline": "April 2 Tariff Details",
        "text": "Details of April 2 tariffs and updated auto/steel/aluminum measures."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 4
      },
      "text": {
        "headline": "China & Canada Retaliation",
        "text": "Includes retaliatory tariffs by China and Canada."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 9
      },
      "text": {
        "headline": "China Tariffs Increased",
        "text": "50% tariff on all Chinese imports added."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 10
      },
      "text": {
        "headline": "Reciprocal Tariffs Paused",
        "text": "90-day pause of reciprocal tariffs and 125% China tariff increase."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 11
      },
      "text": {
        "headline": "New China Chart",
        "text": "Weighted average tariff chart updated; China\u2019s retaliatory rate incorporated."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 18
      },
      "text": {
        "headline": "Electronics Exemption",
        "text": "New exemption for electronics imports from 'reciprocal' tariffs."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 5,
        "day": 5
      },
      "text": {
        "headline": "Stacking Order Rule",
        "text": "Executive order limits stacking of Section 232 and IEEPA fentanyl tariffs on Canada/Mexico."
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