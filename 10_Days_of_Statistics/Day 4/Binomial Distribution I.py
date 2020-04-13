# Importing the library
import math

# Getting the input
ratio = list(map(float, input().split()))

p = ratio[0] / (ratio[0] + ratio[1])
q = 1 - p
n = 6


# Defining function binomial
def binomial(x, n, p):
    f = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    return f * (p ** x) * (q ** (n - x))


result = binomial(3, n, p) + binomial(4, n, p) + binomial(5, n, p) + binomial(6, n, p)

print(round(result, 3))
