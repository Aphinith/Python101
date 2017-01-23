import numpy as np 
import pandas as pd 
from numpy.random import randn

np.random.seed(101)

# DataFrame takes in three arguments, data, index, and columns
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)