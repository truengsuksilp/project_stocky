from numpy.core.records import array
import pandas as pd
import numpy as np
from alpha_vantage.timeseries import TimeSeries

# Config Alpha Vantage with Mock inputs
# key_1 = "3P9NBZQR6NNO2VEF" -- used up?
# key_2 = "950I7MY0U1NO6MUA" -- ok

ts = TimeSeries(key="3P9NBZQR6NNO2VEF")
portfolio = {
    "tickers": ["MSFT", "AAPL", "GOOGL"]
}

#####################
# TEST API: 1 stock #
#####################

# # Static Test
# data, _ = ts.get_daily_adjusted("MSFT")
# price_ticker = data['2021-12-01']['5. adjusted close']
# print(f'MSFT: {price_ticker}')

# Function Test
def last_price_data(ticker):
    ts = TimeSeries(key="3P9NBZQR6NNO2VEF")
    data, _ = ts.get_daily_adjusted(ticker)
    
    price_ticker = data['2021-12-01']['5. adjusted close']
    message = f'{ticker}: {price_ticker}'
    
    return message

############
# GET data #
############

# FUNCTION: Get data
def get_price_full(ticker):
    data, _ = ts.get_daily_adjusted(ticker, 'full')
    return data

# GET JSON DATA INTO A DICTIONARY: {ticker: {}, ticker: {}}
arr = portfolio["tickers"]

def get_hist_prices(tickers: array):
    stocks_hist_prices = {}

    # TEST ONLY
    # tickers_array = []

    for ticker in tickers: 
        price_array = get_price_full(ticker)
        print(ticker)
        
        # TEST ONLY
        # tickers_array.append(ticker)

        stocks_hist_prices[ticker] = price_array
    
    # TEST ONLY
    # return tickers_array
    return stocks_hist_prices


# Dataframes: Create an array of data tables
def get_data_frames(stocks_hist_prices):
    data_frames = []

    # TEST ONLY
    tickers_array = []

    for stock in stocks_hist_prices:

        df = pd.DataFrame.from_dict(stocks_hist_prices[stock], orient='index')

        # Post-Processing: Table: ticker | adj_close, Data Limit: 1 year
        df = df[:250]
        df['ticker'] = stock
        df = df[['ticker','5. adjusted close']]

        df.rename(columns={'5. adjusted close': 'adj_close'}, inplace=True, errors='raise')
        df['adj_close'] = df['adj_close'].astype('float64')

        data_frames.append(df)

    return tickers_array

# # Dataframes: Create df_merge - a LONG table from merging individual stock tables
# df_merged = pd.concat(data_frames)
# df_merged.reset_index(inplace=True)
# df_merged.rename(columns= {"index": "date"}, inplace=True, errors='raise')

# # Summary Table: Generate table of daily and annual returns
# df_pivot = df_merged.pivot(index='date', columns='ticker')
# returns_daily = df_pivot.pct_change()
# returns_annual = returns_daily.mean() * 250

# # VERIFY: Try before simulate
# # print(returns_annual)

# ##############
# # SIMULATION #
# ##############

# # SIMULATION Config: get daily and covariance of returns of the stock
# cov_daily = returns_daily.cov()
# cov_annual = cov_daily * 250

# port_returns = []
# port_volatility = []
# stock_weights = []

# num_assets = len(portfolio["tickers"])
# num_portfolios = 50000

# # SIMULATION: populate the empty lists with each portfolios returns,risk and weights
# for single_portfolio in range(num_portfolios):
#     weights = np.random.random(num_assets)
#     weights /= np.sum(weights)
    
#     returns = np.sum(weights * returns_annual)
#     volatility = np.sqrt(np.dot(weights.T, np.dot(cov_annual, weights)))

#     port_returns.append(returns)
#     port_volatility.append(volatility)
#     stock_weights.append(weights)

# # SUMMARY STATS: Generate a dictionary and dataframe of risk and return for each portfolio

# # Summary Dictionary
# portfolio_stats = {'Returns': port_returns,
#              'Volatility': port_volatility}

# for counter,symbol in enumerate(portfolio["tickers"]):
#     portfolio_stats[symbol+' Weight'] = [Weight[counter] for Weight in stock_weights]

# # Summary Table: get better labels for desired arrangement of columns
# df = pd.DataFrame(portfolio_stats)
# column_order = ['Returns', 'Volatility'] + [stock+' Weight' for stock in portfolio["tickers"]]
# df = df[column_order]

# ##################
# # RECOMMENDATION #
# ##################

# # Get row with highest risk over return
# df['sharpe_ratio'] = df['Returns']/df['Volatility']
# max_index = df['sharpe_ratio'].idxmax()
# max_row = df.iloc[max_index]

# # Test
# print(max_row)