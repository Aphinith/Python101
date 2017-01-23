import numpy as np 
import pandas as pd 
from numpy.random import randn

# Index levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
# print(hier_index)
# print('\n')
hier_index = pd.MultiIndex.from_tuples(hier_index)
# print(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(df)
print('\n')

# to grab higher level index, use .loc[<name of index>]
print(df.loc['G1'])
print('\n')
# can continue to grab the inner index by using .loc chained to above
print(df.loc['G1'].loc[1]) # --> returns the series at index 1
print('\n')

# Naming indexes, by default there are no names. You can get names by:
print(df.index.names) # --> [none, none]
print('\n')
# to add names: set below to list of names
df.index.names = ['Groups', 'Numbers']
print(df)
print('\n')

# Cross Sections (xs). Returns a cross section of rows or columns
# must indicate cross section and specific level
print(df.xs(1, level='Numbers')) # --> this will get all values in the index of 1 in the Numbers column