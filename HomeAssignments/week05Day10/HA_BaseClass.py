import pandas as pd
import numpy as np
import os


class Data_Pro:
    def __init__(self, fileName):
        # fi = os.getcwd()
        # print(fi)
        # self.fileName = fileName
        # #input(f"Is dataSet are present in Source Folder, if yes please enter your dataset name: ")
        # filepath = fi + '/' + fileName
        # print(filepath)
        self.fileName = fileName
        try:
            if self.fileName:
                print("inside if")
                self.df = pd.read_csv(self.fileName)
                print(f"Dataframes df are created Successfully: {self.df.shape}")
                #return self.df
            else:
                print("File path is not correct, please check once")
                return None
        except Exception as e:
            print("Dataset is not available in the path, Check and proceed")


proc = Data_Pro('country_wise_latest.csv')
#print(proc.df.head())

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




