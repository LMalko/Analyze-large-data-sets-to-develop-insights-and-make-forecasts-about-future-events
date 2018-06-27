import pandas as pd

# Prevent 'is_list_like' error.
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data, wb

import numpy as np
import datetime
import matplotlib.pyplot as plt



df = pd.read_pickle('all_banks')
# print(df)

# 1. Stock data from Jan 1st 2006 to Jan 1st 2016 for each
# of the banks. Each bank to be a separate dataframe,
# with the variable name for that bank being its ticker
# symbol.

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

# 'google' & 'yahoo' API are seem to be deprecated,
# using 'quandl'.

# Bank of America
BAC = data.DataReader("BAC", 'quandl', start, end)
# CitiGroup
C = data.DataReader("C", 'quandl', start, end)
# Goldman Sachs
GS = data.DataReader("GS", 'quandl', start, end)
# JPMorgan Chase
JPM = data.DataReader("JPM", 'quandl', start, end)
# Morgan Stanley
MS = data.DataReader("MS", 'quandl', start, end)
# Wells Fargo
WFC = data.DataReader("WFC", 'quandl', start, end)

# df1 = data.DataReader(['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC'],
#                      'quandl', start, end)
# print(BAC)

# 2. Tickers in alphabetical order. The bank dataframes
# concatenated together to a single data frame called
# bank_stocks.
# The keys argument equal to the tickers list.

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC],
                        axis=1, keys=tickers)

bank_stocks.columns.names = ["Bank Ticker",
                             "Stock Info"]

print(bank_stocks.head())