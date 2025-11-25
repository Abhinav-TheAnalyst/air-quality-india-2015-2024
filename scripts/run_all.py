import os
import subprocess

scripts = [
    "clean_data.py",
    "analyze_data.py",
    "analyze_stations.py"
    "seasonal_trends.py",
    "city_year_analysis.py",
    "city_comparison_dashboard.py",
    "city_pollution_over_years.py"
    "top_polluted_cities.py",
    "missing_values_report.py",
    "generate_report.py"
]

print("🚀 Running All Scripts...\n")

for script in scripts:
    print(f"▶ Running {script}...")
    path = os.path.join(os.getcwd(), script)
    subprocess.run(["python", path])
    print(f"✔ Done: {script}\n")

print("\n🎉 ALL SCRIPTS COMPLETED SUCCESSFULLY! 🎉")
