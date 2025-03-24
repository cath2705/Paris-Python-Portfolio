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
🔗 [View Basic Penguins Streamlit App](https://github.com/cath2705/Paris-Python-Portfolio/blob/main/basic_streamlit_app/main.py)

📄 Project Description
In this project, I used Streamlit to create an interactive data exploration app for the Palmer Penguins dataset. This app leverages Streamlit’s UI components to allow users to filter, visualize, and analyze penguin data dynamically — right from the browser.

### This project specfically 
- Starts with a welcoming title and provides an easy-to-use interface with sidebar filters and interactive plots.
- Uses st.sidebar.multiselect() to create multi-selection dropdowns for filtering species and islands.
- Dynamically pulls unique species and islands using .unique() to make the filter options responsive to the data.
- Applies df["species"].isin(species) to filter the dataset based on the user’s selection in real-time.
- Implements a st.checkbox("Show Raw Data") to toggle display of the raw DataFrame.
- Includes a st.button() labeled for fun — when clicked, it uses random.choice(facts) to display a random penguin fact with st.success(), adding a fun, user-friendly element to the app.

### 💼 This project highlights my ability to:
- Build and deploy interactive web apps using Streamlit
- Work with pandas and data filtering techniques
- Write clean and modular Python code
- Integrate data science with user-friendly interfaces
- Add playful, engaging features to enhance UX

