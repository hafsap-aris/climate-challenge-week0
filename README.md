# Climate Challenge - Week 0

## Setup Instructions
1. **Clone the repository:**
   `git clone https://github.com/[your-username]/climate-challenge-week0.git`
2. **Create a virtual environment:**
   `python -m venv venv`
3. **Activate the environment:**
   - Windows: `.\venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. **Install dependencies:**
   `pip install -r requirements.txt`

# African Climate Vulnerability Analysis & Dashboard

## Project Overview
This project provides a data-driven comparative analysis of climate trends across five African nations: **Ethiopia, Kenya, Nigeria, Sudan, and Tanzania**. 

The primary objective is to equip the **Ethiopian Ministry of Water and Energy** with "negotiation-grade" evidence for the **COP32** summit. By synthesizing a decade of meteorological data (2015–2026), this study identifies specific regional vulnerabilities—ranging from extreme thermal stress in Sudan to high precipitation volatility in Ethiopia and Tanzania—to support targeted climate finance requests.

---

## Technical Stack
- **Language:** Python 3.13
- **Data Engineering:** Pandas, NumPy
- **Statistical Analysis:** SciPy (One-way ANOVA)
- **Visualization:** Plotly Express, Seaborn, Matplotlib
- **Web Framework:** Streamlit
- **Version Control:** Git / GitHub

---

## Repository Structure
```text
├── app/
│   ├── main.py          # Streamlit dashboard application
├── data/                # Cleaned datasets (locally stored / gitignored)
│   ├── master_climate_data.csv
├── notebooks/
│   ├── compare_countries.ipynb  # Main analysis, ANOVA, and synthesis
├── requirements.txt     # Production dependencies
└── README.md            # Project documentation
```



## 1. Objective: The Mission for Negotiation
The primary objective of this project is to provide the Ethiopian Ministry with **negotiation-grade climate evidence** to support regional funding requests at the upcoming COP32 summit. By synthesizing a decade of meteorological data (2015–2026) across Ethiopia, Kenya, Nigeria, Sudan, and Tanzania, I have identified specific climate vulnerabilities that justify targeted international financial support.

---


## 2. Executive Summary of Regional Findings
My analysis reveals that while the East African region faces a shared climate crisis, the specific threats are highly localized. Sudan is the regional "hotspot" for extreme heat, while Tanzania and Nigeria face the highest risks from precipitation volatility. Ethiopia, conversely, occupies a unique niche as a highland region with high rainfall variability despite lower average temperatures.

---

## 3. Data-Backed Vulnerability Ranking
Using evidence gathered from my automated cleaning and analysis pipeline, I have ranked the five nations by their primary climate threat profiles:

| Rank | Country | Primary Climate Threat | Supporting Evidence |
| :--- | :--- | :--- | :--- |
| **1** | **Sudan** | **Extreme Aridity & Heat** | Highest mean temperature (**28.76°C**) and lowest cumulative rainfall (**2645.04 mm**). |
| **2** | **Tanzania** | **Precipitation Volatility** | Highest rainfall standard deviation (**8.00**), indicating extreme flood/drought cycles. |
| **3** | **Nigeria** | **Hydrological Stress** | Highest cumulative rainfall (**17310.76 mm**) paired with high volatility (**7.27 std**). |
| **4** | **Ethiopia** | **Water Resource Instability** | Lowest mean temperature (**16.07°C**) but high rainfall standard deviation (**6.29**). |
| **5** | **Kenya** | **Moderate Thermal Rise** | Consistent warming trend but lower volatility compared to its northern neighbors. |

---

## 4. Key Analytical Insights & COP32 Recommendations
Based on the synthesis of NASA POWER data, I provide the following 5 strategic observations for the Ministry's position paper:

1.  **Warming Trends:** **Sudan** is warming fastest and most dangerously. With a max temperature reaching **37.99°C**, it faces a severe risk of desertification that threatens regional stability.
2.  **Unstable Precipitation:** **Tanzania** and **Nigeria** possess the most unpredictable rainfall patterns. This volatility necessitates infrastructure grants specifically for flood-resilient agriculture.
3.  **Extreme Heat Stress:** **Sudan** recorded **41 extreme heat days** (>35°C) in 2015 alone. This frequency confirms that Sudan is the regional leader in climate-driven health and agricultural stress.
4.  **Ethiopia’s Comparative Profile:** Unlike its neighbors, Ethiopia’s threat is not raw heat, but **water predictability**. Its rainfall standard deviation is nearly double that of Sudan, making Ethiopia uniquely vulnerable to seasonal shifts despite its cooler climate.
5.  **Policy Recommendation:** Ethiopia should champion **Sudan** for priority climate finance. The data proves Sudan is a "double-threat" zone—hottest and driest—making its agricultural failure a direct risk to Ethiopia’s regional food security.

---

## 5. Technical Validation
To ensure these recommendations are scientifically sound, I performed a **One-way ANOVA test** on the temperature variables. The resulting **p-value (< 0.05)** statistically confirms that the variations in climate between these five countries are significant and not due to random fluctuations, providing the "negotiation-grade" certainty required for COP32.

---

## 6. Interactive Visualization Strategy
To facilitate data exploration for Ministry officials, I deployed an interactive dashboard with the following features:
* **Country Multi-select:** Allows side-by-side comparison of specific regional blocks.
* **Metric Selector:** Toggles between Temperature (T2M), Precipitation (PRECTOTCORR), and Relative Humidity (RH2M).
* **Timeline Zoom:** Enables officials to focus on specific years of extreme weather events.

---
