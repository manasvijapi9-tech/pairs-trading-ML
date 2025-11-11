"""
Fetch stock price data from Yahoo Finance and save it as CSV.

Usage:
python src/data_fetch.py --tickers "TCS.NS INFY.NS WIPRO.NS HCLTECH.NS" --start 2023-01-01 --end 2025-10-30
"""

import yfinance as yf
import pandas as pd
import argparse
import os

def fetch_data(tickers, start, end):
    """Download adjusted closing prices for given tickers."""
    print(f"📈 Fetching data for: {tickers}")
    # Get the entire OHLCV data
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)
    # Some versions of yfinance return a single-level column index
    if isinstance(data.columns, pd.MultiIndex):
        data = data["Close"]
    else:
        data = data[["Close"]]
    return data

def main():
    parser = argparse.ArgumentParser(description="Fetch stock data from Yahoo Finance")
    parser.add_argument("--tickers", type=str, default="TCS.NS INFY.NS WIPRO.NS HCLTECH.NS",
                        help="Space-separated list of tickers")
    parser.add_argument("--start", type=str, default="2023-01-01",
                        help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, default="2025-10-31",
                        help="End date (YYYY-MM-DD)")
    args = parser.parse_args()

    os.makedirs("data", exist_ok=True)

    tickers = args.tickers.split()
    data = fetch_data(tickers, args.start, args.end)
    output_path = "data/stock_data.csv"
    data.to_csv(output_path)
    print(f"✅ Data saved successfully to {output_path}")

if __name__ == "__main__":
    main()
