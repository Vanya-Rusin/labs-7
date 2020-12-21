import math

x = int(input('ведіть число x:'))
N = int(input('ведіть число n:'))
M = int(input('ведіть число m:'))
a = []
i = 1
while i < N + 1:
    b = []
    j = 1
    while j < M + 1:
        el = i * (math.sin(i * x) + math.cos(j * x))
        b.append(el)
        j += 1
    i += 1
    a.append(b)
for i in range(len(a)):
    print(a[i])
d = 1
for i in range(N):
    for j in range(M):
        if i * j < x:
            d *= a[i][j]
print(d)
