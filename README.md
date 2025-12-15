# Air Quality Analysis: India 2015-2024

[![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3.3-orange.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.3.5-lightblue.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.7-red.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-blue.svg)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-6.5.0-green.svg)](https://plotly.com/)

A concise, human-written analysis of air pollution across Indian cities (2015–2024). This repo contains scripts to clean, analyze and visualize the dataset — designed to be clear for reviewers and recruiters.

## 📊 Project Overview

This repository contains an analysis of air quality data collected from various monitoring stations across Indian cities. The dataset covers 10 years of daily air quality measurements, providing insights into pollution patterns, seasonal variations, and city-wise comparisons.

## ✨ Key Features

- **Data Cleaning Pipeline**: Automated preprocessing of raw data with missing value imputation
- **Trend Analysis**: Monthly and yearly PM2.5 trends for major cities
- **Seasonal Patterns**: Analysis of pollution variations across seasons
- **Correlation Studies**: Relationships between different pollutants
- **City Comparisons**: Statistical comparison of air quality across cities
- **Interactive Visualizations**: Web-based dashboards for data exploration

## 🚀 Getting Started

### Prerequisites
- Python 3.14+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Abhinav-TheAnalyst/air-quality-india-2015-2024.git
cd air-quality-india-2015-2024
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. Clean the raw data:
```bash
python scripts/clean_data.py
```

2. Run the main analysis:
```bash
python scripts/air_quality_analysis.py
```

3. Generate additional reports (optional):
```bash
python scripts/city_ranking.py
python scripts/seasonal_analysis.py
```

## 📈 Analysis Results

### PM2.5 Monthly Trends
Monthly averaged PM2.5 levels showing long-term trends for top polluted cities.

![PM2.5 Monthly Trends](visuals/pm25_trend.png)

### Seasonal Pollution Patterns
Average PM2.5 concentrations across different seasons, highlighting winter peaks.

![Seasonal Analysis](visuals/seasonal_pm25.png)

### Pollutant Correlations
Heatmap showing relationships between major air pollutants.

# 🌍 Air Quality Analysis: India 2015-2024

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3.3-orange.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.3.5-lightblue.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.7-red.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-blue.svg)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-6.5.0-green.svg)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

![PM2.5 Example](visuals/pm25_trend.png)

A concise, human-written analysis of air pollution across Indian cities (2015–2024). This repo contains scripts to clean, analyze and visualize the dataset — designed to be clear for reviewers and recruiters.

---

