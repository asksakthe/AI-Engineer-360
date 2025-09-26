from HA_BaseClass import Data_Pro

class Analyzer(Data_Pro):
    def __init__(self,fileN):
        super().__init__(fileN)


    def summary_Count(self):
        grp = self.df.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered']]
        return grp.sum()
    
    #method to return the confirmed cases which is not more than 10
    def FilterOutput(self,target_Col, target_val):
        self.df_Filtered = self.df[self.df[target_Col]> target_val]
        return self.df_Filtered

    #Identify Region with Highest Confirmed Cases
    def DF_Sort_Ascen(self,target_col, bool):
        self.target_col = target_col
        self.bool = bool
        self.sorted_df = self.df.sort_values(by=self.target_col, ascending=self.bool)
        return self.sorted_df
    
    def convert_CSV(self, data):
        #Sort Data by Confirmed Cases
        # Save sorted dataset into a new CSV file.
        try:
            self.data = data
            self.csv_Out = self.dataF.to_csv('Sorted_Confirmed.csv')
            if self.csv_Out:
                return f"CSV file has been created!!"
        except Exception as e:
            return f"Problem in conversion, {e}"
        
    def rate_ratio_calcation(self,target_col1, target_col2,col_name):
        self.col_name = col_name
        self.target_col1 = target_col1
        self.target_col2 = target_col2
        self.df[col_name] = (self.df[self.target_col1] /self.df[self.target_col2])*100
        return self.df
    
    def identify_outliers(self,target_col,col_Name):
        self.col_Name = col_Name
        self.target_col = target_col

        mean_value = self.df[self.target_col].mean()
        std_value = self.df[self.target_col].std()

        upper_bound = mean_value + (2*std_value)
        lower_bound = mean_value - (2*std_value)

        self.df[self.col_name] = (self.df[target_col] < upper_bound) | (self.df[target_col] > lower_bound)
        return self.df
    
    def finding_ZeroValueRecord(self,target_col):
        self.target_col = target_col
        self.new_df = self.df[self.df[self.target_col] == 0]
        return self.new_df




    

# chi_obj = Analyzer('Sorted_Confirmed.csv')
# ser_obj = chi_obj.removed_ZeroValueRecord('Recovered')

        