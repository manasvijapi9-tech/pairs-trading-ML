"""
Train a simple Machine Learning model for pairs trading prediction.
Predicts one stock's price using another stock's price as input.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os

# Make sure the data folder exists
DATA_PATH = "data/stock_data.csv"
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError("Run data_fetch.py first to create data/stock_data.csv")

# Load data
data = pd.read_csv(DATA_PATH, index_col=0, parse_dates=True)
data = data.dropna()

# Pick your pair (you can change this anytime)
x_ticker = "TCS.NS"
y_ticker = "INFY.NS"

if x_ticker not in data.columns or y_ticker not in data.columns:
    raise ValueError(f"Tickers {x_ticker} or {y_ticker} not found in data. Available: {list(data.columns)}")

X = data[[x_ticker]].values
y = data[y_ticker].values

# Split 80% train, 20% test
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Model trained to predict {y_ticker} using {x_ticker}")
print(f"Mean Squared Error: {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Plot predicted vs actual
plt.figure(figsize=(7,5))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title(f"{y_ticker} Predicted vs Actual ({x_ticker} as predictor)")
plt.grid(True)
plt.tight_layout()
plt.savefig("data/prediction_plot.png")
plt.show()

print("✅ Plot saved to data/prediction_plot.png")
