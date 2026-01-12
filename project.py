import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
import numpy as np


data = pd.read_csv("Machine Learning/machine_learning.csv")

X = data[["Hours"]]
y = data[["Score"]]

model = LinearRegression()

model.fit(X,y)

predicted_score = model.predict(X)

mae = mean_absolute_error(y,predicted_score)
mse = mean_squared_error(y,predicted_score)
rmse = np.sqrt(mse)

print("MAE",mae)
print("MSE",mse)
print("RMSE",rmse)

new_hour = float(input("Enter hours of you studied :"))
new_pred = model.predict([[new_hour]])

print(f"Prediction for {new_hour} is {new_pred}")