## 📋 Index (quick links)

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Analysis Results](#analysis-results)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Data Variables](#data-variables)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This repository analyzes air quality measurements from multiple Indian cities over 2015–2024. The focus is on clear data preparation, interpretable visualizations, and reproducible scripts.

## Key Features

- Data cleaning and preprocessing
- Monthly and yearly PM2.5 trend analysis
- Seasonal comparisons and labeled bar charts
- Pollutant correlation heatmaps
- City-level distribution comparisons (boxplots)
- Simple interactive dashboards (optional)

## Getting Started

### Prerequisites
- Python 3.8+ installed
- pip available

### Installation

Clone and install:
```powershell
git clone https://github.com/Abhinav-TheAnalyst/air-quality-india-2015-2024.git
cd "air-quality-india-2015-2024"
pip install -r requirements.txt
```

### Quick commands
```powershell
# Clean data
python scripts/clean_data.py

# Run the main analysis (creates images in visuals/)
python scripts/air_quality_analysis.py

# Optional reports
python scripts/city_ranking.py
python scripts/seasonal_analysis.py
```

## Analysis Results

Example outputs (saved to `visuals/`):

- `pm25_trend.png` — Monthly PM2.5 trends for top cities
- `seasonal_pm25.png` — Average PM2.5 by season with labels
- `pollution_correlation.png` — Correlation heatmap for pollutants
- `city_pm25_boxplot.png` — Boxplots comparing city PM2.5 distributions
- `yearly_pm25_trends.png` — Annual averages across top cities

## Project Structure

```
air-quality-india-2015-2024/
│
├── data/
│   └── processed/           # Cleaned and processed data (used by scripts)
│
├── scripts/                 # Python analysis scripts
│   ├── clean_data.py        # Data preprocessing
│   ├── air_quality_analysis.py  # Main analysis and visualization
│   ├── city_ranking.py      # City ranking analysis
│   ├── seasonal_analysis.py # Seasonal pattern analysis
│   └── interactive_visualizations.py  # Interactive plots
│
├── visuals/                 # Generated charts and plots (output)
├── output/                  # Analysis results and summaries
│
├── config.py                # Optional configuration
├── requirements.txt         # Python dependencies
├── README.md                # This file
└── LICENSE                  # MIT License
```

> Note: The `data/raw/` folder (original source CSVs) is not included in the public README listing. If you need the raw source files, they can be downloaded from the Kaggle dataset linked below.

## Technologies

- Python, Pandas, NumPy
- Matplotlib, Seaborn for static plots
- Plotly for interactive charts (optional)

## Data Variables

Common columns in processed data:

- `PM2.5`, `PM10` — particulate matter (µg/m³)
- `NO`, `NO2`, `NOx` — nitrogen oxides (µg/m³)
- `SO2` — sulfur dioxide (µg/m³)
- `CO` — carbon monoxide (mg/m³)
- `O3` — ozone (µg/m³)
- `AQI` — air quality index

## Contributing

Contributions welcome. Open an issue or submit a PR with small, focused changes.

## License

MIT — see the `LICENSE` file.

## Data Source

Kaggle: Air Quality Data in India (2015-2024) — https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india
Track the seasonal ebb and flow of PM10 particulate matter in this robust visualization. Featuring earthy tones and clear lines, it offers a grounded view of how larger particulates fluctuate, with colors that evoke the natural cycles of pollution.

### Seasonal SO2
![Seasonal SO2](visuals/seasonal_so2.png)
This chart vividly displays Sulfur Dioxide (SO2) seasonal variations with industrial-inspired colors. It aids in understanding seasonal influences on this pollutant, using a design that's as informative as it is visually striking.

### Pollutant Correlations
![City Correlation](visuals/city_day_cleaned_correlation.png)
Heatmap showing correlations between pollutants in daily city data, revealing relationships with a plasma color scale.

![Station Correlation](visuals/station_day_cleaned_correlation.png)
Station-level daily correlations.

### Interactive Visualizations
[Interactive PM2.5 Trends](visuals/city_day_cleaned_pm25_trend_interactive.html)
Interactive weekly PM2.5 trends by city.

[Interactive Top Polluted Cities](visuals/top_polluted_cities_interactive.html)
Interactive bar chart of top polluted cities.

[Interactive Seasonal PM2.5 Trends](visuals/seasonal_pm25_trends_interactive.html)
Interactive seasonal trends.

[Interactive Correlations](visuals/city_day_cleaned_correlation_interactive.html)
Interactive correlation heatmap.

### City Comparison Dashboard
[Interactive City Comparison Dashboard](visuals/city_comparison_dashboard.html)
An interactive HTML dashboard built with Plotly, allowing users to compare pollution levels across cities dynamically. Explore trends, averages, and insights with engaging, interactive charts that bring the data to life in a fully immersive, colorful experience.

## Original Raw Data (preview)

Below are the original CSV files provided (from Kaggle). For each file I show the approximate number of rows, number of columns, the header, and two sample rows so reviewers can see the raw schema and data format quickly.

- `data/raw/city_day.csv` — rows: ~18,266; columns: 16

```
Header: City,Datetime,PM2.5,PM10,NO,NO2,NOx,NH3,CO,SO2,O3,Benzene,Toluene,Xylene,AQI,AQI_Bucket
Sample:
Delhi,2015-01-01,153.3,241.7,182.9,33.0,81.3,38.5,1.87,64.5,83.6,18.93,20.81,8.32,204.5,Severe
Mumbai,2015-01-01,70.5,312.7,195.0,42.0,122.5,31.5,7.22,83.8,108.0,2.01,19.41,2.86,60.9,Satisfactory
```

- `data/raw/city_hour.csv` — rows: ~438,246; columns: 16

```
Header: City,Datetime,PM2.5,PM10,NO,NO2,NOx,NH3,CO,SO2,O3,Benzene,Toluene,Xylene,AQI,AQI_Bucket
Sample:
Delhi,2015-01-01 00:00:00,258.0,340.6,191.0,13.4,104.1,16.2,1.15,39.8,70.4,11.64,10.23,1.95,411.5,Moderate
Mumbai,2015-01-01 00:00:00,120.1,47.9,165.3,57.9,139.2,14.4,0.76,3.3,23.2,11.35,11.38,1.53,134.8,Poor
```

- `data/raw/stations.csv` — rows: ~11; columns: 2

```
Header: City,Station
Sample:
Delhi,Station_D1
Delhi,Station_D2
```

- `data/raw/station_day.csv` — rows: ~36,531; columns: 17

```
Header: City,Datetime,Station,PM2.5,PM10,NO,NO2,NOx,NH3,CO,SO2,O3,Benzene,Toluene,Xylene,AQI,AQI_Bucket
Sample:
Delhi,2015-01-01,Station_D1,58.3,223.2,126.6,85.5,207.5,18.4,0.25,42.7,184.9,8.03,12.72,4.1,266.4,Moderate
Mumbai,2015-01-01,Station_M1,36.6,160.8,164.2,18.6,94.8,8.9,6.84,70.7,195.4,5.53,26.93,2.64,5.9,Moderate
```

- `data/raw/station_hour.csv` — rows: ~7,211; columns: 17

```
Header: City,Datetime,Station,PM2.5,PM10,NO,NO2,NOx,NH3,CO,SO2,O3,Benzene,Toluene,Xylene,AQI,AQI_Bucket
Sample:
Delhi,2015-01-01 00:00:00,Station_D1,243.1,193.5,182.4,58.8,100.9,30.4,3.08,24.3,166.7,12.66,18.42,1.91,301.5,Good
Delhi,2015-01-01 00:00:00,Station_D2,476.7,504.0,172.4,80.7,114.4,30.3,7.96,48.1,72.9,8.35,26.53,1.66,243.1,Satisfactory
```

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