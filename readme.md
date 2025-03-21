# 🚴♂️ CitiBike Data Analysis with Weather Integration 🌦️

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

## 🌟 **Introduction**  
This project analyzes **CitiBike trip data** alongside **weather conditions** to uncover patterns in bike-sharing usage across New York City. By integrating weather data, it explores how environmental factors influence rider behavior, providing actionable insights for optimizing bike availability and station placement.  

🔗 **Explore the Interactive Dashboard:**  
[![Streamlit Dashboard](https://img.shields.io/badge/Explore_Live_Dashboard-FF4B4B)](https://citibikeanalysis2022-ezcanh3kauapcsaxn4uf4d.streamlit.app/)

---

## 🎯 **Project Objectives**  
1. **Data Integration**: Clean and merge CitiBike trip data with weather datasets.  
2. **Route Analysis**: Identify peak routes and station usage trends.  
3. **Weather Impact**: Correlate temperature/precipitation with bike demand.  
4. **Visual Storytelling**: Create interactive maps and visualizations for stakeholders.  

---

## 🛠️ **Tools & Technologies**  
- **Python**: Data processing, analysis, and automation.  
- **Pandas/NumPy**: Data cleaning and aggregation.  
- **Matplotlib/Seaborn**: Static visualizations (heatmaps, time series).  
- **Streamlit**: Interactive web dashboard deployment.  
- **Kepler.gl**: Geospatial mapping of bike routes.  

---

## 🔍 **Key Insights**  
### 🚲 **Busiest Routes & Stations**  
- **Top Route**: *1 Ave & E 110 St → 1 Ave & E 94 St* (15 trips).  
- **Most Frequent Round Trips**: *1 Ave & E 110 St* (27 round trips).  
- **Key Hub**: *1 Ave & E 110 St* had the highest trip volume, suggesting proximity to residential/commercial hotspots.  

### 🌦️ **Weather Influence**  
- **Temperature**: Higher ridership on days with moderate temperatures (15–25°C).  
- **Precipitation**: 20% drop in rentals during rainy days.  

### 📊 **Usage Patterns**  
- **Peak Hours**: 8–9 AM and 5–6 PM (commuter traffic).  
- **Weekend Trends**: Longer average trip durations (+15% vs. weekdays).  

---

## 📂 **Repository Structure**  
```plaintext
CitiBike-Weather-Analysis/  
├── Data/  
│   ├── Raw/                # Original CitiBike & weather CSV files  
│   └── Processed/          # Cleaned and merged datasets  
├── Notebooks/              # Jupyter notebooks for analysis  
├── Visualizations/         # Kepler.gl maps and static charts  
├── dashboard.py            # Streamlit app script  
├── README.md               # Project overview  
└── requirements.txt        # Python dependencies  
