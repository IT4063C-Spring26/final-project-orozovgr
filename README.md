# Checkpoint 1: Project Idea and Datasets

## 📌 Topic

**Physical Activity, Mental Health, and Academic Performance Among College Students**

Maintaining a healthy lifestyle is essential for students’ physical health, mental well-being, and academic success. However, many college students struggle to balance academic responsibilities with exercise, sleep, and stress management. This often leads to increased stress levels and decreased academic performance.

Understanding how physical activity and lifestyle habits impact student well-being is important for universities aiming to improve student support systems, reduce burnout, and enhance academic outcomes.

---

## ❓ Project Questions

1. How does physical activity affect students’ stress levels?  
2. Is there a relationship between lifestyle habits (sleep, exercise) and academic performance?  
3. What factors contribute most to student stress?  

---

## 📊 What an Answer Could Look Like

- Bar charts showing stress levels across different activity levels  
- Scatter plots comparing physical activity with academic performance (GPA)  
- Visualizations showing relationships between sleep, stress, and productivity  
- Summary insights identifying key factors affecting student well-being  

---

## 📁 Data Sources

### 1. Student Lifestyle Dataset (CSV File)
- **Source:** Kaggle  
- **Type:** CSV  
- **Content:** Includes physical activity, sleep, study hours, stress levels, and GPA  
- **Use:** Main dataset to analyze relationships between activity, stress, and academic performance  

---

### 2. Mental Health & Physical Activity Dataset (CSV File)
- **Source:** Kaggle  
- **Type:** CSV  
- **Content:** Includes steps, exercise frequency, sleep, and mental health indicators  
- **Use:** Helps analyze how physical activity affects mental health  

---

### 3. Student Stress Dataset (CSV File)
- **Source:** Kaggle  
- **Type:** CSV  
- **Content:** Includes stress levels, academic pressure, and lifestyle factors  
- **Use:** Used to analyze stress and its relationship with academic performance  

---

### 4. Public API (API)
- **Source:** https://api.publicapis.org  
- **Type:** API (JSON)  
- **Content:** Sample API data  
- **Use:** Demonstrates integration of API data into the project  

---

## 🔗 Data Integration Plan

### Common Variables
- Activity level (exercise, steps, frequency)  
- Stress levels  
- Lifestyle habits (sleep, study hours)  

### Approach

1. Compare datasets using shared variables such as activity and stress  
2. Normalize variables where needed (e.g., activity frequency, stress scale)  
3. Identify relationships between:
   - Physical activity and stress  
   - Lifestyle habits and academic performance  
   - Stress and academic outcomes  

---

## 💻 Data Import (Implementation)

```python
import pandas as pd
import requests

# Load datasets
lifestyle_df = pd.read_csv("assets/lifestyle.csv")
mental_df = pd.read_csv("assets/mental_health.csv")
stress_df = pd.read_csv("assets/stress.csv")

# Preview data
print(lifestyle_df.head())
print(mental_df.head())
print(stress_df.head())

# API request
response = requests.get("https://api.publicapis.org/entries")
api_data = response.json()

print("API data loaded:", list(api_data.keys()))


🎯 Project Design
Scope

This project focuses on undergraduate students and examines how their lifestyle habits—such as physical activity, sleep, and study patterns—affect their mental health and academic performance.

Objectives
Identify patterns in student physical activity and lifestyle habits
Analyze how these factors influence stress levels
Explore relationships between stress and academic performance
📈 Vision of an Answer
Clear visualizations showing relationships between activity, stress, and GPA
Insights into which lifestyle factors most impact student well-being
Data-driven recommendations to help improve student health and academic success