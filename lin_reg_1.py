# https://www.kaggle.com/code/sudhirnl7/linear-regression-tutorial

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
from sympy import symbols, Eq

# Configure plot
plt.rcParams['figure.figsize'] = [8, 5]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-v0_8-pastel')

# Import dataset
path = './datasets/'
df = pd.read_csv(path+'insurance.csv')

# Shape of dataset (1338, 7)
print('Number of rows and columns in this dataset: ', df.shape)

# First 5 rows of insurance.csv
print(tabulate(df.head(), headers='keys', tablefmt='psql'))

# Dependent (target) variable in this case is charges.
# Independent variables are: age, sex, bmi, children, smoker, and region.

## The linear regression equation ##

# Define the variables
theta_0, theta_1, theta_2, theta_3, theta_4, theta_5, theta_6 = symbols('θ_0 θ_1 θ_2 θ_3 θ_4 θ_5 θ_6')
age, sex, bmi, children, smoker, region = symbols('age sex bmi children smoker region')

# Define the linear regression equation
h_theta_xi = Eq(symbols('hθ(xᵢ)'), theta_0 + age*theta_1 + sex*theta_2 + bmi*theta_3 + children*theta_4 + smoker*theta_5 + region*theta_6)

# Print the equation
print('Linear regression equation: ', h_theta_xi)

# Charge vs. BMI
sns.lmplot(x='bmi', y='charges', data=df, aspect=2, height=6)
plt.xlabel('Body Mass Index$(kg/m^2)$: Independent variable')
plt.ylabel('Insurance Charges: Dependent variable')
plt.title('Charge vs. BMI')
# plt.show()

## Exploratory Data Analysis ##

# Summary of data
print(tabulate(df.describe(), headers='keys', tablefmt='psql'))

# Check for missing values (none)
plt.figure(figsize=(12,4))
sns.barplot(df.isnull())
plt.xlabel('Variables')
plt.ylabel('Total # of Missing Values')
plt.yticks(range(0, 6, 1))
# plt.show()

# Use one-hot encoding for correlation ()
# Correlation between variables
corr = df.corr()
sns.heatmap(corr, cmap='Wistia', annot=True)
plt.show()