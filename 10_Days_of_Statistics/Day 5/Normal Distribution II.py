# Importing the library
import math


# Define function
def cdf(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))


# Getting input
initial_values = list(map(float, input().split()))
mean = initial_values[0]
std = initial_values[1]
val_1 = float(input())
val_2_3 = float(input())

# Calculating and printing result
print(round(100 - (cdf(mean, std, val_1) * 100), 2))
print(round(100 - (cdf(mean, std, val_2_3) * 100), 2))
print(round(cdf(mean, std, val_2_3) * 100, 2))
