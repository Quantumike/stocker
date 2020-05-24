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
    def calculateMACD(self):
        for key in self.database.keys():
            print(self.database[key].ewm(14).mean())
    #Method to store all
    def save_database(self):
        #Save in csv output
        for key in self.database.keys():
            self.database[key].to_csv('database/'+key+'.csv')
    