 About my Portfolio
 
This repository will serve as a centralized location for all my projects in Elements of Computing II (Spring 2025). I plan to structure my work into separate folders based on project type—whether it's exploratory data analysis (EDA), data visualization, or model development. My goal is to ensure clarity and accessibility for both myself and others reviewing my work.

Looking ahead at this semester, I anticipate making four major updates to my GitHub, each corresponding to key milestones in the course. These updates will showcase my progress, including refining analytical techniques, improving visualization methods, and iterating on models. Additionally, I may include smaller updates such as code optimizations, documentation enhancements, or reflections on my learning process.

## Projects
## Tidy Data Project!
🔗 [View the Tidy Data Project Repository](https://github.com/cath2705/TidyData-Project)

📄 Project Description
This project is based on Hadley Wickham's "Tidy Data" paper and explores the principles of organizing datasets to make analysis easier and more efficient. The project involves:

- Extracting and cleaning data from a combined column
- Separating gender and sport from composite strings
- Removing missing or irrelevant data
- Standardizing sport names and fixing formatting inconsistencies
- The result is a clean, well-structured dataset ready for analysis — where each row is an observation, each column is a variable, and each table contains one type of observational unit.

### This project specfically 
- cleans up the data from a dataset file called olympics_08_medalists.csv
- this dataset shows Olympic medal data from the 2008 Summer Olympics
- after cleaning the data, I create visuals showing distrubtions of medals won across sports and genders :) 

### 💼 This project highlights my ability to:
- Work with real-world messy data
- Apply data wrangling techniques using Python and pandas
- Follow best practices in data cleaning and structure
- It complements my portfolio by demonstrating attention to detail, data intuition, and proficiency in transforming raw datasets into clean, analyzable formats — skills essential for data analysis, machine learning, and reporting workflows.


## Basic Penguins Streamlit App!

📄 Project Description
In this project I I used Streamlit to create an interactive data exploration app for the Palmer Penguins dataset. This app leverages Streamlit’s interactive components to allow users to filter, visualize, and analyze penguin data dynamically.

### This project specfically 
- The app starts with a welcoming title and provides an easy-to-use interface with sidebar filters and interactive plots.
- I used st.sidebar.multiselect() to create multi-selection dropdowns for users to filter data and I used .unique() to extract unique species and islands dynamically.
- By incoperating def["species"].isin(species) the app filters the dataset based on user selection.
- By using the st.checkbox("Show Raw Data") command, I created a checkbox that users can click to toggle raw data on and off.
- Users can also filter the data by species using the sidebar options (which also allows for real-time data exploration).
- By using st.button() I creates a button that, when clicked, executes code. By using random.choice(facts) the app will select and display a random fact from a predefined list. By using st.success() renders the selected fact with a highlighted success message. All this comes toegther so that when users click the fun fact button, users learn random facts, adding a fun touch to the app.
