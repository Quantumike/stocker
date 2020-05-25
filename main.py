#Header start
__author__ = "Arthur Pendragon De Simone"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "arthurpdesimone@gmail.com"
__status__ = "Production"
__description__ = "Stock trader python software"
#Header end

#Dependencies start
from alpha_vantage.timeseries import TimeSeries
from pathlib import Path
from gui import *
from stock import *
import time
#Dependencies end

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
#Loop through tickers
for ticker in tickers:
    #Download data for ticker
    data, meta_data = ts.get_daily(ticker, outputsize = 'full')
    print('Downloading '+ticker)
    #Sleep time necessary due to API restrictions of 5 calls per minute
    time.sleep(12)
    #Store data retrieved
    stock.put_dataframe(ticker,data)
    #Save all the data
    stock.save_database()
#Plot EMA
stock.calculateMACD(12,26,9)
#Print whole database
stock.print_database()

#Show interface
#g = GUI()
#window = g.showGUI()
#g.plotmatplot(window)
#window.mainloop()


def _quit():
    window.quit()       # stops mainloop
    window.destroy()    # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

