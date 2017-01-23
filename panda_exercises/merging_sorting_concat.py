import pandas as pd 

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

##########################################################
# concatenation: use pd.concat([<items to concat>]), default axis is 0
print(pd.concat([df1, df2, df3])) # --> will concatenate all data frames into one on axis=0 (rows)
print('\n')
print(pd.concat([df1, df2, df3], axis=1)) # --> will concatenate all data frames into one on axis=01(columns), will have nan where values do not exist
print('\n')

##########################################################
# MORE EXAMPLE DATA FRAMES

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})   

# USING MERGE
# pd.merge() --> arguments are (dataframes, how='inner', on='key' <key being the column that shares the same values in each dataframe>)
# how argument is default to inner, if you want to merge on multiple keys, pass it to on as a list --> on=['key1', 'key2']
# how argument also has inner nad outer 
print(pd.merge(left, right, how='inner', on='key'))
print('\n')

##########################################################
# JOINING
# Joining is a convenient method for combining the columns of 
# two potentially differently-indexed DataFrames into a single result DataFrame.
# using join() will join tables using index



left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])


print(left.join(right))
print('\n')
print(left.join(right, how='outer'))














