# Importing the library
import math


# Define function
def cdf(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))


# Getting the input
max_weight = float(input())
n = float(input())
mean = float(input())
std = float(input())

new_mean = mean * n
new_std = math.sqrt(n) * std

# Calculating and printing result
print(round(cdf(new_mean, new_std, max_weight),4))
