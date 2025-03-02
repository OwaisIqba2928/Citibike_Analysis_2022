import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load dataset
file_path = "merged_citibike_weather.csv"
df = pd.read_csv(file_path)

# Convert date column to datetime
df['DATE'] = pd.to_datetime(df['DATE'])

# Handle missing station names (replace NaN with "Unknown")
df['start_station_name'] = df['start_station_name'].fillna("Unknown")

# --- Main Dashboard Navigation Bar ---
st.markdown(
    """
    <style>
        .main-nav {
            background-color: #1F2937;  /* Dark Color */
            padding: 15px;
            text-align: center;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        }
        .main-title {
            color: #F8E71C;  /* Light Yellow */
            font-size: 26px;
            font-weight: bold;
            letter-spacing: 1px;
        }
    </style>
    <div class="main-nav">
        <p class="main-title">🚲 CitiBike Data Dashboard</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Dashboard Description ---
st.markdown(
    "<p style='text-align:center; font-size:18px; color:#666;'>Explore CitiBike usage patterns and the relationship between trips and weather conditions.</p>", 
    unsafe_allow_html=True
)

# --- Sidebar Filters ---
st.sidebar.markdown("### 🎛️ Filter Options", unsafe_allow_html=True)
selected_station = st.sidebar.selectbox("🚲 **Select a Station**", ["All"] + sorted(df['start_station_name'].unique()))
selected_date_range = st.sidebar.date_input("📅 **Select Date Range**", [df['DATE'].min(), df['DATE'].max()])

# Filter dataset based on sidebar selections
filtered_df = df.copy()
if selected_station != "All":
    filtered_df = filtered_df[filtered_df["start_station_name"] == selected_station]

filtered_df = filtered_df[(filtered_df['DATE'] >= pd.to_datetime(selected_date_range[0])) & 
                          (filtered_df['DATE'] <= pd.to_datetime(selected_date_range[1]))]

# --- Small & Compact Chart Navigation Bars ---
st.markdown(
    """
    <style>
        .chart-nav {
            background-color: #1F2937;
            padding: 5px;
            text-align: center;
            border-radius: 5px;
            box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.15);
            font-size: 14px;
            font-weight: bold;
        }
        .chart-title {
            color: #F8E71C;
        }
    </style>
    <div class="chart-nav">
        <p class="chart-title">🚏 Top 10 Most Popular Bike Stations</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Bar Chart: Top 10 Most Popular Bike Stations ---
station_counts = df['start_station_name'].value_counts().nlargest(10)
fig1 = px.bar(
    station_counts,
    x=station_counts.index,
    y=station_counts.values,
    labels={'x': 'Station Name', 'y': 'Number of Trips'},
    color=station_counts.values,
    color_continuous_scale="YlOrBr"  # Light Yellow-Orange Theme
)

fig1.update_layout(
    xaxis_title="Station Name",
    yaxis_title="Number of Trips",
    xaxis=dict(title_font=dict(size=14, family="Arimo", color="black")),
    yaxis=dict(title_font=dict(size=14, family="Arimo", color="black")),
    title_x=0.5,
    showlegend=False  # Remove legend
)
st.plotly_chart(fig1)

# --- Small & Compact Chart Navigation Bar for Dual-Axis Chart ---
st.markdown(
    """
    <div class="chart-nav">
        <p class="chart-title">📈 Bike Trips & Temperature Trends</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Dual-Axis Line Chart: Bike Trips and Temperature ---
trips_per_day = filtered_df.groupby('DATE').size()
temperature_per_day = filtered_df.groupby('DATE')['TMAX'].mean()

fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=trips_per_day.index, 
    y=trips_per_day.values, 
    mode='lines', 
    name='Bike Trips', 
    line=dict(color="#003366", width=3)  # Dark Blue Line
))

fig2.add_trace(go.Scatter(
    x=temperature_per_day.index, 
    y=temperature_per_day.values, 
    mode='lines', 
    name='Temperature (TMAX)', 
    line=dict(color="#66B2FF", width=3),  # Light Blue Line
    yaxis="y2"
))

fig2.update_layout(
    xaxis_title="Date",
    yaxis=dict(title="Bike Trips", side="left", title_font=dict(size=14, family="Arimo", color="black")),
    yaxis2=dict(title="Temperature (°C)", overlaying="y", side="right", title_font=dict(size=14, family="Arimo", color="black")),
    showlegend=False  # Hide Legend
)

st.plotly_chart(fig2)
