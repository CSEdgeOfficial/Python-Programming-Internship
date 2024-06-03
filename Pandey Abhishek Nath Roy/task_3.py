import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Feature names (replace with actual descriptions from the dataset)
feature_names = ["CRIM", "ZN", "INDUS", ...]

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

# Combine features and target
data = np.c_[raw_df.values[:, :], raw_df.values[1::2, 2]]  # Select all features and target values

# Assign feature names to the DataFrame columns
df = pd.DataFrame(data, columns=feature_names)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df.iloc[:, -1], test_size=0.2, random_state=42)

# Initialize the linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Predict on the training and testing data
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Calculate the scores
train_score = r2_score(y_train, y_train_pred)
test_score = r2_score(y_test, y_test_pred)

# Print additional evaluation metrics
mse_train = mean_squared_error(y_train, y_train_pred)
mse_test = mean_squared_error(y_test, y_test_pred)

print("Training R-squared:", train_score)
print("Testing R-squared:", test_score)
print("Training MSE:", mse_train)
print("Testing MSE:", mse_test)
