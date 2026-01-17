import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
df = pd.read_csv('sales_data.csv')  # Assuming a CSV file with 'Experience' and 'Salary' columns
x = pd.to_numeric(df['Advertising_Spend'], errors='coerce').values.reshape(-1, 1)
y = pd.to_numeric(df['Total Amount'], errors='coerce').values


xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=42)
# Transforming the data to include polynomial features
poly = PolynomialFeatures(degree=2)
xtrainpoly = poly.fit_transform(xtrain)
xtestpoly = poly.transform(xtest)

Model = LinearRegression()
Model.fit(xtrainpoly,ytrain)

ypred = Model.predict(xtestpoly)
#Evaluating the model
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(ytest, ypred)
r2 = r2_score(ytest, ypred)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Plotting the results
plt.scatter(x, y, color='blue', label='Data Points')
# Sort x for a better line plot
sorted_indices = x.flatten().argsort()
x_sorted = x[sorted_indices]
x_sorted_poly = poly.transform(x_sorted)
y_sorted_pred = Model.predict(x_sorted_poly)
plt.plot(x_sorted, y_sorted_pred, color='red', label='Polynomial Fit')
plt.xlabel('Advertising Expense')
plt.ylabel('Total Amount')
plt.title('Polynomial Regression Fit')
plt.legend()
plt.show()

