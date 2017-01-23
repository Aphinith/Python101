import numpy as np 
import pandas as pd 

df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})

# print(df)
# print('\n')
print(df.head())
print('\n')

##########################################################
# FINDING UNIQUE VALUES
# using the .unique() method
print(df['col2'].unique()) # --> will return a list of the unique values
print('\n')
print(len(df['col2'].unique())) # --> will return length of unique values
print('\n')
print(df['col2'].nunique()) # --> pandas has its own unique methoed, nunique(), will return number of unique values
print('\n')

# FINDING VALUE COUNTS
# use .value_counts() --> will return the number of times a value is present in the table
print(df['col2'].value_counts())
print('\n')


###########################################################
# APPLY METHOD

# example:
def times2(x):
  return x*2

# chain the .apply() method to dataframe to apply the functions onto it
print(df['col1'].apply(times2))
print('\n')

# can also use lambda expressions 
print(df['col2'].apply(lambda x: x/2))
print('\n')


###########################################################
# DROPPING COLUMNS
# use .drop(<column name>, axis=1)
print(df.drop('col1', 1))
print('\n')


############################################################
# getting column names
# use .columns method
print(df.columns) # --> return column names
print('\n')

# getting row names (index)
# use .index
print(df.index) # --> return range of index
print('\n')


############################################################
# SORTING AND ORDERING DATAFRAMES
# example: sort by column 2
# use .sort_values(<column name>)
print(df.sort_values('col2'))
print('\n')


###########################################################
# FINDING NULL VALUES IN DATAFRAME
# use .isnull()
print(df.isnull()) # --> return a dataframe of boolean values
print('\n')


###########################################################
# PIVOT TABLES
# example:

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df)
print('\n')

# use pivot tables to create a multi index from above data frame
# use .pivot_table() -- takes three arguments, values, index, and columns
print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']))










