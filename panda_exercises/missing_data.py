import numpy as np 
import pandas as pd 

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df)
print('\n')

############################################################################
# DROP MISSING VALUES
# drop missing data values from data sets, use .dropna()
# if you use .dropna() without any arguments, it will drop any row with 
#   missing values (entire row gets removed)
# print(df.dropna()) # --> only row 0 remains

# if you want to drop columns, use df.dropna(axis=1), must pass in axis 
# print(df.dropna(axis=1)) # --> only column C remains

# can also set threshold to control limit of when to drop nan/null values
# print(df.dropna(thresh=2)) # --> rows 0 and 1 remain, this means row needs at least 2 values to remain

#############################################################################
# FILLING IN MISSING VALUES
# to fill in missing values, use .fillna(value='FILL VALUE') -- use .fillna with value to fill in as first arg
# print(df.fillna(value='FILL VALUE')) # --> all nan values are now 'FILL VALUE'

# fill in column A nan space with mean of column A
print(df['A'].fillna(value=df['A'].mean()))