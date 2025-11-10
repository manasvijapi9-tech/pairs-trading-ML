import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

def load_data(ticker1, ticker2):
    f1, f2 = f"data_{ticker1}.csv", f"data_{ticker2}.csv"
    if not os.path.exists(f1) or not os.path.exists(f2):
        raise FileNotFoundError("Data files not found. Run data_fetch.py first.")
    df1, df2 = pd.read_csv(f1), pd.read_csv(f2)
    merged = pd.merge(df1[["Date","Close"]], df2[["Date","Close"]], on="Date",
                      suffixes=(f"_{ticker1}", f"_{ticker2}"))
    return merged

def train_model(ticker1="AAPL", ticker2="MSFT"):
    df = load_data(ticker1, ticker2)
    X = df[[f"Close_{ticker1}"]].values
    y = df[f"Close_{ticker2}"].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    print(f"Model trained to predict {ticker2} from {ticker1}")
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R² Score: {r2:.4f}")

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, f"models/pairs_model_{ticker1}_{ticker2}.pkl")
    print("Model saved successfully.")

if __name__ == "__main__":
    train_model("AAPL", "MSFT")
