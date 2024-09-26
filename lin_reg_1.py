# https://www.kaggle.com/code/sudhirnl7/linear-regression-tutorial

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

# Configure plot
plt.rcParams['figure.figsize'] = [8, 5]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-v0_8-whitegrid')

# Import dataset
path = './datasets/'
df = pd.read_csv(path+'insurance.csv')
print('\nNumber of rows and columns in this dataset: ', df.shape)
print('')

# First 5 rows of insurance.csv
print(tabulate(df.head(), headers='keys', tablefmt='psql'))