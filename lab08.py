import random
import time
import math

count = 0
r = float(input('Enter rad'))
x0, y0 = float(input('Enter сenter of circle(x,y)')), float(input())
mas_x, mas_y = [], []
start_time = time.time()
for i in range(100000):
    mas_x.append(random.randint(-100, 100))
    mas_y.append(random.randint(-100, 100))
    if math.pow(r, 2) >= math.pow(mas_x[i] - x0, 2) + math.pow(mas_y[i] - y0, 2):
        count += 1
if count == 0:
    print('В данной области нет точек')
else:
    print(f'Радиус:{r}  Центр:{x0};{y0}  Кол-во точек:{count}')
with open('time.txt', 'a') as f:
    f.write(str(time.time() - start_time) + '\n')
