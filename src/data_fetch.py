"""
Fetch stock price data from Yahoo Finance and save it as CSV.

Usage (in Colab or terminal):
python src/data_fetch.py --tickers "AAPL MSFT AMZN GOOG TSLA" --start 2018-01-01 --end 2024-12-31
"""

import yfinance as yf
import pandas as pd
import argparse
import os

def fetch_data(tickers, start, end):
    """Download Adjusted Close prices for given tickers and date range."""
    print(f"📈 Fetching data for: {tickers}")
    data = yf.download(tickers, start=start, end=end)["Adj Close"]
    return data

def main():
    # --- Parse command line arguments ---
    parser = argparse.ArgumentParser(description="Fetch stock data from Yahoo Finance")
    parser.add_argument("--tickers", type=str, default="AAPL MSFT AMZN GOOG TSLA",
                        help="Space-separated list of tickers")
    parser.add_argument("--start", type=str, default="2018-01-01",
                        help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, default="2024-12-31",
                        help="End date (YYYY-MM-DD)")
    args = parser.parse_args()

    # --- Ensure data folder exists ---
    os.makedirs("data", exist_ok=True)

    # --- Fetch and save ---
    tickers = args.tickers.split()
    data = fetch_data(tickers, args.start, args.end)
    output_path = "data/stock_data.csv"
    data.to_csv(output_path)
    print(f"✅ Data saved successfully to {output_path}")

if __name__ == "__main__":
    main()
