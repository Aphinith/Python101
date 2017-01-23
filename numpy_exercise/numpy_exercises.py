import numpy as np 

# create array of 10 zeros
arr_of_zeros = np.zeros(10)
# print(arr_of_zeros)

# create array of 10 ones
arr_of_ones = np.ones(10)
# print(arr_of_ones)

# create array of ten fives
arr_10_fives = np.repeat(5, 10)
# print(arr_10_fives)

# create array of numbers from 10 to 50
arr_10_to_50 = np.arange(10, 51)
# print(arr_10_to_50)

# create array of numbers from 10 to 50 even numbers only
arr_even_10_to_50 = list(filter(lambda num: (num%2 == 0), arr_10_to_50))
# print(arr_even_10_to_50)

# create a 3x3 array with 0-8 integers
arr_3X3_0_to_8 = np.array([[0,1,2], [3,4,5], [6,7,8]])
# print(arr_3X3_0_to_8)

# create a 3x3 identity matrix
arr_identity_3x3 = np.eye(3)
# print(arr_identity_3x3)

# use numpy to generate a number between 0 and 1
ran_num = np.random.rand(1)
# print(ran_num)

# use numpy to generate 25 random numbers sampled from a normal distribution
twentyfive_ran_num = np.random.randn(25)
# print(twentyfive_ran_num)

# create array from 0 to 1, incremented by .01, 2d array
arr_0_to_1_100steps = np.arange(0.01, 1.01, .01).reshape(10, 10)
# print(arr_0_to_1_100steps)

# Create an array of 20 linearly spaced points between 0 and 1:
second_linspace_arr = np.linspace(0, 1, 20)
# print(second_linspace_arr)





