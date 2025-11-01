import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,root_mean_squared_error


#dataframe creation
df01 = pd.read_csv("house_price_regression_dataset.csv")
df02 = df01[['Square_Footage','House_Price']]

# Exploratory Data Analysis (EDA)
# o Display the first few rows of the dataset.
print(df02.head(4))
# o Check for missing or null values and handle them appropriately.
print(df02.isnull().sum())
# o Visualize the relationship between Square Footage and Price using a scatter
print(df01.plot.scatter(x='Square_Footage',y='House_Price'))


# Feature and Target Selection
# o Assign Square Footage as the independent variable (X).
x = df01['Square_Footage']
# o Assign Price as the dependent variable (Y).
y = df01['House_Price']

# Train-Test Split
# o Split the dataset into training and testing sets using an 80-20 ratio.
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=43)

# Model Building
# o Create a Linear Regression model using LinearRegression from
# sklearn.linear_model.
model = LinearRegression()
# o Fit the model on the training data.
model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
# o Display the intercept (b₀) and coefficient (b₁) of the regression line.
print(f"Co-Efficient (slope): {model.coef_}")
print(f"Model Intercept is :{model.intercept_}")

# Prediction and Evaluation
# o Predict the house prices for the test set.
# o Calculate and print the following evaluation metrics:
#  Mean Squared Error (MSE)
mse = mean_squared_error(y_test,y_pred)
print(f"Mean Sq error is : {mse:.2f}")
#  Root Mean Squared Error (RMSE)
RMSE = np.sqrt(mse)
print(f"Root mean SQ is: {RMSE:.2f}")


# Visualization
# o Plot the regression line along with the actual data points.
# o Visualize actual vs predicted prices to assess model performance.
plt.Figure(figsize=(8,6))
plt.scatter(x_test,y_test,color='blue', label='Actual Data')
plt.plot(y_test,y_pred, color='red', label = 'Predicted One')
plt.title("House Prediction Model")
plt.xlabel("SQ Feet")
plt.ylabel("Price in Rupees")
plt.grid(True)
plt.legend()
plt.show()