# Getting the input
no_of_elements = int(input())
elements = list(map(int, input().split()))

elements.sort()

# Defining Median
def median(my_list):
    length = len(my_list)

    if (length % 2 == 0):
        return ((my_list[length // 2 - 1] + my_list[length // 2] / 2))

    else:
        return int(my_list[length // 2])

# Separating case for odd and even
if (no_of_elements % 2 == 0):
    print(median(elements[0:no_of_elements // 2]))
    print(median(elements))
    print(median(elements[no_of_elements // 2:]))

else:
    print(median(elements[0:(no_of_elements - 1) // 2]))
    print(median(elements))
    print(median(elements[(no_of_elements + 1) // 2:]))