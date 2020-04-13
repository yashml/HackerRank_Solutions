# Importing the library
import math

# Getting the input
values = list(map(float, input().split()))

p = (values[0] / 100)
q = 1 - p
n = int(values[1])


# Defining function binomial
def binomial(x, n, p):
    f = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    return f * (p ** x) * (q ** (n - x))


# Case 1: No more than 2 rejects
p_case_1 = 0
for i in range(n):
    if i < 3:
        p_case_1 += binomial(i, n, p)
print(round(p_case_1, 3))

# Case 2: At least 2 rejects
print(round(1 - p_case_1 + binomial(2, n, p), 3))
