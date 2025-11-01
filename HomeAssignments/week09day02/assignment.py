from pathlib import Path
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures

class StudentPerformancePredictor:
    def __init__(self):
           pass
    def preprocess_data(self, df):
          df['Extracurricular Activities'] = (df['Extracurricular Activities']=='Yes').astype(int)
          return df
    def select_features_target(self, df):
          x = df[['Hours Studied', 'Previous Scores', 'Extracurricular Activities', 'Sleep Hours', 'Sample Question Papers Practiced']]
          y = df['Performance Index']
          return x, y
    def train_model(self, xtrain, ytrain):
          model = LinearRegression()
          model.fit(xtrain, ytrain)
          return model
    def evaluate_model(self, model, xtest, ytest):
          ypred = model.predict(xtest)
          mse = mean_squared_error(ytest, ypred)
          rmse = np.sqrt(mse)
          r2score = r2_score(ytest, ypred)
          return mse, rmse, r2score
    


if __name__ =="__main__":
        #try:
        # Get the directory where the script is located
        script_dir = Path.cwd()
        csv_path = script_dir / "Student_Performance.csv"
        print(csv_path)        
        # Read the CSV file using the absolute path
        df = pd.read_csv(csv_path)
        #df = pd.read_csv("Student_Performance.csv")
        predictor = StudentPerformancePredictor()
        df = predictor.preprocess_data(df)
        x, y = predictor.select_features_target(df)
        xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
        model = predictor.train_model(xtrain, ytrain)
        mse, rmse, r2score = predictor.evaluate_model(model, xtest, ytest)
        print("Hello Student, Let me help you predict your performance index!")
        hours_studied = int(input("Enter Hours Studied: "))
        previous_scores = float(input("Enter Previous Scores: "))
        extracurricular_activities = int(input("Participated in Extracurricular Activities (press 1 for yes / 0 for no):"))
        sleeep_hours = float(input("Enter Sleep Hours: "))
        sample_question_papers_practiced = int(input("Enter Sample Question Papers Practiced: "))
        input_data = {'Hours Studied':hours_studied, 'Previous Scores':previous_scores, 'Extracurricular Activities':extracurricular_activities, 'Sleep Hours':sleeep_hours, 'Sample Question Papers Practiced':sample_question_papers_practiced}
        input_df = pd.DataFrame([input_data])
        predicted_performance_index = model.predict(input_df)
        print(f"Your Final Predicted Performance Index: {predicted_performance_index[0]:.2f}")
                                                   
            