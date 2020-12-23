import random
import time
import def_lab08 as count

mas_x, mas_y = [], []
r = float(input('Введите радиус окружности'))
n = 100000
while n <= 1000000:
    start_time = time.time()
    for i in range(n):
        mas_x.append(random.uniform(-100, 100))
        mas_y.append(random.uniform(-100, 100))
    x0, y0 = random.uniform(-100, 100), random.uniform(-100, 100)
    print(f'Центр:{x0};{y0}  Радиус:{r}  Кол-во точек:{count.counter(mas_x, mas_y, x0, y0, r)}')
    with open('time.txt', 'a') as f:
        f.write(str(time.time() - start_time) + '\n')
    n += 100000
