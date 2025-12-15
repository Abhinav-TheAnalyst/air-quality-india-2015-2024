# scripts/clean_data.py
"""
Simple Data Cleaning for Air Quality Dataset

This script cleans the raw air quality data by:
- Removing duplicates
- Filling missing values
- Converting data types
"""

import pandas as pd
import numpy as np

# File paths
RAW_DIR = "../data/raw/"
PROCESSED_DIR = "../data/processed/"

# Files to clean
FILES = ["city_day.csv", "station_day.csv", "stations.csv"]

def clean_data():
    """Clean all data files."""
    for filename in FILES:
        print(f"Cleaning {filename}...")

        # Read data
        df = pd.read_csv(RAW_DIR + filename)

        # Remove duplicates
        df = df.drop_duplicates()

        # Fill missing values for pollutants
        pollutants = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3']
        for col in pollutants:
            if col in df.columns:
                df[col] = df[col].fillna(df[col].median())

        # Fill AQI
        if 'AQI' in df.columns:
            df['AQI'] = df['AQI'].fillna(df['AQI'].median())

        # Save cleaned data
        output_file = PROCESSED_DIR + filename.replace('.csv', '_cleaned.csv')
        df.to_csv(output_file, index=False)
        print(f"Saved: {output_file}")

if __name__ == "__main__":
    clean_data()
