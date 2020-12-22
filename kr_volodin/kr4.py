import random
x = 0
y = 0
z = 0
t = []
s = 0
c = []
n = int(input('Число строк в матрице'))
m = int(input('Число столбцов в матрице'))
a = [[random.randint(1, 10) for j in range(m)] for i in range(n)]
b = [[random.randint(1, 10) for j in range(m)] for i in range(n)]
for i in range(n):
    print(a[i])
print()

for i in range(n):
    print(b[i])
print()

for j in range(0,m):
    for i in range(0,n):
        for z in range(0,n):
            s += a[j][z]*b[z][i]
        t.append(s)
        s = 0
    c.append(t)
    t = []

for i in range(n):
    print(c[i])