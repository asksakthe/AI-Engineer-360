from HA_DerivClass import Analyzer
import matplotlib.pyplot as plt
import pandas as pd

class CovidVisualization(Analyzer):
    # Initialization
    # def __init__(self,fileIN):
    #     super().__init__(fileIN )
    def __init__(self,fileIN):
        super().__init__(fileIN)

        
    # Bar chart visualization
    def view_Barchart(self,x_col,y_col,title,xlabel,ylabel):
        self.x_col = x_col
        self.y_col = y_col
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

        plt.figure(figsize=(10,6))
        plt.bar(self.df[self.x_col], self.df[self.y_col], color='skyblue')
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Pie chart visualization
    def view_Piechart(self, target_col, col_name):
        self.target_col = target_col
        self.col_name = col_name

        pie_data = self.df[self.target_col].value_counts()
        plt.figure(figsize=(8,8))
        plt.pie(pie_data,labels=pie_data.index,autopct='%1.1f%%',startangle=140)
        plt.title(self.col_name)
        plt.axis('equal')
        plt.show()

    # Line Cahrt visualization
    def view_Linechart(self,x_col,y_col,title,xlabel,ylabel):
        self.x_col = x_col
        self.y_col = y_col
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        plt.figure(figsize=(10,6))
        plt.plot(self.df[self.x_col],self.df[self.y_col],marker='o',color='green')
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.xticks(rotation=45)

    def view_Histogram(self,target_col,bins,col_name):
        self.target_col = target_col
        self.bins = bins
        self.col_name = col_name

        plt.figure(figsize=(10,6))
        plt.hist(self.df[self.target_col],bins=self.bins,color='orange',edgecolor='black')
        plt.title(self.col_name)
        plt.xlabel(self.target_col)
        plt.ylabel('Frequency')
        plt.show()

    def view_Scatterplot(self,x_col,y_col,title,xlabel,ylabel):
        self.x_col = x_col
        self.y_col = y_col
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

        plt.figure(figsize=(10,6))
        plt.scatter(self.df[self.x_col],self.df[self.y_col],color='purple')
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
    
    def view_Boxplot(self,target_col,col_name):
        self.target_col = target_col
        self.col_name = col_name

        plt.figure(figsize=(8,6))
        plt.boxplot(self.df[self.target_col],vert=True,patch_artist=True,boxprops=dict(facecolor='lightblue'))
        plt.title(self.col_name)
        plt.ylabel(self.target_col)
        plt.show()

    def view_stackedBar(self,x_col,y_cols,title,xlabel,ylabel):
        self.x_col = x_col
        self.y_cols = y_cols
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

        bottom_values = pd.Series([0]*len(self.df))
        plt.figure(figsize=(10,6))

        for col in self.y_cols:
            plt.bar(self.df[self.x_col],self.df[col],bottom=bottom_values,label=col)
            bottom_values += self.df[col]

        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def view_trendline(self,x_col,y_col,title,xlabel,ylabel):
        self.x_col = x_col
        self.y_col = y_col
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

        plt.figure(figsize=(10,6))
        plt.plot(self.df[self.x_col],self.df[self.y_col],marker='o',color='blue',label='Data Points')

        z = np.polyfit(self.df[self.x_col],self.df[self.y_col],1)
        p = np.poly1d(z)
        plt.plot(self.df[self.x_col],p(self.df[self.x_col]),"r--",label='Trend Line')

        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.show()


# Example usage:
obj_viz = CovidVisualization('country_wise_latest.csv')
#obj_viz.view_Barchart('Country/Region','Confirmed','Covid Confirmed Cases by Country','Country/Region','Confirmed Cases')
# obj_viz.view_Piechart('Deaths','Distribution of Deaths by Country')
# obj_viz.view_Linechart('ObservationDate','Confirmed','Trend of Confirmed Cases Over Time','Observation Date','Confirmed Cases')
# obj_viz.view_Histogram('Recovered',30,'Histogram of Recovered Cases')
# obj_viz.view_Scatterplot('Confirmed','Deaths','Confirmed vs Deaths Scatter Plot','Confirmed Cases','Deaths')
# obj_viz.view_Boxplot('Confirmed','Boxplot of Confirmed Cases')
# obj_viz.view_stackedBar('Country/Region',['Confirmed','Deaths','Recovered'],'Stacked Bar of Covid Cases by Country','Country/Region','Number of Cases')   
# obj_viz.view_trendline('ObservationDate','Confirmed','Trend Line of Confirmed Cases Over Time','Observation Date','Confirmed Cases')
 


# obj_viz = CovidVisualization('Sorted_Confrirmed.csv')
# obj_viz.view_Barchart('Country/Region','Confirmed','Covid Confirmed Cases by Country','Country/Region','Confirmed Cases')



        

