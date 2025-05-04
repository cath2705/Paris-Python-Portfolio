import streamlit as st

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random #this will be used to generate random fun facts

# Set the title
st.title("🐧 Penguin Data Explorer")

st.write("This interactive app allows users to learn more about penguins by filtering through species and islands. Additionally, if users click the button they can see a fun fact! ")

# Load the dataset
CSV_PATH = "data/penguins.csv"

@st.cache_data(ttl=0)
def load_data():
    return pd.read_csv(CSV_PATH)

df = load_data()



#csv_path = "data/penguins.csv"  
#@st.cache_data(ttl=0)
#def load_data():
#    return pd.read_csv("data/penguins.csv")

#df = load_data()

if st.checkbox("Show Raw Data"): # Creates a checkbox in the app, that if clicked will display the FULL dataset
    st.write(df)


st.sidebar.header("Filter Penguins") # adds a section in the sidebar for filters
species = st.sidebar.multiselect("Select Species", df["species"].unique(), default=df["species"].unique()) # finds the uniqu species in the dataset  (ie Adelie) and creates dropdown menu to select multiple species and islands
island = st.sidebar.multiselect("Select Island", df["island"].unique(), default=df["island"].unique()) #

# Filter data
filtered_df = df[(df["species"].isin(species)) & (df["island"].isin(island))]

# Display filtered data
st.subheader("Filtered Data")
st.write(filtered_df)
# this all adds a subheading before shwoing the table and then displays the filtered dataset in a atbel format

# Add a fun fact button
if st.button("🐧 Fun Penguin Fact!"):
    facts = [
        "Penguins can't fly, but they can swim at speeds of up to 22 mph!",
        "There are 18 species of penguins worldwide.",
        "Penguins have a special gland that filters salt from seawater.",
        "Emperor penguins can dive deeper than 500 meters!",
    ]
    st.success(random.choice(facts))
    # this creates a button that when clicked shows a random fun fact about penguins chosen from the list