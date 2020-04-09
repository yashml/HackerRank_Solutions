# Importing the libraries
import numpy as np
from scipy import stats

# Getting the input
no_of_elements = int(input())
elements = list(map(int, input().split()))

# Printing the output
print(np.mean(elements))
print(np.median(elements))
print(int(stats.mode(elements)[0]))