import random

coulmn = int(input('к-сть стовбців : '))
row = int(input('к-сть рядків : '))


A = [[random.randint(0, 100) for j in range(row)] for i in range(coulmn)]

print(A)

for i in range(coulmn):
   for j in range(row):
        if j % 2 == 1:
            A[j].sort(reverse=True)

print('\n')
print(A)
