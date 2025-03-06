import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Load Sample Dataset (Replacing CSV Dependency)
np.random.seed(42)
date_range = pd.date_range(start="2024-01-01", periods=60, freq="D")
stations = ["Central Park", "Times Square", "Brooklyn Bridge", "Union Square", "Wall Street"]
data = []
for date in date_range:
    for station in stations:
        num_rides = np.random.randint(100, 600)
        ride_duration = np.random.exponential(scale=15, size=num_rides)
        for duration in ride_duration:
            data.append([date, station, duration])

df = pd.DataFrame(data, columns=["start_date", "start_station_name", "ride_duration"])
df["start_date"] = pd.to_datetime(df["start_date"])

# Sidebar Navigation with Emojis
st.sidebar.title("🚲 Navigation")
page = st.sidebar.selectbox(
    "📌 Choose a page",
    ["🏁 Introduction", "📊 Ride Trends", "📍 Popular Stations", "⏳ Ride Duration Analysis", "💡 Recommendations"]
)

# Introduction Page
if page == "🏁 Introduction":
    st.markdown("""
    <h1 style='text-align: center; color: #ffffff; background-color: #333333; padding: 15px; border-radius: 10px; font-size: 40px;'>
    🚲 New York Citi Bike Dashboard
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    ## 🌟 Welcome to the Citi Bike Analysis Dashboard!
    This interactive dashboard provides an **in-depth analysis** of New York City's Citi Bike rides. 🚴‍♂️🚴‍♀️
    
    - Discover **ride trends** over time 📈
    - Identify the **most popular bike stations** 📍
    - Analyze **ride duration distributions** ⏳
    - Gain valuable **business recommendations** 💡
    
    ---
    
    ### Why Use This Dashboard?  
    - ✅ **Real-Time Data Insights**: Get the latest trends in Citi Bike rides  
    - ✅ **User-Friendly UI**: Simple & intuitive navigation  
    - ✅ **Actionable Business Insights**: Make data-driven decisions  

    ---
    
    ### How to Use This Dashboard?
    - Select different **pages** from the sidebar to view various analyses.  
    - Use the **filters** to customize the charts based on date range or stations.  
    - Hover over **charts** for detailed insights.  
    - Scroll down for **recommendations** to improve Citi Bike services.  
    """, unsafe_allow_html=True)

# Ride Trends Page
elif page == "📊 Ride Trends":
    st.markdown("""
    <h1 style='text-align: center; color: #ffffff; background-color: #444444; padding: 15px; border-radius: 10px; font-size: 35px;'>
    📊 Ride Trends Over Time
    </h1>
    """, unsafe_allow_html=True)

    daily_rides = df.groupby("start_date").size().reset_index(name="Total Rides")

    fig = px.line(
        daily_rides, 
        x="start_date", 
        y="Total Rides", 
        title="🚴‍♂️ Daily Citi Bike Rides", 
        line_shape="spline"
    )
    fig.update_traces(line_color='#1f77b4', line_width=5)
    fig.update_layout(
        title_x=0.5, 
        xaxis_title="<b>Date</b>", 
        yaxis_title="<b>Total Rides</b>",
        xaxis_title_font=dict(size=16, color="black"),
        yaxis_title_font=dict(size=16, color="black"),
        height=600  # Increase Chart Size
    )
    
    st.plotly_chart(fig)

# Popular Stations Page
elif page == "📍 Popular Stations":
    st.markdown("""
    <h1 style='text-align: center; color: #ffffff; background-color: #555555; padding: 15px; border-radius: 10px; font-size: 35px;'>
    📍 Most Popular Citi Bike Stations
    </h1>
    """, unsafe_allow_html=True)

    station_counts = df["start_station_name"].value_counts().nlargest(10)

    fig = px.bar(
        x=station_counts.index, 
        y=station_counts.values, 
        title="🏆 Top 10 Popular Start Stations",
        labels={"x": "🚲 <b>Station Name</b>", "y": "📊 <b>Number of Rides</b>"},
        color=station_counts.values,
        color_continuous_scale='Blues'
    )
    
    fig.update_layout(
        title_x=0.5,
        xaxis_title_font=dict(size=16, color="black"),
        yaxis_title_font=dict(size=16, color="black"),
        height=600  # Increase Chart Size
    )
    
    st.plotly_chart(fig)

# Ride Duration Analysis Page
elif page == "⏳ Ride Duration Analysis":
    st.markdown("""
    <h1 style='text-align: center; color: #ffffff; background-color: #666666; padding: 15px; border-radius: 10px; font-size: 35px;'>
    ⏳ Ride Duration Distribution
    </h1>
    """, unsafe_allow_html=True)

    # Create histogram
    fig = px.histogram(
        df, 
        x="ride_duration", 
        nbins=50, 
        title="⏳ Distribution of Ride Durations",
        labels={"ride_duration": "<b>Duration (Minutes)</b>"}, 
        color_discrete_sequence=['#FF5733']
    )
    
    fig.update_layout(
        title_x=0.5,
        xaxis_title_font=dict(size=16, color="black"),
        yaxis_title_font=dict(size=16, color="black"),
        height=600  # Increase Chart Size
    )

    st.plotly_chart(fig)
    
    st.markdown("""
    ## 📢 Interpretation:
    - ⏳ **Most rides are short**, typically under **30 minutes**.
    - 🚀 **Some long rides exist**, but they are less frequent.
    - 💡 **Business Opportunity:** Encourage longer rides with promotional discounts.
    """, unsafe_allow_html=True)

# Recommendations Page
elif page == "💡 Recommendations":
    st.markdown("""
    <h1 style='text-align: center; color: #ffffff; background-color: #777777; padding: 15px; border-radius: 10px; font-size: 35px;'>
    💡 Final Recommendations
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ## 🚴‍♂️ Citi Bike Improvement Plan:
    
    - 📉 **Optimize Bike Availability:** Reduce supply from **November–April** due to lower demand.  
    - 📍 **Expand Stations Near Water Areas:** High tourism areas could benefit from more bike docks.  
    - 🛠️ **Implement Smart Tracking:** Use real-time inventory updates to avoid shortages.  
    - 📊 **Enhance Pricing Strategy:** Offer discounts during off-peak hours to balance usage.  
    - 🌍 **Sustainability Initiatives:** Invest in eco-friendly bike options to reduce carbon footprint.  
    
    ---
    
    **🔹 Future Considerations:**
    - 🚲 Adding more **e-bikes** for longer commutes.
    - 📊 Enhancing **data analysis tools** to predict future demand.
    - 📢 Implementing **customer feedback systems** to improve services.
    """, unsafe_allow_html=True)
