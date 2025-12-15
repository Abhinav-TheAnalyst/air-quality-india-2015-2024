# scripts/clean_data.py
"""
Data Cleaning Script for Air Quality Dataset (India 2015-2024)

This script cleans raw CSV files by:
- Removing duplicates and invalid rows
- Standardizing date formats
- Converting data types appropriately
- Handling missing values with appropriate methods
- Saving cleaned data to processed directory

Author: Abhinav-TheAnalyst
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path

# Define paths
RAW_DIR = Path("../data/raw")
PROCESSED_DIR = Path("../data/processed")

# Ensure processed directory exists
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Files to process (only daily data for consistency)
FILES_TO_CLEAN = [
    "city_day.csv",
    "station_day.csv",
    "stations.csv"
]

def detect_date_column(df):
    """Detect the date/datetime column in the dataframe."""
    possible_cols = ['Date', 'Datetime', 'date', 'datetime', 'timestamp']
    for col in possible_cols:
        if col in df.columns:
            return col
    return None

def clean_pollutant_data(df, pollutant_cols):
    """Clean pollutant columns: convert to numeric, handle outliers, fill missing values."""
    for col in pollutant_cols:
        if col in df.columns:
            # Convert to numeric
            df[col] = pd.to_numeric(df[col], errors='coerce')

            # Remove negative values (invalid for pollutants)
            df.loc[df[col] < 0, col] = np.nan

            # Fill missing values with forward fill, then backward fill, then median
            df[col] = df[col].ffill().bfill().fillna(df[col].median())

    return df

def clean_data_quality(df):
    """Clean AQI and AQI_Bucket columns."""
    if 'AQI' in df.columns:
        df['AQI'] = pd.to_numeric(df['AQI'], errors='coerce')
        df.loc[df['AQI'] < 0, 'AQI'] = np.nan
        df['AQI'] = df['AQI'].ffill().bfill()

    if 'AQI_Bucket' in df.columns:
        # Standardize AQI bucket categories
        valid_buckets = ['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe']
        df['AQI_Bucket'] = df['AQI_Bucket'].astype(str).str.strip().str.title()
        df.loc[~df['AQI_Bucket'].isin(valid_buckets), 'AQI_Bucket'] = 'Unknown'

    return df

def clean_file(filepath):
    """Clean a single CSV file and return the cleaned dataframe."""
    print(f"Cleaning {filepath.name}...")

    # Read CSV
    df = pd.read_csv(filepath)

    # Remove completely empty rows
    df = df.dropna(how='all')

    # Remove duplicate rows
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"Removed {initial_rows - len(df)} duplicate rows")

    # Detect and process date column
    date_col = detect_date_column(df)
    if date_col:
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
        df = df.dropna(subset=[date_col])
        print(f"Processed {len(df)} rows with valid dates")
    else:
        print("Warning: No date column found")

    # Clean pollutant columns
    pollutant_cols = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']
    df = clean_pollutant_data(df, pollutant_cols)

    # Clean data quality columns
    df = clean_data_quality(df)

    # Clean categorical columns
    if 'City' in df.columns:
        df['City'] = df['City'].astype(str).str.strip().str.title()

    if 'Station' in df.columns:
        df['Station'] = df['Station'].astype(str).str.strip()

    return df

def main():
    """Main function to clean all specified files."""
    print("Starting data cleaning process...")

    for filename in FILES_TO_CLEAN:
        input_path = RAW_DIR / filename
        output_path = PROCESSED_DIR / filename.replace('.csv', '_cleaned.csv')

        if not input_path.exists():
            print(f"Warning: {input_path} not found, skipping")
            continue

        try:
            # Clean the data
            cleaned_df = clean_file(input_path)

            # Save cleaned data
            cleaned_df.to_csv(output_path, index=False)
            print(f"Saved cleaned data to {output_path}")
            print(f"Final shape: {cleaned_df.shape}")
            print("-" * 50)

        except Exception as e:
            print(f"Error cleaning {filename}: {e}")

    print("Data cleaning completed!")

if __name__ == "__main__":
    main()
