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
8. [Requirements](#requirements)
9. [Installation & Usage](#installation--usage)
10. [Future Enhancements](#future-enhancements)
11. [Contributing](#contributing)
12. [Author](#author)
13. [License](#license)

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
Dive into the vibrant ebb and flow of PM2.5 pollution levels across Indian cities from 2015 to 2024. This striking line chart highlights seasonal spikes and yearly patterns, painting a clear picture of air quality evolution with bold, intuitive visuals.

### Seasonal Pollutant Trends
![Pollutant Distribution](visuals/pollutant_distribution.png)
Uncover the dynamic distribution and seasonal rhythms of key pollutants in this colorful visualization. It vividly illustrates peak pollution periods, using engaging hues to make complex data patterns easy to grasp and remember.

### Top Polluted Cities
![Top Cities](visuals/top_cities.png)
Ranked in a bold bar chart, this visualization spotlights India's most polluted cities by average AQI. With eye-catching colors and sharp contrasts, it delivers a compelling comparison of urban air quality challenges at a glance.

### Pollution Hotspots
![Pollution Hotspots](visuals/pollution_hotspots_clusters.png)
Explore pollution hotspots through this innovative clustering analysis. Cities with similar pollution profiles are grouped in a visually appealing scatter plot, revealing geographical patterns with vibrant clusters that highlight regional air quality stories.

### City Pollution Over Years
![Yearly Summary](visuals/yearly_summary.png)
Track the decade-long journey of pollution in selected cities with this elegant yearly summary chart. Featuring smooth lines and rich colors, it showcases trends and changes in air quality, making long-term insights both accessible and captivating.

### Stations per City
![Station Stats](visuals/station_stats.png)
This informative bar chart displays the number of monitoring stations per city, using a palette of fresh colors to emphasize data coverage and reliability. It's a quick, visually engaging way to assess the robustness of air quality monitoring across India.

### Additional Charts
### City Hour PM2.5 Trend
![City Hour PM2.5 Trend](visuals/city_hour_cleaned_pm25_trend.png)
Zoom into hourly PM2.5 fluctuations with this detailed trend chart. Bursting with color-coded data points, it offers granular insights into daily air quality variations, perfect for spotting short-term pollution events.

### Station Day PM2.5 Trend
![Station Day PM2.5 Trend](visuals/station_day_cleaned_pm25_trend.png)
Delve into daily PM2.5 trends from individual stations in this polished visualization. With a harmonious color scheme, it provides a granular, location-specific view of pollution levels, highlighting micro-trends in air quality.

### Station Hour PM2.5 Trend
![Station Hour PM2.5 Trend](visuals/station_hour_cleaned_pm25_trend.png)
Experience the pulse of hourly PM2.5 changes at specific stations through this dynamic chart. Its vibrant design captures short-term variations, making it an exciting tool for understanding real-time air quality dynamics.

### Seasonal CO
![Seasonal CO](visuals/seasonal_co.png)
Witness the seasonal dance of Carbon Monoxide (CO) levels in this lively chart. Using warm, inviting colors, it reveals how CO concentrations fluctuate across seasons, offering a fresh perspective on this critical pollutant.

### Seasonal NO
![Seasonal NO](visuals/seasonal_no.png)
This visualization brings seasonal Nitrogen Oxide (NO) patterns to life with bold, contrasting hues. It helps decode seasonal impacts on NO levels, transforming data into an engaging narrative of urban pollution.

### Seasonal NO2
![Seasonal NO2](visuals/seasonal_no2.png)
Explore Nitrogen Dioxide (NO2) trends through the seasons in this eye-popping chart. With a palette that pops, it provides clear insights into urban air pollution variations, making complex seasonal data feel approachable and fun.

### Seasonal O3
![Seasonal O3](visuals/seasonal_o3.png)
Highlighting Ozone (O3) concentrations, this chart uses serene yet striking colors to illustrate seasonal patterns. It spotlights periods of elevated ozone, delivering a visually soothing yet informative experience.

### Seasonal PM10
![Seasonal PM10](visuals/seasonal_pm10.png)
Track the seasonal ebb and flow of PM10 particulate matter in this robust visualization. Featuring earthy tones and clear lines, it offers a grounded view of how larger particulates fluctuate, with colors that evoke the natural cycles of pollution.

### Seasonal SO2
![Seasonal SO2](visuals/seasonal_so2.png)
This chart vividly displays Sulfur Dioxide (SO2) seasonal variations with industrial-inspired colors. It aids in understanding seasonal influences on this pollutant, using a design that's as informative as it is visually striking.

### City Comparison Dashboard
[Interactive City Comparison Dashboard](visuals/city_comparison_dashboard.html)
An interactive HTML dashboard built with Plotly, allowing users to compare pollution levels across cities dynamically. Explore trends, averages, and insights with engaging, interactive charts that bring the data to life in a fully immersive, colorful experience.

## Key Insights
- Delhi consistently ranks highest in PM2.5 levels.  
- Winter months show peak pollution across most cities.  
- Southern cities have comparatively lower pollution levels.  
- PM2.5 and PM10 are strongly correlated.  
- AQI improved slightly after the 2020 lockdown.

---

## Requirements

The project dependencies are listed below (from `requirements.txt`):

```
pandas==2.3.3
numpy==2.3.5
matplotlib==3.10.7
seaborn==0.13.2
plotly==6.5.0
scikit-learn==1.7.2
scipy==1.16.3
statsmodels==0.14.5
matplotlib-venn==1.1.2
pillow==12.0.0
```

## Installation & Usage

### 1️⃣ Clone & Navigate
```bash
# Clone the repository
git clone https://github.com/Abhinav-TheAnalyst/air-quality-india-2015-2024.git
cd air-quality-india-2015-2024
````

### 2️⃣ Install Dependencies

```bash
# (optional) Create and activate a virtual environment (PowerShell)
python -m venv .venv
. .venv\Scripts\Activate.ps1

# Install required Python libraries from the pinned requirements file
pip install -r requirements.txt
```

### 3️⃣ Run Data Cleaning

```bash
# Run the cleaning script
python scripts/clean_data.py
```

### Quick demo

Run the small example script (prints a summary and saves a demo PM2.5 plot):

```powershell
python .\scripts\run_example.py
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
# Generate a lightweight summary report (markdown)
python scripts/generate_summary.py
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

* LinkedIn: [LinkedIn](https://www.linkedin.com/in/abhinav-theanalyst/)
* GitHub: [Abhinav-TheAnalyst](https://github.com/Abhinav-TheAnalyst)

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## Reflections — What I learned

- Worked with a large, real-world dataset (Kaggle) covering 2015–2024 and learned practical data cleaning strategies (duplicate removal, date standardization, numeric coercion, median imputation for pollutants).
- Practiced time-series aggregation and visualization to reveal trends (daily/hourly aggregation and yearly summaries). 
- Performed seasonal analysis and basic statistical testing (ANOVA + Tukey HSD) to evaluate seasonal pollutant differences.
- Built reproducible analysis scripts and a small demo runner (`scripts/run_example.py`) so reviewers can quickly run a demo.
- Learned how to prepare outputs for sharing: CSV summaries in `output/` and visuals in `visuals/`; replaced a bulky PDF report with a lightweight `output/summary_report.md` and a small generator script to recreate it.

If you'd like, I can expand this section with specific lessons (libraries used, pitfalls, improvements you would make next) or convert it into a short 'Lessons learned' slide for portfolio use.