#Class definition
class stock():
    #Initialize class
    def __init__(self):
        self.database = {}
    #Method to print a simple line
    def print_line(self):
        print('# ' + '=' * 78)
    #Method to print whole database
    def print_database(self):
        #Iterate over database
        for key in self.database.keys():
            self.print_line()
            print(key)
            print(self.database[key])
    #Method to store a record at database
    def put_dataframe(self,ticker,data_frame):
        self.database[ticker] = data_frame
    #Calculate MACD for database
    def calculateMACD(self, key, fast, slow, signal):
        #Calculating MACD slow, fast and signal for column 4. close at database
        #Reverse the order of the dates so pandas can calculates EMAs properly
        self.database[key] = self.database[key].sort_index()
        #Calculate EMAfast and EMAslow of a given ticker
        emaFast = self.database[key]['4. close'].ewm(span=fast, adjust = False).mean()
        emaSlow = self.database[key]['4. close'].ewm(span=slow, adjust = False).mean()
        #Definition of MACD
        macd = emaFast - emaSlow
        #Signal line calculation
        signal = macd.ewm(span=signal, adjust = False).mean()
        #Adding to the database all the elements of MACD
        self.database[key]['5. MACDLine'] = macd
        self.database[key]['6. MACDSignal'] = signal
        #Calculate the histogram
        macdHistogram = macd - signal
        self.database[key]['7. MACDHist'] = macdHistogram

    def calculateRSI(self,ticker,period):
        close = self.database[ticker]['4. close']
        # Get the difference in price from previous step
        delta = close.diff()
        # Get rid of the first row, which is NaN since it did not have a previous 
        # row to calculate the differences
        delta = delta[1:]
        # Make the positive gains (up) and negative gains (down) Series
        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0
        # Calculate the EWMA
        roll_up = up.ewm(com=period-1, adjust=False).mean()
        roll_down = down.abs().ewm(com=period-1, adjust=False).mean()
        # Calculate the RSI based on EWMA
        RS1 = roll_up / roll_down
        RSI = 100.0 - (100.0 / (1.0 + RS1))
        #Store at the database
        self.database[ticker]['8. RSI'] = RSI
    #Method to calculate SMA
    def calculateSMA(self,ticker,period):
        self.database[ticker]['9. SMA'] = self.database[ticker]['4. close'].rolling(window=period).mean()
    #Method clear database from NaN values
    def clearNaN(self):
        for key in self.database.keys():
            self.database[key].dropna(how='any',inplace=True)
    #Method to store all
    def save_database(self):
        #Save in csv output
        for key in self.database.keys():
            self.database[key].to_csv('database/'+key+'.csv')
    #Acessor method to database
    def get_database(self):
        return self.database