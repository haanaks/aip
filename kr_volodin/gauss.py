import random
from sys import getsizeof
import time
import for5 as f

number = int(input('Сколько уравнений?'))
matrix = [[random.randint(0, 9) for i in range(number+1)] for j in range(number)]
start_time = time.time()
result = f.gauss(matrix, number)
with open('time.txt', 'a') as file:
    file.write(str(time.time() - start_time) + '\n')
with open('memory.txt','a') as file:
    file.write(str(getsizeof(result)) + '\n')
print(f'Ответ:{result}')