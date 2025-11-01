import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



class CovidEDA:
    def __init__:
        self.data = None
    
    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        print(self.data.head())
        print(self.data.info())

    