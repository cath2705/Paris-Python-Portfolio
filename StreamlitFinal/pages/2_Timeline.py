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
📌 Highlight key moments like **President Trump's inauguration** and **China retaliation policies**  
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

  "events":[
    {
      "start_date": {
        "year": 2025,
        "month": 1,
        "day": 20
      },
      "text": {
        "headline": "President Trump Inaugurated",
        "text": "President Trump is sworn in as President of the United States.  In his inaugural address, he again promises to 'tariff and tax foreign countries to enrich our citizens.'"
      },
     
      "media": {
                "url": "https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2194365306.jpg?c=16x9&q=w_1280,c_fill",
                "caption": "President Trump being sworn in",
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
        "text": "President Trump threatens 25% tariffs on all Colombia imports and other retaliatory measures after President Gustavo Petro’s rejects two U.S. military aircraft carrying migrants to the country, accusing Trump of not treating immigrants with dignity during deportation."
      },
       "media": {
                "url": "https://static.politico.com/09/2b/74bad78e46dfaadde77d25a813f8/trump-46174.jpg",
                "caption": "President Trump speaks to reporters aboard Air Force One on Jan 25",
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
        "text": "President Trump signs an executive order to impose tariffs on imports from Mexico, Canada and China — 10% on all imports from China and 25% on imports from Mexico and Canada starting Feb. 4. Trump invoked this power by declaring a national emergency — ostensibly over undocumented immigration and drug trafficking."
      },
       "media": {
                "url": "https://www.usatoday.com/gcdn/authoring/authoring-images/2025/01/31/USAT/78080737007-2196174992.jpg?crop=8255,4645,x0,y429&width=660&height=371&format=pjpg&auto=webp",
                "caption": "President Trump imposes 25% tariffs on Canada and Mexico",
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
      },
      "media": {
                "url": "https://www.reuters.com/resizer/v2/DKLCUS74T5ITTMR62K4LAACLVE.jpg?auth=fa11362870879195b427489bd7311733ac3a041861d61e6dce4af94d73e98369&width=1200&quality=80",
                "credit": "Reuters"
            }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 2,
        "day": 3
      },
      "text": {
        "headline": "President Trump agrees to 30-day Pause on Tariffs to Canada & Mexico",
        "text": "President Trump agrees to a 30-day pause on his tariff threats against Mexico and Canada, as both trading partners take steps to appease President Trump’s concerns about border security and drug trafficking."
      },
      "media": {
                "url": "https://dims.apnews.com/dims4/default/3d648a7/2147483647/strip/true/crop/4000x2666+0+0/resize/1440x960!/format/webp/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2F0f%2F9d%2Fd8ddde30dbb0b308bc73ce3954cd%2Ff473f300a90e4c9ca8fcfa0356641384",
                "caption": "Shipping containers at Atlantic Hub container terminal in Halifax, one day ahead of imposed tariffs.",
                "credit": "AP News"
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
        "text": "President Trump proceeded to implement the previously announced tariffs on China. Chinese imports saw an increase from 10% to 20%. China retaliated the same day with a flurry of countermeasures, including sweeping new duties on a variety of American goods and an anti-monopoly investigation into Google."
      },
      "media": {
                "url": "https://dehayf5mhw1h7.cloudfront.net/wp-content/uploads/sites/2103/2024/05/22225433/US-CHINA-AG-TRADE-ORIGINAL-PHOTO.jpeg",
                "credit": "Hoosier Ag Today"
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
        "text": "President Trump announces plans to increase Steel and Aluminum tariffs starting March 12. He removes the exemptions from his 2018 tariffs on steel, meaning that all steel imports will be taxed at a minimum of 25%, and also raises his 2018 aluminum tariffs from 10% to 25%."
      },
      "media": {
                "url": "https://i.guim.co.uk/img/media/f1be0634b211a3e9e0d6b1bd5240712998dd645a/0_0_5315_3547/master/5315.jpg?width=620&dpr=2&s=none&crop=none",
                "caption": "Rolls of steel are seen at a steel market in Fuyang, China",
                "credit": "The Guardian"
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
        "text": "President Trump announces a plan for “reciprocal” tariffs — promising to increase U.S. tariffs to match the tax rates that countries worldwide charge on imports 'for purposes of fairness.'"
      },
      "media": {
                "url": "https://www.reuters.com/resizer/v2/AFT6Z2ETE5JJVC7HUGJ4JRAOAE.jpg?auth=a9f26113c53acce0c4b518deb62432d4d5608acb2eb3a46ae70c9427e1204f0d&width=1920&quality=80",
                "caption": "President Trump holds an executive order about tariffs increase in the Oval Office",
                "credit": "Reuters"
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
        "text": "President Trump signs an executive order instructing the Commerce Department to consider whether a tariff on imported copper is needed to protect national security. He cites the material’s use in U.S. defense, infrastructure and emerging technologies.'"
      },
      "media": {
                "url": "https://smartcdn.gprod.postmedia.digital/financialpost/wp-content/uploads/2025/02/0227-mg-trump.jpg?quality=90&strip=all&w=944&h=708&type=webp&sig=vkEVSyNQy92hp-czlBxCkA",
                "caption": "President Trump signs an executive order in the Oval Office at the White House, directing the Commerce Department to open an investigation into potential tariffs for copper imports.",
                "credit": "Financial Post"
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
        "text": "President Trump signs an additional executive order instructing the Commerce Department to consider whether tariffs on lumber and timber are also needed to protect national security, arguing that the construction industry and military depend on a strong supply of wooden products in the U.S."
      },
      "media": {
                "url": "https://cdn.woodcentral.com.au/wp-content/uploads/2025/02/HTP2P8.jpg",
                "caption": "President Trump signs timber executive order",
                "credit": "Wood Central"
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
      },
      "media": {
                "url": "https://npr.brightspotcdn.com/dims3/default/strip/false/crop/4050x2700+0+0/resize/1600/quality/85/format/webp/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2F97%2F6b%2F028821994853ad08c1f51c3c844f%2Fgettyimages-2207579595.jpg",
                "caption": "President Trump announces reciprocal tariffs during an event in the Rose Garden on Wednesday entitled Make America Wealthy Again.",
                "credit": "NPR"
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
        "text": "President Trump’s 25% tariffs on imports from Canada and Mexico go into effect, though he limits the levy to 10% on Canadian energy. He also doubles the tariff on all Chinese imports to 20%. Following discussions with Canadian Prime Minister Justin Trudeau and Mexican President Claudia Sheinbaum, the administration agreed to a one-month pause on the implementation of these tariffs, contingent upon enhanced border enforcement measures by both countries."
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
        "text": "President Trump grants a one-month exemption on his new tariffs impacting goods from Mexico and Canada for U.S. automakers. The pause arrives after the president spoke with leaders of the “Big 3” automakers — Ford, General Motors and Stellantis."
      },
      "media": {
                "url": "https://image.cnbcfm.com/api/v1/image/108110759-1741116450853-gettyimages-2203287370-dji_20250304100538_0895_d_nnejsdcy.jpeg?v=1741194272&w=1260&h=709&ffmt=webp&vtcrop=y",
                "caption": "In an aerial view, brand new Subaru cars sit in a storage lot at Auto Warehouse Co.",
                "credit": "CNBC"
            }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 6
      },
      "text": {
        "headline": "President Trump Extends Postponing of Tariffs",
        "text": "In a wider extension, President Trump postpones 25% tariffs on many imports from Mexico and some imports from Canada for a month."
      },
      "media": {
                "url": "https://npr.brightspotcdn.com/dims3/default/strip/false/crop/5293x3529+0+0/resize/1600/quality/85/format/webp/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2F13%2F1c%2F32c8ffc04a4fab84d95330315296%2Fgettyimages-2203670416.jpg",
                "caption": "President Trump holds up an executive order after signing it in the Oval Office on March 6, 2025.",
                "credit": "NPR"
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
      },
      "media": {
                "url": "https://www.livemint.com/lm-img/img/2025/03/04/600x338/CHINA-POLITICS-TWO-SESSIONS-151_1741100782830_1741100818703.jpg",
                "caption": "China's President Xi Jinping attends the opening ceremony of the Chinese People's Political Consultative Conference (CPPCC) at the Great Hall of the People in Beijing on March 4, 2025. (AFP)",
                "credit": "Live Mint News"
            }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 12
      },
      "text": {
        "headline": "President Trump's Steel & Aluminum Tariffs Take Effect",
        "text": "President Trump’s new tariffs on all steel and aluminum imports go into effect. Both metals are now taxed at 25% across the board.The European Union takes retaliatory trade action promising new duties on U.S. industrial and farm products. The measures will cover goods from the United States worth some 26 billion euros ($28 billion), and not just steel and aluminum products, but also textiles, home appliances and agricultural goods."
      },
      "media": {
                "url": "https://www.ft.com/__origami/service/image/v2/images/raw/ftcms%3Af5b22a42-c84c-4f11-b415-297c2f6babbb?source=next-article&fit=scale-down&quality=highest&width=700&dpr=2",
                "caption": "President Trump's original announcement of the steel & aluminum tariffs while on board Air Force One",
                "credit": "Financial Times"
            }
    },
     {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 13
      },
      "text": {
        "headline": "President Trump Threatens More EU Tariffs",
        "text": "President Trump threatens a 200% tariff on European wine, Champagne and spirits if the European Union goes forward with its previously-announced plans for a 50% tariff on American whiskey."
      },
      "media": {
                "url": "https://ca-times.brightspotcdn.com/dims4/default/d5504d7/2147483647/strip/true/crop/5697x3798+0+0/resize/1200x800!/format/webp/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F77%2F8a%2Fdc4aada336767253b275f35c7d0b%2F685b9a6751034a6293432f4f76927639",
                "caption": "President Trump, in a social media post, vowed a new escalation in his trade war",
                "credit": "LA Times"
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
        "text": "President Trump says he will place a 25% tariff on all imports from any country that buys oil or gas from Venezuela, in addition to imposing new tariffs on the South American country itself, starting April 2."
        "The tariffs would most likely add to the taxes facing China, which in 2023 bought 68% of the oil exported by Venezuela, per the U.S. Energy Information Administration"
      },
      "media": {
                "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.opb.org%2Farticle%2F2025%2F03%2F24%2Ftrump-says-countries-that-buy-venezuelan-oil-will-face-25-tariff%2F&psig=AOvVaw2ffFoGFIpws1Zq_rPPIRbJ&ust=1746648845201000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCODe05PUj40DFQAAAAAdAAAAABAJ",
                "caption": "President Trump speaks at executive order signing in the East Room of the White House on March 20, 2025",
                "credit": "OPB"
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
        "text": "President Trump says he is placing 25% tariffs on auto imports. These auto imports will start being collected April 3 — beginning with taxes on fully-imported cars. The tariffs are set to then expand to applicable auto parts in the following weeks, through May 3."
      },
      "media": {
                "url": "https://i.abcnewsfe.com/a/376f31c2-23bd-457f-9043-b1865b0e1824/donald-trump-21-rt-gmh-250326_1743025952165_hpMain.jpg?w=1500",
                "caption": "President Trump speaks to the media, explaining auto tariffs, in the Oval Office at the White House in Washington, Mar. 26, 2025",
                "credit": "ABC News"
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
        "text": "President Trump announces his long-promised “reciprocal” tariffs — declaring a 10% baseline tax on imports across the board starting April 5, as well as higher rates for dozens of nations that run trade surpluses with the U.S. to take effect April 9."
        "Among those steeper levies, President Trump says the U.S. will now charge a 34% tax on imports from China, a 20% tax on imports from the European Union, 25% on South Korea, 24% on Japan and 32% on Taiwan. "
      },
      "media": {
                "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fgmk.center%2Fen%2Fnews%2Ftrump-announces-large-scale-reciprocal-tariffs-on-us-imports%2F&psig=AOvVaw3znWcCND4GqCFjlgrLnMA5&ust=1746649440725000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLDArK3Wj40DFQAAAAAdAAAAABAE",
                "caption": "President Trump's Reciprocal Tariffs ",
                "credit": "GMK Center"
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
        "text": "President Trump’s previously-announced auto tariffs begin. Prime Minister Mark Carney says that Canada will match the 25% levies with a tariff on vehicles imported from the U.S."
      },
      "media": {
                "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.nytimes.com%2F2025%2F03%2F26%2Fus%2Ftrump-tariffs-auto-cars.html&psig=AOvVaw2d2Gc9JelvUx0gIhSb6CYX&ust=1746649508869000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMCgwc7Wj40DFQAAAAAdAAAAABAE",
                "credit": "New York Times"
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
        "text": "China announces plans to impose a 34% tariff on imports of all U.S. products beginning April 10, matching President Trump’s new “reciprocal” tariff on Chinese goods, as part of a flurry of retaliatory measures."
        "The Commerce Ministry in Beijing says it will also impose more export controls on rare earths, which are materials used in high-tech products like computer chips and electric vehicle batteries. And the government adds 27 firms to lists of companies subject to trade sanctions or export controls."
      }
      ,
      "media": {
                "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.reddit.com%2Fr%2FDestiny%2Fcomments%2F1jr93dd%2Fchina_retaliates_with_34_tariff_on_all_us_goods%2F&psig=AOvVaw36NiNAqZxR-DgucS944PWU&ust=1746649632269000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIC0uY3Xj40DFQAAAAAdAAAAABAJ",
                "credit": "New York Times"
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
        "text": "President Trump’s higher “reciprocal” rates go into effect, hiking taxes on imports from dozens of countries just after midnight. But hours later, the administration suspended the implementation of the higher tariffs (above the universal 10%) for 90 days for all countries except China (whose tariffs are now 125%), following concerns over potential economic repercussions."
      },
      "media": {
                "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.foxbusiness.com%2Feconomy%2Ftrump-says-hes-raising-china-tariffs-further-pausing-reciprocal-tariffs-others&psig=AOvVaw01_qO6FJF7IFMWTChGeNRm&ust=1746649746125000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNiHtcPXj40DFQAAAAAdAAAAABAJ",
                "credit": "FOX News"
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
        "text": "The EU puts its steel and aluminum tariff retaliation on hold for 90 days, to match President Trump’s pause on steeper “reciprocal” levies. European Commission President Ursula von der Leyen says the commission wants to give negotiations with the U.S. a chance — but warns countermeasures will kick in if talks “are not satisfactory.”"
      },
      "media": {
                "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dagens.com%2Fnews%2Fursula-von-der-leyen-welcomes-trumps-90-day-tariff-suspension-for-eu%2F&psig=AOvVaw2204M_dXcOXzTzPbQlRfus&ust=1746649843297000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIC2ue7Xj40DFQAAAAAdAAAAABAE",
                "caption": "Ursula von der Leyen at the EU headquarters in Brussels on 9 April 2025.",
                "credit": "RFI"
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
        "text": "China says it will raise tariffs on U.S. goods from 84% to 125%, in response to President Trump’s heightened levies. The new rate is set to begin April 12."
        "Later, the Trump administration unveils that electronics, including smartphones and laptops, will be exempt from so-called “reciprocal” tariffs. "
      },
      "media": {
                "url": "https://s.yimg.com/ny/api/res/1.2/5NI0n.vksnmV791wwzxBhQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTcwNTtoPTQ3MA--/https://media.zenfs.com/en/united_press_international_articles_356/3162a449363df0d7606b976727083b41",
                "caption": "China's President Xi Jinping, speaking about relations with the European Union, called for closer cooperation to resist unilateral 'tariff bullying' by President Trump.",
                "credit": "Yahoo! News"
            }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 3,
        "day": 14
      },
      "text": {
        "headline": "President Trump Continues China Investigation",
        "text": "The Trump administration also launches investigations into imports of computer chips, chipmaking equipment and pharmaceuticals — signaling next steps toward imposing tariffs on these sectors."
      },
      "media": {
                "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cbsnews.com%2Fnews%2Fchip-pharmaceutical-imports-probe-trump-administration%2F&psig=AOvVaw0uNCpTic_p1qgTFcBSQ5GP&ust=1746650169582000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLD7k4rZj40DFQAAAAAdAAAAABAE",
                "credit": "CBS News"
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
        "text": "President Trump signs executive orders to relax some of his 25% tariffs on automobiles and auto parts — aimed at easing import taxes for vehicles that are made with foreign parts, but assembled in the U.S."
      },
      "media": {
                "url": "https://d3i6fh83elv35t.cloudfront.net/static/2023/01/2023-01-24T163623Z_1490130142_RC23LT9FF93F_RTRMADP_3_GLOBAL-ECONOMY-PMI-1200x800.jpg",
                "credit": "PBS News"
            }
    },
    {
      "start_date": {
        "year": 2025,
        "month": 4,
        "day": 4
      },
      "text": {
        "headline": "President Trump Threatens Film Tariff",
        "text": "President Trump threatens a 100% tariff on foreign-made films, while claiming that the movie industry in the U.S. is dying. It isn’t immediately clear how such a tariff on international productions could be implemented, but President Trump says he’s authorized the Commerce Department and the U.S. Trade Representative to “immediately begin the process.”"
      },
      "media": {
                "url": "https://bloximages.newyork1.vip.townnews.com/telegraphherald.com/content/tncms/assets/v3/editorial/6/60/6605649c-1cf7-55c4-9e85-3ef0c5c3a756/6818819976f75.image.jpg?resize=1476%2C982",
                "caption": "President Trump speaks to reporters, explaining new film tariff",
                "credit": "Telegraph Herald"
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