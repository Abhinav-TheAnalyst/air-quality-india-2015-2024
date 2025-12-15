# Data Cleaning Script for Air Quality Dataset
# This script processes the raw data files to prepare them for analysis

import pandas as pd
import numpy as np

# Define file paths
RAW_DIR = "../data/raw/"
PROCESSED_DIR = "../data/processed/"

# List of files that need cleaning
FILES = ["city_day.csv", "station_day.csv", "stations.csv"]

def clean_data():
    # Process each data file
    for filename in FILES:
        print(f"Cleaning {filename}...")

        # Load the raw data
        df = pd.read_csv(RAW_DIR + filename)

        # Remove any duplicate rows
        df = df.drop_duplicates()

        # Handle missing values for pollutant columns by filling with median
        pollutants = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3']
        for col in pollutants:
            if col in df.columns:
                df[col] = df[col].fillna(df[col].median())

        # Fill missing AQI values
        if 'AQI' in df.columns:
            df['AQI'] = df['AQI'].fillna(df['AQI'].median())

        # Save the cleaned data
        output_file = PROCESSED_DIR + filename.replace('.csv', '_cleaned.csv')
        df.to_csv(output_file, index=False)
        print(f"Saved: {output_file}")

if __name__ == "__main__":
    clean_data()
