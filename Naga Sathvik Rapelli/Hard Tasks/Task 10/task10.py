#1. Load the DataSet:
import seaborn as sns
iris_df = sns.load_dataset('iris')

#2. Exploratory Data Analysis (EDA):

print(iris_df.info())
print(iris_df.describe())
print(iris_df.head())

#3. Data Cleaning:

print(iris_df.isnull().sum())
print(iris_df.duplicated().sum())

#4. Aggregation:

species_mean = iris_df.groupby('species').mean()

#5. Visualizations:

import matplotlib.pyplot as plt
import seaborn as sns

sns.pairplot(iris_df, hue='species')
plt.show()

sns.heatmap(iris_df.corr(), annot=True, cmap='coolwarm')
plt.show()

#6. Correlation Calculations:

correlation_matrix = iris_df.corr()
