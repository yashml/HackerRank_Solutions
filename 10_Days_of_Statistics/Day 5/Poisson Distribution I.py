# Importing the library
import math

# Getting the input
mean = float(input())
k = float(input())
e = 2.71828

# Calculating and printing the result
result = ((mean ** k) * (e ** -mean)) / math.factorial(k)
print(round(result, 3))
