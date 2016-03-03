import pandas_datareader.data as web
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2016, 3, 3)

print('--> Reading symbol data')
symbols = pd.read_csv("./PIMCO Funds.csv", header=None)

data = {}

print("--> reading price data")
for index, row in symbols.iterrows():
    symbol = row[1]
    print("--> reading", symbol)
    try:
        ohlc = web.DataReader(symbol, 'yahoo', start, end)
        data[symbol] = ohlc
    except:   
        print(symbol, "not readable----------------<")

print("--> finished reading price data")

print("--> plotting data")

data['PASCX']['Close'].plot()
plt.show()