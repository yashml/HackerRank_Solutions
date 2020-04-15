# Importing the library
import math

# Set data
n = float(input())
mean = float(input())
std = float(input())
percent_confidence_interval = float(input())
z_score = float(input())

# Calculate Confidence Interval
confidence_interval = z_score * (std / math.sqrt(n))

# Calculating and printing result
print(round(mean - confidence_interval, 2))
print(round(mean + confidence_interval, 2))
