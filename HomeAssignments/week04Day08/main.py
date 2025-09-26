from HA_DerivClass import Analyzer

filename = "country_wise_latest.csv"

analyes = Analyzer(filename)

#Display total confirmed, death, and recovered cases for each region.
regional_summary = analyes.summary_Count()
print(regional_summary.head())
print("#################################################")

#Exclude entries where confirmed cases are < 10
Filtered_DF = analyes.FilterOutput('Confirmed',10)
print(f"The Filtered Dataframe Output for Excluding Entries below 10:\n\t {Filtered_DF}")

#Identify Region with Highest Confirmed Cases
Highest_Confirmed = analyes.DF_Sort_Ascen('Confirmed',False)
print(f"The Highest Confirmed cases recorded from Listed Country/Region: {Highest_Confirmed.iloc[0,0]}")

#Save sorted dataset into a new CSV file
try:
    Sorted_DF = analyes.DF_Sort_Ascen('Confirmed',True)
    Sorted_DF.to_csv('sorted_DataSet.csv')
    print("CSV File has been created")
except Exception as e:
    print(f"there is some problem in CSV file creation: {e}")

#Top 5 Countries by Case Count
Top5Countries = analyes.DF_Sort_Ascen('Confirmed',False)
print(f"Top 5 Countries are : {list(Top5Countries.iloc[0:6,0])}\n")

#Region with Lowest Death Count
Low_Death = analyes.DF_Sort_Ascen('Deaths',True)
print(f"Lowest Death Count region is: {Low_Death.iloc[0,0]}\n")

#Death-to-confirmed case ratio
D2C_Ratio = analyes.rate_ratio_calcation('Deaths','Confirmed','Death_Confirmed_Ratio')
print(D2C_Ratio[['Country/Region','Death_Confirmed_Ratio']])

#Recovery Rates Across Regions
Reco_Rate = analyes.rate_ratio_calcation('Recovered','Confirmed','RecoveryRate')
print(Reco_Rate[['Country/Region','RecoveryRate']])
print("#########################################")

# #Detect Outliers in Case Counts
outliers = analyes.identify_outliers('Confirmed','outliers_in_Cases')
print(outliers)

#11. Group Data by Country and Region


#12. Identify Regions with Zero Recovered Cases
Recover = analyes.finding_ZeroValueRecord('Recovered')
print(Recover[['Country/Region','Recovered']])



    