#Header start
__author__ = "Arthur Pendragon De Simone"
__license__ = "GPL"
__version__ = "0.1.0"
__email__ = "arthurpdesimone@gmail.com"
__status__ = "Production"
__description__ = "Stock trader python software"
#Header end

#Dependencies start
from alpha_vantage.timeseries import TimeSeries
from pathlib import Path
from stock import *
from trader import *
import time
#Dependencies end
#Start counting time
start_time = time.time()
#Simple method to print a line
def print_line():
    print('# ' + '=' * 78)
#Header print start
print_line()
print('Author: ' + __author__)
print('Version: ' + __version__)
print('Description: ' + __description__)
print_line()
#Header print end
#Read API key
api_key = Path('api.txt').read_text()
#Load tickers
ticker_file = Path('stocks.txt')
tickers = ticker_file.read_text().splitlines()
print('Loading tickers')
print(tickers)
print_line()
#Initialize objects
ts = TimeSeries(key = api_key,  output_format="pandas")
stock = stock()
trader = trader()
#Loop through tickers
for ticker in tickers:
    #Download data for ticker
    print('Downloading '+ticker)
    data, meta_data = ts.get_daily(ticker, outputsize = 'full')
    #Sleep time necessary due to API restrictions of 5 calls per minute
    if len(tickers) > 1 : 
        time.sleep(12)
    #Store data retrieved
    stock.put_dataframe(ticker,data)
    #Calculate MACD
    stock.calculateMACD(ticker,12,26,9)
    #Calculate RSI
    stock.calculateRSI(ticker,14)
    #Calculate SMA
    stock.calculateSMA(ticker,25)
    #Clear NaN
    stock.clearNaN()
#Save all the data
stock.save_database()
#Print whole database
stock.print_database()
#End script time
trader.perform_trades(stock)
end_time = time.time()
print('Elapsed time :',end_time-start_time,'s')