# 🌍 Air Quality Data Analysis (India, 2015–2024)

[![Python](https://img.shields.io/badge/python-3.10-blue?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

Analyzing air quality data across major Indian cities from 2015 to 2024.  
This project demonstrates a **complete end-to-end data pipeline**, including **data cleaning, processing, visualization, trend analysis, and city-level insights**, aimed at showcasing skills for **Data Analyst / Data Scientist roles**.

---

## Table of Contents
1. [Overview](#overview)
2. [Problem Statement](#problem-statement)
3. [Project Structure](#project-structure)
4. [Tech Stack](#tech-stack)
5. [Key Features](#key-features)
6. [Key Visualizations](#key-visualizations)
7. [Key Insights](#key-insights)
8. [Installation & Usage](#installation--usage)
9. [Future Enhancements](#future-enhancements)
10. [Contributing](#contributing)
11. [Author](#author)
12. [License](#license)

---

## Overview
This project analyzes **air quality across major Indian cities from 2015 to 2024**, providing insights on pollution trends, hotspots, and seasonal variations.  
It highlights **skills in data cleaning, exploratory data analysis, visualization, and trend reporting**, making it recruiter-friendly.

---

## Problem Statement
Air pollution is a serious concern in India, impacting public health and quality of life.  
This project aims to:
- Identify cities with the highest pollution levels.
- Track trends over the years and across seasons.
- Provide actionable insights for environmental monitoring.

---

## Project Structure
```

air-quality-data-2015-2024/
│
├── data/
│   ├── raw/        # Original CSV files
│   ├── processed/  # Processed datasets
│   └── output/     # Analysis outputs
│
├── visuals/        # Plots, graphs & dashboards
├── scripts/        # Python scripts for analysis
└── notebooks/      # Jupyter notebooks

````

---

## Tech Stack
- **Languages:** Python 3.10+  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn  
- **Environment:** Jupyter Notebook / VS Code  
- **Tools:** Git & GitHub  
- **Concepts:** ETL, Time-Series Analysis, Data Visualization, Correlation Analysis

---

## Key Features
- **Automated Data Cleaning:** Removes duplicates, fixes missing values, standardizes dates.  
- **Trend Analysis:** PM2.5 trends over time for each dataset.  
- **Top Polluted Cities:** Ranking of cities by average AQI.  
- **Seasonal Trends:** Average pollutant levels by season.  
- **City Pollution Over Years:** Trends in AQI for top cities.  
- **Station Analysis:** Number of monitoring stations per city.  
- **Pollution Hotspots:** Clustering of cities by pollution levels.

---

## Key Visualizations
### PM2.5 Trends
![PM2.5 Trend](visuals/pm25_trend.png)
This chart illustrates the overall trends in PM2.5 pollution levels across Indian cities from 2015 to 2024, highlighting seasonal and yearly variations.

### Seasonal Pollutant Trends
![Pollutant Distribution](visuals/pollutant_distribution.png)
This visualization shows the distribution and seasonal patterns of various pollutants, helping to identify peak pollution periods throughout the year.

### Top Polluted Cities
![Top Cities](visuals/top_cities.png)
This bar chart ranks the top polluted cities in India based on average AQI levels, providing a clear comparison of pollution severity across major urban areas.

### Pollution Hotspots
![Pollution Hotspots](visuals/pollution_hotspots_clusters.png)
This clustering analysis identifies pollution hotspots by grouping cities with similar pollution profiles, revealing geographical patterns in air quality.

### City Pollution Over Years
![Yearly Summary](visuals/yearly_summary.png)
This chart displays the yearly summary of pollution levels for selected cities, showing trends and changes in air quality over the decade.

### Stations per City
![Station Stats](visuals/station_stats.png)
This visualization presents the number of air quality monitoring stations available in each city, indicating the coverage and reliability of pollution data.

### Additional Charts
### City Hour PM2.5 Trend
![City Hour PM2.5 Trend](visuals/city_hour_cleaned_pm25_trend.png)
This chart shows the PM2.5 pollution trends over time based on hourly city-level data, offering detailed insights into daily and hourly fluctuations.

### Station Day PM2.5 Trend
![Station Day PM2.5 Trend](visuals/station_day_cleaned_pm25_trend.png)
This visualization depicts PM2.5 trends from daily station data, providing a granular view of pollution levels at specific monitoring locations.

### Station Hour PM2.5 Trend
![Station Hour PM2.5 Trend](visuals/station_hour_cleaned_pm25_trend.png)
This chart illustrates hourly PM2.5 trends from station-level data, highlighting short-term variations in air quality at individual monitoring points.

### Seasonal CO
![Seasonal CO](visuals/seasonal_co.png)
This chart shows the seasonal trends in Carbon Monoxide (CO) levels, revealing how CO concentrations vary across different seasons.

### Seasonal NO
![Seasonal NO](visuals/seasonal_no.png)
This visualization displays seasonal patterns in Nitrogen Oxide (NO) levels, helping to understand seasonal impacts on this pollutant.

### Seasonal NO2
![Seasonal NO2](visuals/seasonal_no2.png)
This chart illustrates the seasonal trends in Nitrogen Dioxide (NO2) concentrations, providing insights into seasonal variations in urban air pollution.

### Seasonal O3
![Seasonal O3](visuals/seasonal_o3.png)
This visualization shows seasonal patterns in Ozone (O3) levels, highlighting periods of higher ozone concentration in the atmosphere.

### Seasonal PM10
![Seasonal PM10](visuals/seasonal_pm10.png)
This chart depicts seasonal trends in PM10 particulate matter, offering a view of how larger particulate pollution fluctuates throughout the year.

### Seasonal SO2
![Seasonal SO2](visuals/seasonal_so2.png)
This visualization displays seasonal variations in Sulfur Dioxide (SO2) levels, aiding in understanding seasonal influences on this industrial pollutant.

---

## Key Insights
- Delhi consistently ranks highest in PM2.5 levels.  
- Winter months show peak pollution across most cities.  
- Southern cities have comparatively lower pollution levels.  
- PM2.5 and PM10 are strongly correlated.  
- AQI improved slightly after the 2020 lockdown.

---

## Installation & Usage

### 1️⃣ Clone & Navigate
```bash
# Clone the repository
git clone https://github.com/abhinav0077/air-quality-india-2015-2024.git
cd air-quality-india-2015-2024
````

### 2️⃣ Install Dependencies

```bash
# Install required Python libraries
pip install pandas numpy matplotlib seaborn plotly streamlit prophet scipy statsmodels
```

### 3️⃣ Run Data Cleaning

```bash
# Run the cleaning script
python scripts/clean_data.py
```

### 4️⃣ Run Analysis & Visualizations

```bash
# Run data cleaning
python scripts/clean_data.py

# Run analysis and generate visualizations
python scripts/analyze_data.py
python scripts/analyze_data_enhanced.py
python scripts/analyze_stations.py
python scripts/city_pollution_over_years.py
python scripts/pollution_hotspots.py
python scripts/seasonal_trends.py
python scripts/top_polluted_cities.py

# Generate reports and dashboards
python scripts/generate_report.py
python scripts/interactive_visualizations.py
python scripts/city_comparison_dashboard.py
python scripts/missing_values_report.py

# Run all scripts at once
python scripts/run_all.py
```

## Contributing

Contributions are welcome!

* Fork the repo
* Create a branch (`git checkout -b feature-name`)
* Make improvements or add features
* Submit a pull request

---

## Author

**Abhinav Verma** – Aspiring Data Analyst / Data Scientist

* LinkedIn: [LinkedIn](https://www.linkedin.com/in/abhinav-verma-0077/)
* GitHub: [abhinav0077](https://github.com/abhinav0077)

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
