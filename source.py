#!/usr/bin/env python
# coding: utf-8

# # Physical Activity, Mental Health, and Academic Performance Analysis
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# 
# This project explores how physical activity and lifestyle habits impact college students’ mental health and academic performance. Many students struggle to maintain a healthy balance between academics and personal well-being, which can lead to increased stress and lower academic success.
# 
# Understanding these relationships can help universities design better wellness programs, reduce student stress, and improve overall academic outcomes.

# ## Project Questions
# 
# 1. How does physical activity affect students’ stress levels?  
# 2. Is there a relationship between lifestyle habits (sleep, exercise) and academic performance?  
# 3. What factors contribute most to student stress?  

# ## What Would an Answer Look Like?
# 
# - Bar charts showing levels of stress across different activity levels  
# - Scatter plots comparing physical activity with GPA or performance  
# - Visualizations showing relationships between sleep, stress, and academic success  
# - Summary insights identifying key factors affecting student well-being  

# ## Data Sources
# 
# This project uses 4 datasets:
# 
# 1. **Student Lifestyle Dataset**
#    - Includes physical activity, sleep, study hours, stress levels, and GPA  
# 
# 2. **Mental Health & Physical Activity Dataset**
#    - Includes steps, exercise frequency, and mental health indicators  
# 
# 3. **Student Stress Dataset**
#    - Includes stress levels, academic pressure, and lifestyle factors  
# 
# 4. **Public API Dataset**
#    - Source: https://jsonplaceholder.typicode.com/posts  
#    - Type: JSON API  
#    - Includes sample post data (userId, id, title, body)  
#    - Used to demonstrate API integration by retrieving and processing JSON data  
#   
# 
# These datasets are related through common variables such as activity level, stress, and lifestyle habits, allowing for comparative analysis across datasets.

# ## Approach and Analysis
# 
# 1. Load and clean all datasets  
# 2. Explore key variables such as activity level, stress, and academic performance  
# 3. Compare patterns across datasets  
# 4. Identify correlations between physical activity, stress, and performance  
# 5. Visualize findings using charts and summary statistics  

# In[22]:


get_ipython().system('pip install pandas matplotlib seaborn requests')


# In[23]:


# Start your code here
import pandas as pd
import requests

# Load datasets
lifestyle_df = pd.read_csv("data/Lifestyle.csv")
mental_df = pd.read_csv("data/mentalhealth.csv")
stress_df = pd.read_csv("data/Stress.csv")

# Preview datasets
lifestyle_df.head()


# In[24]:


mental_df.head()
stress_df.head()


# In[25]:


# API integration (working example)
response = requests.get("https://jsonplaceholder.typicode.com/posts")
api_data = response.json()

print("API loaded:", len(api_data), "records")


# ## Exploratory Data Analysis (EDA)
# 
# In this section, we perform exploratory data analysis (EDA) to understand dataset structure, identify patterns, examine relationships between variables, and detect potential data quality issues.

# In[26]:


# Check dataset structure
print("Lifestyle Dataset Info:")
lifestyle_df.info()

print("\nMental Health Dataset Info:")
mental_df.info()

print("\nStress Dataset Info:")
stress_df.info()


# ### Dataset Structure Insights
# 
# The `.info()` function was used to examine the structure of each dataset. This provides information about:
# - Number of rows and columns
# - Data types of each variable
# - Presence of missing values
# 
# From this, we can identify columns that may require data type conversion or further cleaning.

# In[27]:


# Summary statistics
lifestyle_df.describe()


# In[28]:


import matplotlib.pyplot as plt
import seaborn as sns


# ### Stress Levels vs Physical Activity
# 
# This bar chart shows how stress levels vary based on the amount of physical activity. It helps identify whether increased activity is associated with lower stress.

# In[29]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(
    x="Physical_Activity_Hours_Per_Day",
    y="GPA",
    data=lifestyle_df
)
plt.title("Physical Activity vs GPA")
plt.show()


# ### Study Hours vs GPA
# 
# This scatter plot examines the relationship between study time and academic performance.

# In[30]:


sns.scatterplot(
    x="Study_Hours_Per_Day",
    y="GPA",
    data=lifestyle_df
)
plt.title("Study Hours vs GPA")
plt.show()


# ### Sleep Hours vs Stress Levels
# 
# This visualization explores whether sleep duration impacts student stress levels.

# In[31]:


sns.scatterplot(
    x="Sleep_Hours_Per_Day",
    y="Stress_Level",
    data=lifestyle_df
)
plt.title("Sleep vs Stress")
plt.show()


# ### Correlation Heatmap
# 
# This heatmap visualizes relationships between numerical variables and highlights strong correlations.

# In[32]:


corr = lifestyle_df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# ### Additional Dataset Analysis
# 
# We also analyze the mental health and stress datasets to understand their statistical distributions and compare them with the lifestyle dataset.

# In[33]:


mental_df.describe()
stress_df.describe()


# These summaries help identify patterns, ranges, and variability in stress levels, activity frequency, and academic indicators across datasets.

# ### Distribution Analysis
# 
# The `.describe()` function provides statistical summaries such as mean, standard deviation, minimum, and maximum values.
# 
# This helps us understand:
# - The distribution of numerical variables
# - The range of values (e.g., study hours, sleep hours, stress levels)
# - Whether there are unusually high or low values that may indicate outliers

# In[34]:


# Correlation matrix
lifestyle_df.corr(numeric_only=True)


# ### Correlation Analysis
# 
# The correlation matrix shows relationships between numerical variables.
# 
# This helps identify:
# - Positive or negative relationships between variables
# - Potential connections between lifestyle habits and stress
# - Variables that may influence academic performance
# 
# These relationships will be further explored in the visualization section.

# In[35]:


# Check missing values
lifestyle_df.isnull().sum()


# ### Missing Values
# 
# We checked for missing values in the dataset.
# 
# Missing data can affect analysis and model performance. These values will be handled during the data cleaning phase.

# In[36]:


# Check duplicates
lifestyle_df.duplicated().sum()


# ### Duplicate Values
# 
# Duplicate records can lead to biased results. Identifying duplicates helps ensure that the dataset represents unique observations.
# 
# Duplicates will be removed during data cleaning if necessary.

# ### Key Insights from EDA
# 
# - There is a strong positive relationship between study hours and GPA, indicating that increased study time contributes to better academic performance.
# - Physical activity shows a slight negative correlation with stress levels, suggesting that more active students may experience lower stress.
# - Sleep duration appears relatively consistent across students, but lower sleep levels may contribute to higher stress.
# - Social and extracurricular activities vary widely, reflecting different lifestyle balances among students.
# - The dataset contains no significant missing or duplicate values, indicating high data quality.
# - Overall, lifestyle factors such as study time, sleep, and physical activity play a meaningful role in both academic success and stress management.

# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[37]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

