# Importing the library
from sklearn import linear_model

# Getting the input
m, n = map(int, input().split())
X, Y = [], []

# Getting the parameters X and Y
for i in range(n):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < m:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)

# Setting the model
model = linear_model.LinearRegression()
model.fit(X, Y)
a = model.intercept_
b = model.coef_

# Getting the parameters X for discovery the Y
q = int(input())
new_X = []
for i in range(q):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    new_X.append(x)

# Calculating and printing result
result = model.predict(new_X)
for i in range(len(result)):
    print(round(result[i],2))
