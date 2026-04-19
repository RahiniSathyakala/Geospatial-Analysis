# 🌍 Geospatial Analysis & Interactive Restaurant Map

## 📌 Overview
This project focuses on performing geospatial analysis on a restaurant dataset using location-based features such as latitude and longitude. An interactive map is created to visualize restaurant distribution and explore geographic patterns.

## 🎯 Objective
- Visualize restaurant locations using latitude and longitude  
- Build an interactive map using real-world data  
- Analyze restaurant distribution across cities and countries  
- Study the relationship between location and ratings  

## 🛠️ Tools & Technologies
- Python  
- Pandas  
- Folium  

## 📂 Dataset Details
The dataset contains information about restaurants, including:
- Restaurant Name  
- City  
- Country Code  
- Latitude & Longitude  
- Aggregate Rating  
- Votes  

## 🔍 Methodology

### 1. Data Loading & Preparation
- Loaded dataset using Pandas  
- Selected relevant columns for analysis  

### 2. Map Initialization
- Created a base map using Folium  
- Centered the map using mean latitude and longitude  

### 3. Marker Visualization
- Plotted restaurant locations on the map  
- Added markers with popup details:
  - Restaurant Name  
  - Aggregate Rating  

### 4. Exporting Output
- Saved the interactive map as:
`restaurant_map.html`

### 5. Data Analysis
- Identified top cities with highest number of restaurants  
- Analyzed country-wise distribution  
- Evaluated correlation between:
  - Latitude  
  - Longitude  
  - Aggregate Rating  

## 📊 Key Insights
- New Delhi has the highest number of restaurants  
- Followed by Gurgaon and Noida  
- Dataset is concentrated in a few major cities  
- Country Code 1 dominates the dataset  
- Very weak correlation between location and rating  
→ Ratings are mostly independent of geographic location  

## 🗺️ Interactive Map
👉 [View the map](restaurant_map.html)

## 🚀 How to Run

1. Install required libraries:
```bash
pip install pandas folium
```

2. Run the Python file:
```bash
python "Task 3.py"
```

3. Open the generated file:
```bash
restaurant_map.html
```

## 📁 Project Structure

```
Geospatial-Restaurant-Analysis/
│
├── Task 3.py
├── restaurant_map.html
├── Dataset.csv
└── README.md
```

## 🚀 Conclusion
This project demonstrates how geospatial data can be visualized effectively using interactive maps. It highlights restaurant clustering across regions and shows that ratings are not significantly influenced by geographic location.

---
