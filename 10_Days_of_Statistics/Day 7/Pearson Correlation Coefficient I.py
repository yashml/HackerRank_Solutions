# Importing the library
import statistics as st

# Getting the input
n = int(float(input()))
data_x = list(map(float, input().split()))
data_y = list(map(float, input().split()))


# Defining the function
def pearson_coefficient(n, x, y):
    mean_x = st.mean(x)
    mean_y = st.mean(y)
    std_x = st.pstdev(x)
    std_y = st.pstdev(y)
    c = 0
    for i in range(n):
        c = c + (x[i] - mean_x) * (y[i] - mean_y)
    return c / (n * std_x * std_y)


# Calculating and printing result
print(round(pearson_coefficient(n, data_x, data_y), 3))
