import pandas_datareader.data as web
import datetime
import pandas as pd

start = datetime.datetime(2011, 1, 1)
end = datetime.datetime(2016, 3, 3)

#symbols = pd.read_csv("./PIMCO Funds.csv", header=None)

symbols = [['PIMCO ALL ASSET C', 'PASCX'], 
           ['PIMCO CA INTERMEDIATE MUNI BOND C','PCFCX']]

data = {}

for name, symbol in symbols:
    ohlc = web.DataReader("PASCX", 'yahoo', start, end)
    data[symbol] = ohlc

print (data['PASCX'])