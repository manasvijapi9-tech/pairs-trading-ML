# Pairs Trading + ML Signals

Detects cointegrated stock pairs, trains a RandomForest to time mean-reversion entries/exits, and backtests the strategy.

## How to run
1. `pip install -r requirements.txt`
2. `python src/data_fetch.py --tickers "AAPL MSFT AMZN GOOG TSLA" --start 2018-01-01 --end 2024-12-31`
3. `python src/features.py data/prices.csv`
4. `python src/model.py data/features.csv`
5. `python src/backtest.py data/features_with_preds.csv`

## Files
- `src/` — code modules (data_fetch, features, model, backtest, utils)
- `data/` — input/output CSVs
- `notebooks/` — analysis & charts

## Notes
This is a student project; backtest assumptions are simplified (close-to-close fills, simple transaction cost model).
