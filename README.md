# Pairs Trading Analysis using Python & Machine Learning  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/manasvijapi9-tech/pairs-trading-ML/blob/main/pairs_trading_analysis.ipynb)

### Overview  
This project explores **Pairs Trading**, a real-world strategy used in quantitative finance to find two stocks that usually move together.  
It uses Python, data analysis, and a simple machine learning model to study stock relationships in the **Indian IT sector** — TCS, Infosys, Wipro, and HCLTech.  

I used **real stock data** from **Yahoo Finance (Jan 2023 – Oct 2025)** to analyze patterns, visualize correlations, and predict one stock’s price from another.  

---

## What the Project Does  

| Step | Description |
|------|--------------|
| **1. Fetch Data** | Downloads stock data automatically from Yahoo Finance using Python. |
| **2. Analyze Trends** | Calculates how strongly each stock pair moves together (correlation and cointegration). |
| **3. Visualize** | Creates heatmaps and scatter plots to show relationships clearly. |
| **4. Predict with ML** | Uses Linear Regression to model Infosys’s price using TCS’s price. |
| **5. Evaluate** | Prints accuracy (R² score) and shows predicted vs actual price plots. |

---

##  Tools & Libraries  
Python · Pandas · NumPy · Matplotlib · Scikit-learn · Statsmodels · yFinance · Google Colab · GitHub  

---

##  Example Results  

**Correlation Findings:**  
- TCS & Infosys have the strongest correlation (~0.88)  
- Wipro and HCLTech also move closely with them  

**Machine Learning Model Output:**  
| Metric | Result |
|--------|---------|
| **R² Score (TCS → INFY)** | 0.87 |
| **Mean Squared Error** | 250.45 |

- The model explains about **87% of Infosys’s price movement** based on TCS’s prices.

---

## How to Run

You can run this project in **Google Colab** or your local terminal.

### In Google Colab
```bash
!git clone https://github.com/manasvijapi9-tech/pairs-trading-ML.git
%cd pairs-trading-ML
!pip install -r requirements.txt
!python src/data_fetch.py
!python src/train_model.py


## Why This Project Matters  
This project helped me understand how **data science connects with finance** — how to collect real data, clean it, analyze relationships, and make small predictions using ML.  
It’s a practical example of combining **finance, coding, and statistics** to understand real-world market behavior.  

---




## Stocks & Time Period

Stocks:
TCS.NS, INFY.NS, WIPRO.NS, HCLTECH.NS
Time Period: Jan 2023 → Oct 2025
Source: Yahoo Finance


## Author

Manasvi Japi
Student — Interested in Quantitative Finance and Data Science
Pairs Trading ML Project (2025)

