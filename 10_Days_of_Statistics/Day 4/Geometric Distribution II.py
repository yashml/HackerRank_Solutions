# Getting the input
values = list(map(float, input().split()))

p = values[0] / values[1]
q = 1 - p

n = int(input())

# Calculating and printing result
result = 0
for i in range(1, n + 1):
    result = result + (q ** (i - 1) * p)

print(round(result, 3))
