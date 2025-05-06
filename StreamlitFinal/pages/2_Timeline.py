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
        "text": "Donald Trump is sworn in as President of the United States.  In his inaugural address, he again promises to 'tariff and tax foreign countries to enrich our citizens.'"
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
        "day": 26
      },
      "text": {
        "headline": "Initial Tariff Threats",
        "text": "Trump threatens 25% tariffs on all Colombia imports and other retaliatory measures after President Gustavo Petro’s rejects two U.S. military aircraft carrying migrants to the country, accusing Trump of not treating immigrants with dignity during deportation."
      },
       "media": {
                "url": "https://static.politico.com/09/2b/74bad78e46dfaadde77d25a813f8/trump-46174.jpg",
                "caption": "President Donald Trump speaks to reporters aboard Air Force One on Jan 25",
                "credit": "Politico"
            }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 1,
        "day": 30
      },
      "text": {
        "headline": "Initial Tariff Announcements",
        "text": "Trump signs an executive order to impose tariffs on imports from Mexico, Canada and China — 10% on all imports from China and 25% on imports from Mexico and Canada starting Feb. 4. Trump invoked this power by declaring a national emergency — ostensibly over undocumented immigration and drug trafficking."
      },
       "media": {
                "url": "https://www.usatoday.com/gcdn/authoring/authoring-images/2025/01/31/USAT/78080737007-2196174992.jpg?crop=8255,4645,x0,y429&width=660&height=371&format=pjpg&auto=webp",
                "caption": "Trump imposes 25% tariffs on Canada and Mexico",
                "credit": "USA Today"
            }
    },
   {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 1
      },
      "text": {
        "headline": "First Tariffs Implemented",
        "text": "The U.S. proceeded to implement the previously announced tariffs: 1) 25% on most goods from Canada and Mexico, with Canadian energy exports facing a reduced 10% tariff. 2) Chinese imports saw an increase from 10% to 20%."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 3
      },
      "text": {
        "headline": "Trump Agrees to 30-day Pause on Tariffs to Canada & Mexico",
        "text": "Trump agrees to a 30-day pause on his tariff threats against Mexico and Canada, as both trading partners take steps to appease Trump’s concerns about border security and drug trafficking."
      }
    },
     {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 4
      },
      "text": {
        "headline": "Tariffs on China Go Into Effect",
        "text": "Trump proceeded to implement the previously announced tariffs on China. Chinese imports saw an increase from 10% to 20%. China retaliated the same day with a flurry of countermeasures, including sweeping new duties on a variety of American goods and an anti-monopoly investigation into Google."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 10
      },
      "text": {
        "headline": "Plans to Increase Steel and Aluminum Tariffs Announced",
        "text": "Trump announces plans to increase Steel and Aluminum tariffs starting March 12. He removes the exemptions from his 2018 tariffs on steel, meaning that all steel imports will be taxed at a minimum of 25%, and also raises his 2018 aluminum tariffs from 10% to 25%."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 13
      },
      "text": {
        "headline": "Reciprocal Tariff Plan Announced",
        "text": "Trump announces a plan for “reciprocal” tariffs — promising to increase U.S. tariffs to match the tax rates that countries worldwide charge on imports 'for purposes of fairness.'"
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 25
      },
      "text": {
        "headline": "Executive Order on Copper to Commerce Department",
        "text": "Trump signs an executive order instructing the Commerce Department to consider whether a tariff on imported copper is needed to protect national security. He cites the material’s use in U.S. defense, infrastructure and emerging technologies.'"
      }
    },
   {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 1
      },
      "text": {
        "headline": "Executive Order on Timber to Commerce Department",
        "text": "Trump signs an additional executive order instructing the Commerce Department to consider whether tariffs on lumber and timber are also needed to protect national security, arguing that the construction industry and military depend on a strong supply of wooden products in the U.S."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 2
      },
      "text": {
        "headline": "Liberation Day",
        "text": "President Trump declared April 2 as Liberation Day, introducing a 10% universal tariff on all imports, effective April 5. Additionally, higher tariffs ranging from 11% to 50% were announced for 57 countries, based on the principle of reciprocal trade practices."
      }
    },
   {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 4
      },
      "text": {
        "headline": "Canada Energy Tariff",
        "text": "Trump’s 25% tariffs on imports from Canada and Mexico go into effect, though he limits the levy to 10% on Canadian energy. He also doubles the tariff on all Chinese imports to 20%. Following discussions with Canadian Prime Minister Justin Trudeau and Mexican President Claudia Sheinbaum, the administration agreed to a one-month pause on the implementation of these tariffs, contingent upon enhanced border enforcement measures by both countries."
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
        "month": 3,
        "day": 5
      },
      "text": {
        "headline": "One-Month Exemption for Automakers",
        "text": "Trump grants a one-month exemption on his new tariffs impacting goods from Mexico and Canada for U.S. automakers. The pause arrives after the president spoke with leaders of the “Big 3” automakers — Ford, General Motors and Stellantis."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 6
      },
      "text": {
        "headline": "Trump Extends Postponing of Tariffs",
        "text": "In a wider extension, Trump postpones 25% tariffs on many imports from Mexico and some imports from Canada for a month."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 10
      },
      "text": {
        "headline": "China’s Retaliatory Tariffs Take Effect",
        "text": "China’s retaliatory 15% tariffs on key American farm products — including chicken, pork, soybeans and beef — take effect. Goods already in transit are set to be exempt through April 12, per China’s Commerce Ministry previous announcement."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 12
      },
      "text": {
        "headline": "Trump's Steel & Aluminum Tariffs Take Effect",
        "text": "Trump’s new tariffs on all steel and aluminum imports go into effect. Both metals are now taxed at 25% across the board.The European Union takes retaliatory trade action promising new duties on U.S. industrial and farm products. The measures will cover goods from the United States worth some 26 billion euros ($28 billion), and not just steel and aluminum products, but also textiles, home appliances and agricultural goods."
      }
    },
     {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 13
      },
      "text": {
        "headline": "Trump's Threatens More EU Tariffs",
        "text": "Trump threatens a 200% tariff on European wine, Champagne and spirits if the European Union goes forward with its previously-announced plans for a 50% tariff on American whiskey."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 24
      },
      "text": {
        "headline": "Venezuela Oil & Gas Tariff",
        "text": "Trump says he will place a 25% tariff on all imports from any country that buys oil or gas from Venezuela, in addition to imposing new tariffs on the South American country itself, starting April 2."
        "The tariffs would most likely add to the taxes facing China, which in 2023 bought 68% of the oil exported by Venezuela, per the U.S. Energy Information Administration"
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 26
      },
      "text": {
        "headline": "Auto Tariffs",
        "text": "Trump says he is placing 25% tariffs on auto imports. These auto imports will start being collected April 3 — beginning with taxes on fully-imported cars. The tariffs are set to then expand to applicable auto parts in the following weeks, through May 3."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 2
      },
      "text": {
        "headline": "Reciprocal Tariff Plan Formalized",
        "text": "Trump announces his long-promised “reciprocal” tariffs — declaring a 10% baseline tax on imports across the board starting April 5, as well as higher rates for dozens of nations that run trade surpluses with the U.S. to take effect April 9."
        "Among those steeper levies, Trump says the U.S. will now charge a 34% tax on imports from China, a 20% tax on imports from the European Union, 25% on South Korea, 24% on Japan and 32% on Taiwan. "
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 3
      },
      "text": {
        "headline": "Auto Tariffs Start",
        "text": "Trump’s previously-announced auto tariffs begin. Prime Minister Mark Carney says that Canada will match the 25% levies with a tariff on vehicles imported from the U.S."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 4
      },
      "text": {
        "headline": "China Responds with 34% Tariff",
        "text": "China announces plans to impose a 34% tariff on imports of all U.S. products beginning April 10, matching Trump’s new “reciprocal” tariff on Chinese goods, as part of a flurry of retaliatory measures."
        "The Commerce Ministry in Beijing says it will also impose more export controls on rare earths, which are materials used in high-tech products like computer chips and electric vehicle batteries. And the government adds 27 firms to lists of companies subject to trade sanctions or export controls."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 9
      },
      "text": {
        "headline": "90 Day Suspension of Higher Tariffs",
        "text": "Trump’s higher “reciprocal” rates go into effect, hiking taxes on imports from dozens of countries just after midnight. But hours later, the administration suspended the implementation of the higher tariffs (above the universal 10%) for 90 days for all countries except China (whose tariffs are now 125%), following concerns over potential economic repercussions."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 10
      },
      "text": {
        "headline": "EU Implements 90 Day Suspension",
        "text": "The EU puts its steel and aluminum tariff retaliation on hold for 90 days, to match Trump’s pause on steeper “reciprocal” levies. European Commission President Ursula von der Leyen says the commission wants to give negotiations with the U.S. a chance — but warns countermeasures will kick in if talks “are not satisfactory.”"
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 11
      },
      "text": {
        "headline": "China Responds: 125% Tariff ",
        "text": "China says it will raise tariffs on U.S. goods from 84% to 125%, in response to Trump’s heightened levies. The new rate is set to begin April 12."
        "Later, the Trump administration unveils that electronics, including smartphones and laptops, will be exempt from so-called “reciprocal” tariffs. "
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 14
      },
      "text": {
        "headline": "Trump Continues China Investigation",
        "text": "The Trump administration also launches investigations into imports of computer chips, chipmaking equipment and pharmaceuticals — signaling next steps toward imposing tariffs on these sectors."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 29
      },
      "text": {
        "headline": "Executive Orders to Relax Auto Tariffs",
        "text": "Trump signs executive orders to relax some of his 25% tariffs on automobiles and auto parts — aimed at easing import taxes for vehicles that are made with foreign parts, but assembled in the U.S."
      }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 4
      },
      "text": {
        "headline": "Trump Threatens Film Tariff",
        "text": "Trump threatens a 100% tariff on foreign-made films, while claiming that the movie industry in the U.S. is dying. It isn’t immediately clear how such a tariff on international productions could be implemented, but Trump says he’s authorized the Commerce Department and the U.S. Trade Representative to “immediately begin the process.”"
      }
    },
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