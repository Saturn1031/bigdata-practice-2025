# -*- coding: utf-8 -*-
"""
Created on Sat May 17 15:24:52 2025

@author: narae
"""

from sklearn import linear_model
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

diabetes_data = datasets.load_diabetes()
X = pd.DataFrame(diabetes_data.data)
y = diabetes_data.target

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=156)

linear_regression = linear_model.LinearRegression()
linear_regression.fit(X = pd.DataFrame(X_train), y = Y_train)
prediction = linear_regression.predict(X = pd.DataFrame(X_test))

print('a value = ', linear_regression.intercept_)
print('b value =', linear_regression.coef_)

residuals = Y_test-prediction
SSE = (residuals**2).sum(); SST = ((Y_test-Y_test.mean())**2).sum()
R_squared = 1 - (SSE/SST)

print('R_squared = ', R_squared)
print('score = ', linear_regression.score(X = pd.DataFrame(X_test), y = Y_test))
print('Mean_Squared_Error = ', mean_squared_error(Y_test, prediction))
print('RMSE = ', mean_squared_error(Y_test, prediction)**0.5)
