import streamlit as st
from streamlit_timeline import timeline
import json

st.set_page_config(page_title="Tariff Timeline", layout="centered")

st.title("📅 Interactive Tariff Policy Timeline")
st.markdown("Explore key moments in global tariff policy with this interactive timeline.")

# Load JSON timeline data
with open("tariff_events.json", "r") as f:
    data = json.load(f)

# Display the interactive timeline
timeline(data, height=600)

{
  "title": {
    "text": {
      "headline": "Tariff Policy Timeline"
    }
  },
  "events": [
    {
      "start_date": {"year": 2018, "month": 3},
      "text": {
        "headline": "Steel & Aluminum Tariffs",
        "text": "Trump announces tariffs of 25% on steel and 10% on aluminum imports from all countries."
      }
    },
    {
      "start_date": {"year": 2018, "month": 7},
      "text": {
        "headline": "First China Tariffs",
        "text": "First round of tariffs on $34 billion worth of Chinese goods."
      }
    }
  ]
}

#with st.expander("📌 March 2018 – Steel & Aluminum Tariffs"):
#    st.write("Trump announces tariffs of 25% on steel and 10% on aluminum imports from all countries.")
##
#with st.expander("📌 July 2018 – First China Tariffs"):
#st.write("First round of tariffs on $34 billion worth of Chinese goods.")