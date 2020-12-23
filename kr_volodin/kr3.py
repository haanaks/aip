import time
import random

xa =[]
yx = []
x, y = [], []
for i in range(2):
    x.append(random.uniform(-10,10))
    y.append(random.uniform(-10,10))
a = random.uniform(-10,10)
print('Координаты х: ', x)
print('Координаты y: ', y)
print('Скаляр: ', a)
start_time = time.time()
for elem_x in x:
    xa.append(elem_x * a)
print('Вектор х, умноженные на скаляр: ', xa)
for elem in zip(y, xa):
    x_elem, y_elem = elem
    yx.append(x_elem + y_elem)
print('Вектор у: ', yx)
with open('time.txt', 'a') as f:
    f.write(str(time.time() - start_time) + '\n')