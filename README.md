# 🌞 Solar Challenge - Week 0  
**Cross-Country Solar Farm Analysis for MoonLight Energy Solutions**

---

## 📋 Project Overview  
This project analyzes solar farm data from **Benin, Sierra Leone, and Togo** to identify high-potential regions for solar installation. The analysis supports MoonLight Energy Solutions' strategic approach to enhance operational efficiency and sustainability through targeted solar investments.

---

## 🎯 Business Objective  
Perform comprehensive data analysis to provide data-driven recommendations for solar investment strategy, focusing on identifying regions with the highest solar potential aligned with long-term sustainability goals.

---

## 🗂️ Project Structure  
```bash
solar-challenge-week0/
├── .github/workflows/       # CI/CD pipeline
├── app/                     # Streamlit dashboard
│   ├── main.py              # Main dashboard application
│   └── utils.py             # Utility functions
├── data/                    # Solar datasets (gitignored)
├── notebooks/               # Jupyter notebooks for EDA
│   ├── benin_eda.ipynb      # Benin exploratory analysis
│   ├── sierra_leone_eda.ipynb # Sierra Leone analysis
│   └── togo_eda.ipynb       # Togo analysis
├── src/                     # Source code modules
├── tests/                   # Test suites
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## 🚀 Quick Start  

### Environment Setup  
```bash
# Clone repository
git clone https://github.com/Aperca/solar-challenge-week0.git
cd solar-challenge-week0

# Create and activate conda environment
conda create --name solar-env python=3.11 -y
conda activate solar-env

# Install dependencies
pip install -r requirements.txt
```

### Run Jupyter Notebooks  
```bash
jupyter notebook
# Open notebooks/ for exploratory data analysis
```

### Run Dashboard Locally  
```bash
streamlit run app/main.py
```
---
## Dashboard Preview

### Main Dashboard Interface
![Dashboard Main](dashboard_screenshots/dashboard_main.png)

*Interactive dashboard showing solar data comparison across Benin, Sierra Leone, and Togo*

### Country Comparison
![Country Comparison](dashboard_screenshots/country_boxplot_comparison.png)

*Boxplot visualization of GHI distribution across selected countries*

### Time Series Analysis
![Solar Ranking](dashboard_screenshots/time_series_analysis.png)

### Statistical Summary
![Statistics](dashboard_screenshots/dashboard_stats.png)

*Detailed statistics including mean, median, and standard deviation*
## 🧰 Technical Stack  

- **Programming:** Python 3.11+  
- **Data Analysis:** Pandas, NumPy, SciPy  
- **Visualization:** Matplotlib, Seaborn, Plotly  
- **Dashboard:** Streamlit  
- **Version Control:** Git, GitHub Actions CI/CD  
- **Environment:** Conda, Jupyter Notebooks  

---

## 📈 Key Metrics Analyzed  

- **GHI (Global Horizontal Irradiance):** Total solar radiation  
- **DNI (Direct Normal Irradiance):** Direct path solar radiation  
- **DHI (Diffuse Horizontal Irradiance):** Diffused solar radiation  
- **Weather Data:** Temperature, humidity, wind speed, pressure  
- **Sensor Readings:** Module temperatures and performance  

---

## 🎯 Expected Outcomes  

- **Data-Driven Insights:** Identify optimal locations for solar farms  
- **Strategic Recommendations:** Support MoonLight’s investment decisions  
- **Interactive Tools:** Dashboard for ongoing analysis  
- **Reproducible Analysis:** Complete documentation and code  

---

## 👥 Team  
This project is part of the **10 Academy Artificial Intelligence Mastery Program**, focusing on Data Engineering, Financial Analytics, and Machine Learning Engineering tracks.

---

## 📄 License  
This project is for educational purposes as part of the **10 Academy Training Program**.
