About my Basic Penguins Streamlit App!

I used Streamlit to create an interactive data exploration app for the Palmer Penguins dataset. This app leverages Streamlit’s interactive components to allow users to filter, visualize, and analyze penguin data dynamically.

The app starts with a welcoming title and provides an easy-to-use interface with sidebar filters and interactive plots.
I used st.sidebar.multiselect() to create multi-selection dropdowns for users to filter data and I used .unique() to extract unique species and islands dynamically.
By incoperating def["species"].isin(species) the app filters the dataset based on user selection.

By using the st.checkbox("Show Raw Data") command, I created a checkbox that users can click to toggle raw data on and off. Users can also filter the data by species using the sidebar options (which also allows for real-time data exploration). 

By using st.button() I creates a button that, when clicked, executes code.
By using random.choice(facts) the app will select and display a random fact from a predefined list.
By using st.success() renders the selected fact with a highlighted success message.
All this comes toegther so that when users click the fun fact button, users learn random facts, adding a fun touch to the app. 
