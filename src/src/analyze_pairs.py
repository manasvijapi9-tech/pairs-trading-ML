import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(ticker):
    filename = f"data_{ticker}.csv"
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} not found. Please run data_fetch.py first.")
    return pd.read_csv(filename)

def calculate_returns(df):
    df["Return"] = df["Close"].pct_change()
    return df.dropna()

def compare_stocks(ticker1, ticker2):
    df1 = calculate_returns(load_data(ticker1))
    df2 = calculate_returns(load_data(ticker2))
    
    merged = pd.merge(df1[["Date", "Return"]], df2[["Date", "Return"]],
                      on="Date", suffixes=(f"_{ticker1}", f"_{ticker2}"))
    
    corr = merged[f"Return_{ticker1}"].corr(merged[f"Return_{ticker2}"])
    print(f"Correlation between {ticker1} and {ticker2}: {corr:.2f}")
    
    plt.figure(figsize=(10, 5))
    plt.scatter(merged[f"Return_{ticker1}"], merged[f"Return_{ticker2}"], alpha=0.6)
    plt.title(f"Return Correlation: {ticker1} vs {ticker2} ({corr:.2f})")
    plt.xlabel(f"{ticker1} Returns")
    plt.ylabel(f"{ticker2} Returns")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example comparison between Apple and Microsoft
    compare_stocks("AAPL", "MSFT")
