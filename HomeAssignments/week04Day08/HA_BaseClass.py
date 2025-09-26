import pandas as pd
import numpy as np
import os

class Data_Pro:
    def __init__(self, fileName):
        fi = os.getcwd()
        self.fileName = fileName
        #input(f"Is dataSet are present in Source Folder, if yes please enter your dataset name: ")
        filepath = fi + '/' + fileName
        #print(filpath)
        try:
            if filepath:
                self.df = pd.read_csv(filepath)
                print(f"Dataframes df are created Successfully")
                # df
        except Exception as e:
            print("Dataset is not available in the path, Check and proceed")


proc = Data_Pro('Sorted_Confirmed.csv')

# class dataSource:
#     def dataFetch(self,fileName):
#         self.filePath = fi + fileName
#         df = pd.read_csv(self.filePath)
#         return df
    

# #filepath = 'country_wise_latest.csv'
# #'/Users/sakthee/Documents/AI/Training_2025/AI-Engineer-360/HomeAssignments/country_wise_latest.csv'
# datafile = dataSource()

# # Fix: assign the result of dataFetch to 'result' and print its head
# result = datafile.dataFetch(filepath)
# print(result.head())




