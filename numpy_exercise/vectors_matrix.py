import numpy as np

# print(np)

my_list = [1, 2, 3, 4]

# np.array() -- takes in one argument, an array, turns it into a vector or
# a matrix depending on if the array is a 1D or 2D array

# print('this is before using np: ', my_list)
# print(np.array(my_list))

my_2D_list = [[1,2,3], [4,5,6], [7,8,9]]

# print(np.array(my_2D_list))


# np.arange() -- takes in a start, stop, and step parameters

arange_arr = np.arange(0, 10) # --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(arange_arr)