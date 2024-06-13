# import necessary libraries

import seaborn as sns
import pandas as  pd
import matplotlib.pyplot as plt


# load the iris dataset using load_dataset()
iris = sns.load_dataset('iris')


# explore the loaded iris dataset(EXPLORATORY DATA ANALYSIS)
print("First five rows of the Iris dataset: ")
iris.head() # gives first 5 rows of iris dataset

print("Information about the columns in the Iris dataset: ")
iris.info() # gives info about dataset columns

print("A summary of basic analysis on Iris dataset: ")
iris.describe() # gives a consolidated analysis of the dataset


# DATA CLEANING

# check for missing values in the Iris dataset
print(iris.isnull().sum())

# check for duplicates in the dataset
print("Number of duplicates in Iris dataset: ")
print(iris.duplicated().sum())
if iris.duplicated().sum() > 0:
    # remove duplicates
    iris = iris.drop_duplicates()

    # verifying if duplicates have been removed
    print(iris.duplicated().sum())


# AGGREGATION
# perform aggregation to get a statistical summary of Iris dataset grouped by species
species_mean = iris.groupby('species').mean()
print(f"The mean of sepcies in Iris dataset is :\n\n {species_mean}")

species_summary = iris.groupby('species').describe()
print(f"The statistical summary of species in Iris dataset:\n\n {species_summary}")


# VISUALISATION
# generating a grid of scatterplots with pairwise relationships for each pair of features in Iris dataset
sns.pairplot(iris, hue = 'species') # color in scatter plots represent various Iris flower species
plt.show()


# box plot
plt.figure(figsize = (6,4))
plt.title('Box plot of Iris Dataset')
sns.boxplot(data=iris, orient='h')


# correlation  calculations & heatmaps

# correlation matrix
correlation_matrix = iris.drop(columns=['species']).corr()

# generate heatmap
plt.figure(figsize = (6,4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Iris Dataset')
plt.show()