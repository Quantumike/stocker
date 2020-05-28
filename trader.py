#Dependencies start
from stock import * 
import pandas as pd
#Dependencies end
#Class definition
class trader():
    def perform_trades(self, stock):
        #Create an empty dataframe
        df = pd.DataFrame()
        #Loop through the database
        for ticker in stock.get_database().keys():
            #Simple stock among dictionary
            stock = stock.get_database()[ticker]
            #MACD Crossover detected
            df['macd_crossover'] = stock['5. MACDLine'] > stock['6. MACDSignal']
            #If RSI is below a certain trigger
            df['rsi_buy'] = stock['8. RSI'] < 50
            #If close is over SMA, buy stock
            df['sma_crossover'] = stock['4. close'] > stock['9. SMA']

            df_buy = df.query('macd_crossover == True and rsi_buy == True and sma_crossover == True')
            df_sell = df.query('macd_crossover == False and rsi_buy == False and sma_crossover == False')
            frames= [df_buy,df_sell,stock['4. close']]
            result = pd.concat(frames,axis=0)
            result.sort_index(inplace=True)
            result = result.groupby('date').first()
            result.to_csv('result.csv')
