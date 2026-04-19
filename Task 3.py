# =========================================
# LEVEL 1 - TASK 3
# Geospatial Analysis (FINAL CODE)
# =========================================

import pandas as pd
import folium

# -------------------------------
# 1. Load dataset
# -------------------------------
df = pd.read_csv("Dataset.csv")

# -------------------------------
# 2. Create base map
# -------------------------------
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]

restaurant_map = folium.Map(location=map_center, zoom_start=5)

# -------------------------------
# 3. Add markers to map
# -------------------------------
# Limiting to first 1000 for performance
for index, row in df.head(1000).iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Restaurant Name']} | Rating: {row['Aggregate rating']}"
    ).add_to(restaurant_map)

# -------------------------------
# 4. Save map
# -------------------------------
restaurant_map.save("restaurant_map.html")

print("\nMap created and saved as 'restaurant_map.html'")

# -------------------------------
# 5. Distribution by City
# -------------------------------
print("\nTop 10 Cities with Most Restaurants:")
print(df['City'].value_counts().head(10))

# -------------------------------
# 6. Distribution by Country
# -------------------------------
print("\nTop 10 Country Codes:")
print(df['Country Code'].value_counts().head(10))

# -------------------------------
# 7. Correlation Analysis
# -------------------------------
correlation = df[['Latitude', 'Longitude', 'Aggregate rating']].corr()

print("\nCorrelation between Location and Rating:")
print(correlation)