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

# Selecting with conditionals
# print(df > 0) --> table of boolean values

booldf = df > 0
# print(df[booldf]) # --> table of values, true shows values, false shows NaN

# Selecting rows or columns with conditionals
print(df['Y'] > 0) # --> series of boolean values
print('\n')
# Passing in series will not give you null values in result, below also prints out whole dataframe
print(df[df['Y'] > 0])
print('\n')
# Can stack calls onto data frames as well, for example, if just want new column:
print(df[df['Y'] > 0]['new'])
print('\n')

# More examples using variables to store results
boolser = df['W'] > 0
result = df[boolser]
print('result:')
print(result)
print('\n')
# pulling multiple columns from result
mycols = ['Y', 'Z']
print(result[mycols]) # --> will get columns Y and Z
print('\n')


# Using tow or more conditions, use & for the 'and' operator. Do not use 'and', 
# will not work on series comparisons. To use 'or', use the pipe operator '|'
print(df[(df['Y'] > 0) & (df['new'] > 1)])
print('\n')

# resetting index, will need to pass in 'inplace=True' to keep change
print(df.reset_index())
print('\n');

# exercise to set new index
newind = 'CA NY WA FL'.split()
# print(newind)
# set new columns into df 
df['States'] = newind
print(df)
print('\n')

# using one of the columns to set index
print(df.set_index('States'))









