"""
Analyze fetched stock data for correlations and cointegration.
Reads: data/stock_data.csv
Outputs:
 - prints correlation matrix summary and top correlated pairs
 - saves data/corr_matrix.csv
 - displays (and saves) two plots:
    - correlation heatmap -> data/corr_heatmap.png
    - scatter of top correlated pair -> data/top_pair_scatter.png
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from statsmodels.tsa.stattools import coint

plt.rcParams["figure.figsize"] = (8, 5)

DATA_PATH = "data/stock_data.csv"
os.makedirs("data", exist_ok=True)

def load_prices(path=DATA_PATH):
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    # if multi-level columns (Close for each ticker) collapse to single level
    if isinstance(df.columns, pd.MultiIndex):
        # try to pick 'Close' level if present, else first level
        if "Close" in df.columns.levels[0]:
            df = df["Close"]
        else:
            df = df.iloc[:, df.columns.get_level_values(1) == "Close"]
    # ensure numeric
    df = df.apply(pd.to_numeric, errors="coerce")
    df = df.dropna(axis=1, how="all")
    return df

def compute_returns(prices):
    return prices.pct_change().dropna()

def corr_matrix(returns):
    return returns.corr()

def top_pairs_from_corr(corr_df, top_n=5):
    pairs = []
    tickers = corr_df.columns
    for i in range(len(tickers)):
        for j in range(i+1, len(tickers)):
            pairs.append((tickers[i], tickers[j], corr_df.iloc[i,j]))
    pairs = sorted(pairs, key=lambda x: -abs(x[2]))
    return pairs[:top_n]

def test_cointegration(prices, pair):
    a, b = pair
    s1 = prices[a].dropna()
    s2 = prices[b].dropna()
    # align
    df = pd.concat([s1, s2], axis=1).dropna()
    score, pvalue, _ = coint(df.iloc[:,0], df.iloc[:,1])
    return pvalue, score

def plot_heatmap(corr_df, outpath="data/corr_heatmap.png"):
    fig, ax = plt.subplots(figsize=(8,6))
    im = ax.imshow(corr_df.values, vmin=-1, vmax=1)
    ax.set_xticks(np.arange(len(corr_df.columns)))
    ax.set_yticks(np.arange(len(corr_df.index)))
    ax.set_xticklabels(corr_df.columns, rotation=45, ha="right")
    ax.set_yticklabels(corr_df.index)
    plt.colorbar(im, ax=ax, fraction=0.03)
    plt.title("Return Correlation Matrix")
    plt.tight_layout()
    fig.savefig(outpath)
    plt.show()

def plot_scatter_for_pair(returns, pair, outpath="data/top_pair_scatter.png"):
    a, b = pair
    x = returns[a]
    y = returns[b]
    plt.figure(figsize=(7,5))
    plt.scatter(x, y, alpha=0.6)
    plt.axhline(0, linewidth=0.5)
    plt.axvline(0, linewidth=0.5)
    plt.xlabel(f"{a} daily returns")
    plt.ylabel(f"{b} daily returns")
    plt.title(f"Scatter: {a} vs {b}")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(outpath)
    plt.show()

def main():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"{DATA_PATH} not found. Run src/data_fetch.py first.")
    prices = load_prices()
    print("Loaded prices for tickers:", list(prices.columns))
    returns = compute_returns(prices)
    corr = corr_matrix(returns)
    corr.to_csv("data/corr_matrix.csv")
    print("\nSaved correlation matrix -> data/corr_matrix.csv")
    top_pairs = top_pairs_from_corr(corr, top_n=5)
    print("\nTop correlated pairs (abs correlation):")
    for a,b,val in top_pairs:
        print(f"  {a} - {b} : corr = {val:.3f}")
    # cointegration tests on top 3 pairs
    print("\nCointegration test p-values on top 3 pairs:")
    for a,b,_ in top_pairs[:3]:
        pval, score = test_cointegration(prices, (a,b))
        print(f"  {a} & {b} -> p-value = {pval:.4f}, score = {score:.3f}")
    # plots
    plot_heatmap(corr, outpath="data/corr_heatmap.png")
    top_pair = (top_pairs[0][0], top_pairs[0][1])
    plot_scatter_for_pair(returns, top_pair, outpath="data/top_pair_scatter.png")
    print("\nPlots saved -> data/corr_heatmap.png, data/top_pair_scatter.png")

if __name__ == "__main__":
    main()
