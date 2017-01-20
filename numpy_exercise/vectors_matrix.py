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


# np.linspace() -- takes in start, stop, and third argument is a 
# number for evenly spaced points

evenly_spaced_num = np.linspace(0, 10, 20) # --> (see below)
   # [  0.           0.52631579   1.05263158   1.57894737   2.10526316
   # 2.63157895   3.15789474   3.68421053   4.21052632   4.73684211
   # 5.26315789   5.78947368   6.31578947   6.84210526   7.36842105
   # 7.89473684   8.42105263   8.94736842   9.47368421  10.        ]

# print(evenly_spaced_num)


# identity matrix, use np.eye() -- takes in one number

first_identity_matrix = np.eye(4) # --> (see below)
  # [[ 1.  0.  0.  0.]
  #  [ 0.  1.  0.  0.]
  #  [ 0.  0.  1.  0.]
  #  [ 0.  0.  0.  1.]]

# print(first_identity_matrix)


# creating random matrixes
# np.random.rand() -- will give you random numbers from 0 to 1
# np.random.randn() -- will givey ou random numbers for 0 distribution
# np.random.randint() -- takes in a low, high, and size of array --> will give you 
#   a random array of integers with the specificed arguments passed in

# reshaping arrays
# use arr.reshape() -- arguments will be the size of the array (arr refers to array object)















