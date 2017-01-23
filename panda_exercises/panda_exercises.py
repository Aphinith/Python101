import numpy as np 
import pandas as pd 

# print('np: ', np)
# print('pd: ', pd)

# create series

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

# print('labels: ', labels)
# print('my_data: ', my_data)
# print('arr: ', arr)
# print('d: ', d)

# print(pd.Series(data=my_data, index=labels))
# above is the same as below
# print(pd.Series(my_data, labels))

# can also pass in numpy arrays
# print(pd.Series(arr, labels))

#can also pass in dictionaries 
print(pd.Series(d))