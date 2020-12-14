import random

coulmn = int(input('к-сть стовбців : '))
row = int(input('к-сть рядків : '))
A = [[random.randint(-100, 100) for j in range(row)] for i in range(coulmn)]
print(A)
s = 0
for i in range(1, coulmn, 2):
    if A[i] < 0:
        s += A[i]
print(s)
