import numpy as np 
import pandas as pd 

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]
       }

df = pd.DataFrame(data)
print(df)
print('\n')

###################################################################################
# Grouping by different methods --> use .groupby()
# group by company name
byComp = df.groupby('Company') # --> will return object with referene to location in memory space
# print(byComp)
# can perform other aggregrate functions now on byComp, and it will return the data frame
print(byComp.mean()) # --> will print out the mean of the columns with numeric values
print(byComp.sum()) # --> will print out the sum of the columns with numeric values
print('\n')
# from there you can also pull specific rows using .loc
print(byComp.sum().loc['FB'])
print('\n')


####################################################################################
# USING THE DESCRIBE METHOD
# chain .describe() method to get more information
print(df.groupby('Company').describe())
print('\n')

# chain .transpose() to change view to columns instead of rows
print(df.groupby('Company').describe().transpose())
