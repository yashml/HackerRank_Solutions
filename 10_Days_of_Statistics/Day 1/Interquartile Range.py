# Getting the input
no_of_elements = int(input())
elements = list(map(int, input().split()))
frequencies = list(map(int, input().split()))
total_frequency = sum(frequencies)

# Defining Median function
def median(my_list):
    length = len(my_list)

    if (length % 2 == 0):
        return ((my_list[length // 2 - 1] + my_list[length // 2]) / 2)

    else:
        return my_list[(length - 1) // 2]

# New data creation base don elements and frequencies
new_data = []
for i in range(len(elements)):
    for j in range(frequencies[i]):
        new_data.append(elements[i])
new_data.sort()

# Separating case for odd and even
if (total_frequency % 2 == 0):
    q1 = median(new_data[0:total_frequency // 2])
    q3 = median(new_data[total_frequency // 2:])
    print(q3 - q1)

else:
    q1 = median(new_data[0:(total_frequency - 1) // 2])
    q3 = median(new_data[(total_frequency + 1) // 2:])
    print(q3 - q1)