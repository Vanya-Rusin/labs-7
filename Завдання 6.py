import random

r = int(input("Кількість стовбців  = "))
e = int(input("Кількість рядків  = "))

a = [[random.randint(-100, 100) for j in range(e)] for i in range(r)]
print(a)
b = []
for j in range(len(a)):
    d = 0
    minimal = min(a[j])
    i = a[j].index(minimal)
    for k in range(len(a)):
        if a[k][i] > minimal:
            d = 1
    if d == 0:
        b.append((j, i))
print(b)
