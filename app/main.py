import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Solar Farm Analysis Dashboard",
    page_icon="☀️",
    layout="wide"
)

# Title and description
st.title("🌍 Solar Farm Analysis Dashboard")
st.markdown("Compare solar potential across Benin, Sierra Leone, and Togo")

# Load data function
@st.cache_data
def load_data():
    """Load all country data and combine"""
    benin = pd.read_csv('data/benin_clean.csv')
    sierra_leone = pd.read_csv('data/sierraleone-bumbuna_clean.csv')
    togo = pd.read_csv('data/togo_clean.csv')
    
    # Add country labels
    benin['Country'] = 'Benin'
    sierra_leone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'
    
    # Combine all data
    all_data = pd.concat([benin, sierra_leone, togo], ignore_index=True)
    return all_data

# Load the data
data = load_data()

# Sidebar for controls
st.sidebar.header("🎛️ Dashboard Controls")

# Country selection
countries = st.sidebar.multiselect(
    "Select Countries:",
    ["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

# Metric selection
metric_options = ['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS', 'WSgust', 'TModA', 'TModB']
metric = st.sidebar.selectbox("Select Metric:", metric_options)

# Date range filter (if timestamp available)
st.sidebar.subheader("Time Filter")
if 'Timestamp' in data.columns:
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    min_date = data['Timestamp'].min().date()
    max_date = data['Timestamp'].max().date()
    
    date_range = st.sidebar.date_input(
        "Select Date Range:",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

# Filter data based on selections
filtered_data = data[data['Country'].isin(countries)]

if 'Timestamp' in data.columns and len(date_range) == 2:
    start_date, end_date = date_range
    filtered_data = filtered_data[
        (filtered_data['Timestamp'].dt.date >= start_date) & 
        (filtered_data['Timestamp'].dt.date <= end_date)
    ]

# Main dashboard layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"📊 {metric} Distribution by Country")
    
    # Boxplot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=filtered_data, x='Country', y=metric, ax=ax, palette="viridis")
    ax.set_title(f'{metric} Distribution Across Selected Countries', fontsize=14, fontweight='bold')
    ax.set_ylabel(metric)
    ax.set_xlabel('Country')
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.subheader("📈 Country Statistics")
    
    # Summary statistics table
    if not filtered_data.empty:
        stats = filtered_data.groupby('Country')[metric].agg([
            'mean', 'median', 'std', 'min', 'max'
        ]).round(2)
        stats.columns = ['Mean', 'Median', 'Std Dev', 'Min', 'Max']
        st.dataframe(stats, use_container_width=True)
    else:
        st.warning("No data available for selected filters")

# Solar Potential Ranking
st.subheader("🏆 Solar Potential Ranking")

# Bar chart - average metric by country
if not filtered_data.empty:
    avg_metric = filtered_data.groupby('Country')[metric].mean().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['gold', 'silver', 'brown'][:len(avg_metric)]
    avg_metric.plot(kind='bar', ax=ax, color=colors, edgecolor='black')
    ax.set_title(f'Countries Ranked by Average {metric}', fontweight='bold')
    ax.set_ylabel(f'Average {metric}')
    ax.set_xlabel('Country')
    plt.xticks(rotation=45)
    
    # Add value labels on bars
    for i, v in enumerate(avg_metric):
        ax.text(i, v + max(avg_metric)*0.01, f'{v:.1f}', ha='center', va='bottom', fontweight='bold')
    
    st.pyplot(fig)

# Time Series Analysis
if 'Timestamp' in filtered_data.columns and not filtered_data.empty:
    st.subheader("⏰ Time Series Analysis")
    
    # Daily averages
    daily_avg = filtered_data.groupby([filtered_data['Timestamp'].dt.date, 'Country'])[metric].mean().reset_index()
    
    fig = px.line(daily_avg, x='Timestamp', y=metric, color='Country',
                  title=f'Daily Average {metric} Over Time',
                  labels={'Timestamp': 'Date', metric: f'Average {metric}'})
    st.plotly_chart(fig, use_container_width=True)

# Data Summary
st.subheader("📋 Data Summary")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", f"{len(filtered_data):,}")

with col2:
    st.metric("Countries Selected", len(countries))

with col3:
    if not filtered_data.empty:
        top_country = filtered_data.groupby('Country')[metric].mean().idxmax()
        top_value = filtered_data.groupby('Country')[metric].mean().max()
        st.metric("Highest Average", f"{top_country}: {top_value:.1f}")

# Footer
st.markdown("---")
st.markdown("**MoonLight Energy Solutions** | Solar Data Analysis Dashboard")
st.markdown("*Data sources: Benin, Sierra Leone, and Togo solar measurement stations*")