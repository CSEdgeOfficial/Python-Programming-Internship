#1. Load the Dataset:

from sklearn.datasets import load_boston
boston = load_boston()

#2. Prepare the Data:

import pandas as pd

boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df['PRICE'] = boston.target

X = boston_df.drop('PRICE', axis=1)
y = boston_df['PRICE']

#3. Split the Data:

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#4. Train the Model:

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

#5. Evaluate the Model:

train_score = model.score(X_train, y_train)
print(f'Training Score: {train_score}')

test_score = model.score(X_test, y_test)
print(f'Testing Score: {test_score}')

#6. Plot Residuals:

import matplotlib.pyplot as plt

train_residuals = y_train - model.predict(X_train)
test_residuals = y_test - model.predict(X_test)

plt.figure(figsize=(10, 5))
plt.scatter(model.predict(X_train), train_residuals, label='Train Residuals', alpha=0.5)
plt.scatter(model.predict(X_test), test_residuals, label='Test Residuals', alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.legend()
plt.show()
