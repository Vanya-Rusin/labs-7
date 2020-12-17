import random

coulmn = int(input('к-сть стовбців : '))
row = int(input('к-сть рядків : '))
A = [[random.randint(-5, 10) for j in range(row)] for i in range(coulmn)]
print(A)
s = 0
r = 0
for j in range(coulmn):
    for i in range(row):
        if A[i][j] < 0:
            r = 1
    if r == 1:
        for i in range(row):
            s += A[i][j]
print(s)
