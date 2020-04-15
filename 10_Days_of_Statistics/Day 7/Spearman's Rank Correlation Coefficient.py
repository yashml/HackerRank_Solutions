# Getting the input
n = int(float(input()))
data_x = list(map(float, input().split()))
data_y = list(map(float, input().split()))



# Defining the function
def rank(det):
    ranks = {}
    sorted_val = sorted(det)
    for i in range(len(det)):
        for j in range(len(sorted_val)):
            if det[i] == sorted_val[j]:
                ranks[det[i]] = j + 1
    return ranks


def spearman_coefficient(x, y, rx, ry, n):
    diff_rank = 0
    for i in range(n):
            diff_rank += ((rx[x[i]] - ry[y[i]]) ** 2)
    return 1 - (6 * diff_rank) / (n ** 3 - n)


# Get rank
rank_x = rank(data_x)
rank_y = rank(data_y)

# Gets the result and show on the screen
s = spearman_coefficient(data_x, data_y, rank_x, rank_y, n)
print(round(s, 3))
