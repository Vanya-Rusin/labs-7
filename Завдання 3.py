m = int(input("Введіть вимір вектора (кількість елементів матриці): "))
n = int(input("кількість рядків матриці n="))

b = [float(input("Веідть {0}-у координату вектора: ".format(i+1))) for i in range(m)]
print("Вектор b={0}".format(b))
a = [[float(input("Введіть координати матриці а[{0}][{1}]=".format(i, j))) for j in range(m)] for i in range(n)]
print("Матриця А={0}".format(a))

с = [[a[i][j]-b[j] for j in range(m)] for i in range(n)]
print("Вектор с={0}".format(с))
