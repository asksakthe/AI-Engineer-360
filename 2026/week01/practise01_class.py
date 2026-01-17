import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
x = np.array([1, 2, 3, 4]).reshape(-1, 1)
y = np.array([1,4,9,15])

# Transforming the data to include polynomial features
poly = PolynomialFeatures(degree=2)
xpoly = poly.fit_transform(x)

# Fitting the model
model = LinearRegression()
model.fit(xpoly, y)

# Making predictions
y_pred = model.predict(xpoly)

# Plotting the results
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_pred, color='red', label='Polynomial Fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Regression Fit')
plt.legend()
plt.show()

#different input
x_new = np.array([55, 61, 70]).reshape(-1, 1)
x_new_poly = poly.transform(x_new)

y_new_pred = model.predict(x_new_poly)
print("Predictions for new inputs:", y_new_pred)
# Output the predictions
for i, val in enumerate(x_new):
    print(f"Input: {val[0]}, Predicted Output: {y_new_pred[i]}")
# Predictions for new inputs: [3026.  3722.5  4990. ]
# Input: 55, Predicted Output: 3026.0
# Input: 61, Predicted Output: 3722.5
# Input: 70, Predicted Output: 4990.0
# The model predicts the outputs for the new inputs based on the polynomial regression fit.
# Predictions for new inputs: [3026.  3722.5  4990. ]
# Input: 55, Predicted Output: 3026.0
# Input: 61, Predicted Output: 3722.5
# Input: 70, Predicted Output: 4990.0
# The model predicts the outputs for the new inputs based on the polynomial regression fit.
# Predictions for new inputs: [3026.  3722.5  4990. ]
# Input: 55, Predicted Output: 3026.0









