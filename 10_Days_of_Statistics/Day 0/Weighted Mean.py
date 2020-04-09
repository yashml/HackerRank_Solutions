# Getting the input
no_of_elements = int(input())
elements = list(map(int, input().split()))
element_weights = list(map(int, input().split()))

sum_elements = 0

for i in range(no_of_elements):
    sum_elements += elements[i]*element_weights[i]

# Printing the output
print(round(sum_elements/sum(element_weights), 1))