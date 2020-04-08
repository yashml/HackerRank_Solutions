import numpy as np
from scipy import stats

no_of_elements = int(input())
elements = list(map(int, input().split()))

print(np.mean(elements))
print(np.median(elements))
print(int(stats.mode(elements)[0]))