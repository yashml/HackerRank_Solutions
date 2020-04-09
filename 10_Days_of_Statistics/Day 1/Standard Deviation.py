# Importing the library
import math

# Getting the input
no_of_elements = int(input())
elements = list(map(int, input().split()))

mean =  sum(elements)/no_of_elements

# Defining the Standard Deviation function
def stddev(my_list, size):
    sum = 0
    for i in range(size):
        sum += (my_list[i]-mean)**2
    return math.sqrt(sum/size)

print(round(stddev(elements, no_of_elements), 1))