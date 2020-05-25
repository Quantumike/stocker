#Dependencies start
import numpy
#Dependencies end
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
    def calculateMACD(self, fast, slow, signal):
        for key in self.database.keys():
            #Calculating MACD slow, fast and signal for column 4. close at database
            print('calculating MACD for '+key)
            emaFast = self.database[key]['4. close'].ewm(span=fast).mean()
            emaSlow = self.database[key]['4. close'].ewm(span=slow).mean()
            #Definition of MACD
            macd = emaFast - emaSlow
            #Signal line calculation
            signal = macd.ewm(span=signal).mean()
            #Adding to the database all the elements of MACD
            self.database[key]['5. MACDLine'] = macd
            self.database[key]['6. MACDSignal'] = signal
            macdHistogram = macd - signal
            self.database[key]['7. MACDHistogram'] = macdHistogram
    #Method to store all
    def save_database(self):
        #Save in csv output
        for key in self.database.keys():
            self.database[key].to_csv('database/'+key+'.csv')
    