# Air Quality Analysis Script
# This script generates various charts and analysis for the air quality dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up plotting style
plt.style.use('default')
sns.set_palette("husl")

# File paths
PROCESSED_DIR = "../data/processed/"
VISUALS_DIR = "../visuals/"

def create_pm25_trend():
    # Create a line chart showing PM2.5 trends over time for major cities
    df = pd.read_csv(PROCESSED_DIR + "city_day_cleaned.csv")
    df['Datetime'] = pd.to_datetime(df['Datetime'])

    # Group by city and resample to monthly averages to reduce noise
    df.set_index('Datetime', inplace=True)
    monthly_trend = df.groupby('City')['PM2.5'].resample('M').mean().reset_index()

    plt.figure(figsize=(14, 8))
    # Get top 6 cities by average PM2.5
    top_cities = monthly_trend.groupby('City')['PM2.5'].mean().nlargest(6).index

    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
    for i, city in enumerate(top_cities):
        city_data = monthly_trend[monthly_trend['City'] == city]
        plt.plot(city_data['Datetime'], city_data['PM2.5'],
                label=city, color=colors[i], linewidth=2, alpha=0.8)

    plt.title('Monthly PM2.5 Trends by Top Cities (2015-2024)', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('PM2.5 (µg/m³)', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(VISUALS_DIR + 'pm25_trend.png', dpi=200, bbox_inches='tight')
    plt.close()

def create_pollution_heatmap():
    # Generate a heatmap showing correlations between different pollutants
    df = pd.read_csv(PROCESSED_DIR + "city_day_cleaned.csv")

    pollutants = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
    corr = df[pollutants].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f', square=True)
    plt.title('Pollutant Correlation Matrix', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(VISUALS_DIR + 'pollution_correlation.png', dpi=200, bbox_inches='tight')
    plt.close()

def create_seasonal_analysis():
    # Analyze PM2.5 levels by season
    df = pd.read_csv(PROCESSED_DIR + "city_day_cleaned.csv")
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df['Month'] = df['Datetime'].dt.month

    # Define seasons based on months
    season_map = {12: 'Winter', 1: 'Winter', 2: 'Winter',
                  3: 'Spring', 4: 'Spring', 5: 'Spring',
                  6: 'Summer', 7: 'Summer', 8: 'Summer',
                  9: 'Fall', 10: 'Fall', 11: 'Fall'}
    df['Season'] = df['Month'].map(season_map)

    seasonal_avg = df.groupby('Season')['PM2.5'].mean().reindex(['Winter', 'Spring', 'Summer', 'Fall'])

    plt.figure(figsize=(10, 6))
    bars = plt.bar(seasonal_avg.index, seasonal_avg.values, color=['blue', 'green', 'orange', 'red'])
    plt.title('Average PM2.5 by Season (2015-2024)', fontsize=16, fontweight='bold')
    plt.xlabel('Season', fontsize=12)
    plt.ylabel('PM2.5 (µg/m³)', fontsize=12)
    plt.grid(axis='y', alpha=0.3)

    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.1f}', ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.savefig(VISUALS_DIR + 'seasonal_pm25.png', dpi=200, bbox_inches='tight')
    plt.close()

def create_city_comparison():
    # Compare PM2.5 distributions across cities using box plots
    df = pd.read_csv(PROCESSED_DIR + "city_day_cleaned.csv")

    top_cities = df.groupby('City')['PM2.5'].mean().nlargest(8).index
    df_top = df[df['City'].isin(top_cities)]

    plt.figure(figsize=(12, 8))
    sns.boxplot(x='City', y='PM2.5', data=df_top, palette='Set2')
    plt.title('PM2.5 Distribution by Top Cities', fontsize=16, fontweight='bold')
    plt.xlabel('City', fontsize=12)
    plt.ylabel('PM2.5 (µg/m³)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(VISUALS_DIR + 'city_pm25_boxplot.png', dpi=200, bbox_inches='tight')
    plt.close()

def create_yearly_trends():
    # Show yearly average PM2.5 trends for major cities
    df = pd.read_csv(PROCESSED_DIR + "city_day_cleaned.csv")
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df['Year'] = df['Datetime'].dt.year

    yearly_avg = df.groupby(['Year', 'City'])['PM2.5'].mean().reset_index()
    top_cities = yearly_avg.groupby('City')['PM2.5'].mean().nlargest(5).index
    yearly_top = yearly_avg[yearly_avg['City'].isin(top_cities)]

    plt.figure(figsize=(12, 8))
    for city in top_cities:
        city_data = yearly_top[yearly_top['City'] == city]
        plt.plot(city_data['Year'], city_data['PM2.5'], marker='o', label=city, linewidth=2)

    plt.title('Yearly Average PM2.5 by Top Cities', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('PM2.5 (µg/m³)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(yearly_avg['Year'].unique())
    plt.tight_layout()
    plt.savefig(VISUALS_DIR + 'yearly_pm25_trends.png', dpi=200, bbox_inches='tight')
    plt.close()

def main():
    # Run all analysis functions
    print("Creating visualizations...")
    create_pm25_trend()
    create_pollution_heatmap()
    create_seasonal_analysis()
    create_city_comparison()
    create_yearly_trends()
    print("Analysis complete!")

if __name__ == "__main__":
    main()
