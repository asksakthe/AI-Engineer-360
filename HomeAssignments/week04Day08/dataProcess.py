import pandas as pd
import numpy as np


class dataSource:
    def dataFetch(self,filePath):
        self.filePath = filePath
        df = pd.read_csv(self.filePath)
        return df
    

filepath = 'country_wise_latest.csv'
#'/Users/sakthee/Documents/AI/Training_2025/AI-Engineer-360/HomeAssignments/country_wise_latest.csv'
datafile = dataSource()

# Fix: assign the result of dataFetch to 'result' and print its head
result = datafile.dataFetch(filepath)
print(result.head())




