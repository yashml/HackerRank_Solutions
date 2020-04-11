dice_1 = [1, 2, 3, 4, 5, 6]
dice_2 = [1, 2, 3, 4, 5, 6]
total_outcomes = len(dice_1) * len(dice_2)
event = 0

# Calculating number of occurrences of event
for i in range(len(dice_1)):
    for j in range(len(dice_2)):
        if (dice_1[i] != dice_2[j]) and ((dice_1[i] + dice_1[j]) == 6):
            event += 1

# Calculating probability
probability = event / total_outcomes
print(probability)
