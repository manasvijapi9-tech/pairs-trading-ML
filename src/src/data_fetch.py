import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


def fetch_stock_data(ticker, period="1y"):
    """
    Fetch historical data for a given stock ticker using yfinance.
    Returns a pandas DataFrame.
    """
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, period=period, progress=False)
    data.reset_index(inplace=True)
    return data


if __name__ == "__main__":
    # Example: Fetch data for Apple and Microsoft
    tickers = ["AAPL", "MSFT"]
    for ticker in tickers:
        df = fetch_stock_data(ticker)
        filename = f"data_{ticker}.csv"
        df.to_csv(filename, index=False)
        print(f"Saved {filename}")
