# Getting the input
values = list(map(float, input().split()))

p = values[0]/values[1]
q = 1-p

n = int(input())

# Calculating and printing result
result = q**(n-1) * p
print(round(result, 3))
