🌍 Air Quality Data Analysis (India, 2015–2024)

This project analyzes air quality data across major Indian cities from 2015 to 2024.
It includes a complete ETL pipeline, visualizations, trend analysis, city rankings, pollutant summaries, and insights designed to impress recruiters for data analyst / data scientist roles.

📁 Project Structure
air-quality-data-2015-2024/
│
├── data/
│   ├── raw/              # Original CSV files
│   ├── cleaned/          # Cleaned files from clean_data.py
│   └── processed/        # Additional processed outputs
│
├── visuals/              # Plots, graphs & dashboards
│
└── scripts/
    ├── clean_data.py
    ├── analyze_data.py
    ├── report_top_cities.py
    ├── pollutant_distribution.py
    ├── city_trend_analysis.py
    ├── correlation_matrix.py
    ├── yearly_summary.py
    ├── station_stats.py
    └── combined_dashboard.py

🛠 Tech Stack

Python 3.10+

Pandas

NumPy

Matplotlib

Seaborn

Jupyter / VS Code

Git & GitHub

🚀 Features
✔ 1. Automated Cleaning Pipeline

Your cleaning script:

Removes duplicates

Fixes missing values

Standardizes date formats

Creates new cleaned files

✔ 2. Trend Analysis

Plots PM2.5 & PM10 pollution trends for each city over time.

✔ 3. Most Polluted Cities Report

Creates an annual ranking of:

Highest AQI cities

Worst PM2.5 levels

Declining vs improving cities

✔ 4. Pollutant Distribution

Histograms & KDE plots for:

PM2.5, PM10

NO2, SO2, Ozone

CO, NH3, Benzene

✔ 5. Yearly Summary Reports

Generates summarized CSVs:

Average pollutant levels

Max/Min AQI

Top polluted cities per year

✔ 6. Correlation Heatmaps

Shows correlation between pollutants.

✔ 7. Station-Level Insights

Stats per monitoring station:

Missing data rate

Pollutant averages

Top polluted stations

✔ 8. Combined Dashboard

Generates multiple visualizations at once.

📜 How to Run the Project
1️⃣ Install requirements
pip install pandas matplotlib seaborn numpy

2️⃣ Run the cleaning script
python scripts/clean_data.py

3️⃣ Run analysis scripts

Run all:

python scripts/analyze_data.py
python scripts/report_top_cities.py
python scripts/yearly_summary.py
python scripts/pollutant_distribution.py
python scripts/city_trend_analysis.py
python scripts/correlation_matrix.py
python scripts/station_stats.py
python scripts/combined_dashboard.py

📊 Visuals (Saved in visuals/)

Your project generates visuals such as:

✔ PM2.5 Trends
✔ AQI Trend Comparisons
✔ Pollutant Distributions
✔ Top Polluted Cities Bar Charts
✔ Correlation Heatmaps
✔ Yearly AQI Summary Charts
✔ Station Performance Reports
✔ Combined Dashboards

🔍 Insights (Example)

Some insights you may include once visuals are ready:

Delhi consistently ranks #1 in PM2.5 pollution for most years.

Winter months show the highest pollution peaks.

Southern cities have significantly lower PM levels.

Correlation matrix shows PM2.5 and PM10 are strongly correlated.

AQI improved slightly after 2020 lockdown.

(You can fill more after generating visuals.)

🎯 Why This Project Is Recruiter-Friendly

Shows end-to-end data pipeline skills

Demonstrates data cleaning + EDA + visualization

Uses real world, large-scale environmental data

Includes automation, modular scripts, charts, and insights

Clean folder structure & professional documentation

🔮 Future Enhancements

Deploy dashboards using Streamlit

Machine learning:

AQI forecasting

Anomaly detection

Add interactive city comparison tool

Build API for live city AQI lookup

👨‍💻 Author

Abhinav Verma
Aiming for roles in Data Analysis • Data Science • Python Development