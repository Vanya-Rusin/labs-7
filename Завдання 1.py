import random

r = int(input("Кількість стовбців  = "))
e = int(input("Кількість рядків  = "))

a = [[random.randint(-100, 100) for j in range(e)] for i in range(r)]

b = []

for row in a:
    row_str = ['{0:5d}'.format(el) for el in row]
    b.append(row_str)

b = [''.join(['{0:5d}'.format(el) for el in row]) for row in a]
print(*b, sep='\n')
s = 0
for i in range(1, r, 2):
    for j in range(1, r, 2):
        if a[i][j] > 0:
            s += a[i][j]
print(s)
