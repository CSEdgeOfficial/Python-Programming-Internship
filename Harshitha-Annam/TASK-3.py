# import necessary libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.datasets import load_boston

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]


# load the dataset
X = data
y = target


# split the data into training data and testing data
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size = 0.2, random_state = 42)

# initialize the linear regression model 
model = LinearRegression()
# fit the model to the training dataset
model.fit(Xtrain, ytrain)

# perform predicitons
ytrain_pred = model.predict(Xtrain)
ytest_pred = model.predict(Xtest)

# compute the training and testing scores
train_score = model.score(Xtrain, ytrain)
test_score = model.score(Xtest, ytest)
# train_mse = mean_squared_error(ytrain, ytrain_pred)
# test_mse = mean_squared_error(ytest, ytest_pred)

# print the corresponding scores
print("The training score: ", train_score)
print("The testing score: ", test_score)
# print("Training MSE: ", train_mse)
# print("Testing MSE: ", test_mse)


# visualize the residuals
train_residuals = ytrain_pred - ytrain
test_residuals = ytest_pred - ytest
# plt.subplot(1, 2, 1)
plt.scatter(ytrain_pred, train_residuals, alpha=0.5)
plt.hlines(y=0, xmin=min(ytrain_pred), xmax=max(ytrain_pred), colors='r', linestyles='dashed')
plt.xlabel('Predicted Prices')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted Prices (Train)')
plt.show()
# plt.subplot(1, 2, 2)
plt.scatter(ytest_pred, test_residuals, alpha=0.5)
plt.hlines(y=0, xmin=min(ytest_pred), xmax=max(ytest_pred), colors='r', linestyles='dashed')
plt.xlabel('Predicted Prices')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted Prices (Test)')
plt.show()