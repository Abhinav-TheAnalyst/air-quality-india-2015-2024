# scripts/analyze_data_enhanced.py
"""
Simple Data Analysis for Air Quality Dataset

This script creates basic visualizations and analysis.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
plt.style.use('default')
sns.set_palette("husl")

# Paths
PROCESSED_DIR = "../data/processed/"
VISUALS_DIR = "../visuals/"

def create_pm25_trend():
    """Create PM2.5 trend plot."""
    df = pd.read_csv(PROCESSED_DIR + "city_day_cleaned.csv")

    # Group by city and date
    trend = df.groupby(['Datetime', 'City'])['PM2.5'].mean().reset_index()

    plt.figure(figsize=(12, 6))
    for city in trend['City'].unique()[:5]:  # Top 5 cities
        city_data = trend[trend['City'] == city]
        plt.plot(city_data['Datetime'], city_data['PM2.5'], label=city, marker='o', markersize=2)

    plt.title('PM2.5 Trends by City (2015-2024)')
    plt.xlabel('Date')
    plt.ylabel('PM2.5 (µg/m³)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(VISUALS_DIR + 'pm25_trend.png', dpi=150)
    plt.close()

def create_pollution_heatmap():
    """Create correlation heatmap."""
    df = pd.read_csv(PROCESSED_DIR + "city_day_cleaned.csv")

    pollutants = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
    corr = df[pollutants].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title('Pollutant Correlation Matrix')
    plt.tight_layout()
    plt.savefig(VISUALS_DIR + 'pollution_correlation.png', dpi=150)
    plt.close()

def create_seasonal_analysis():
    """Create seasonal PM2.5 analysis."""
    df = pd.read_csv(PROCESSED_DIR + "city_day_cleaned.csv")
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df['Month'] = df['Datetime'].dt.month

    # Map months to seasons
    season_map = {12: 'Winter', 1: 'Winter', 2: 'Winter',
                  3: 'Spring', 4: 'Spring', 5: 'Spring',
                  6: 'Summer', 7: 'Summer', 8: 'Summer',
                  9: 'Fall', 10: 'Fall', 11: 'Fall'}
    df['Season'] = df['Month'].map(season_map)

    seasonal_avg = df.groupby('Season')['PM2.5'].mean().reindex(['Winter', 'Spring', 'Summer', 'Fall'])

    plt.figure(figsize=(8, 5))
    seasonal_avg.plot(kind='bar', color=['blue', 'green', 'red', 'orange'])
    plt.title('Average PM2.5 by Season')
    plt.xlabel('Season')
    plt.ylabel('PM2.5 (µg/m³)')
    plt.tight_layout()
    plt.savefig(VISUALS_DIR + 'seasonal_pm25.png', dpi=150)
    plt.close()

def main():
    """Run all analyses."""
    print("Creating visualizations...")
    create_pm25_trend()
    create_pollution_heatmap()
    create_seasonal_analysis()
    print("Analysis complete!")

if __name__ == "__main__":
    main()
