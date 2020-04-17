# Importing the library
import statistics as st

# Getting the input
n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
mean_x = st.mean(x)
mean_y = st.mean(y)
std_x = st.pstdev(x)
std_y = st.pstdev(y)

# Defining the function
def pearson_coefficient(number_of_elements, data_x, data_y):
    mean_x = st.mean(data_x)
    mean_y = st.mean(data_y)
    std_x = st.pstdev(data_x)
    std_y = st.pstdev(data_y)
    c = 0
    for i in range(n):
        c = c + (x[i] - mean_x) * (y[i] - mean_y)
    return c / (n * std_x * std_y)


x_squared = sum([x[i] ** 2 for i in range(5)])
xy = sum([x[i]*y[i] for i in range(5)])

# Set the b and a
b = pearson_coefficient(n, x, y) * std_y/std_x
a = mean_y - b * mean_x

# Calculating and printing result
print(round(a + 80 * b, 3))
