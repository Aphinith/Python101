import numpy as np 
import pandas as pd 
from numpy.random import randn

np.random.seed(101)

# DataFrame takes in three arguments, data, index, and columns
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print('\n')
# print(df['W'])
# print('this is type: ', type(df['W']))

# to get multiple columns, pass in list of columns
# print(df[['X', 'Y']])
# print('\n')

# to add new columns: 
df['new'] = df['W'] + df['Z']
# print(df)
# print('\n')

# to remove columns, use df.drop(<column name>, <axis = 0 or 1, 0 are rows, 1 are columns>, inplace=True)
df.drop('X', 1, inplace=True)
# print(df)
# print('\n')
df.drop('E', 0, inplace=True)
print(df)
print('\n')

# Selecting rows, can use two methods to use to get rows --> .loc or .iloc
# print(df.loc['A'])
# print('\n')
# print(df.iloc[2])
# print('\n')

# Selecting subsets of rows and columns
# One way is to select the row, then the column with .loc method:
print('This should just be one number: ', df.loc['A', 'W'])
print('\n')

# Another way is to use list within the list to get subsets of multiple rows and columns
print(df.loc[ ['A', 'B'], ['Z', 'new'] ])
print('\n')




