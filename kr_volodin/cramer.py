import for5 as f
import time
from sys import getsizeof
import random

coeffs = []
free_coeffs = []
number = int(input('Сколько уравнений? '))

for i in range(number):
    coeffs.append([])
    for j in range(number):
        # Собираем коэффициенты
        coeffs[i].append(random.randint(-10, 10))
    # Собираем свободные коэффициенты
    free_coeffs.append(random.randint(-10, 10))

# Определитель матрицы
d = f.determinant(coeffs, number)

if d == 0:
    print("Определитель равен нулю")
else:
    start_time = time.time()
    result = f.cramer(coeffs, free_coeffs, number, d)
    print(f'Ответ:{result}')
    with open('time.txt', 'a') as file:
        file.write(str(time.time() - start_time) + '\n')
    with open('memory.txt', 'a') as file:
        file.write(str(getsizeof(result)) + '\n')
