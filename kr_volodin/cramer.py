import det
import copy

# Массив для коэффициентов при переменных
coeffs = []
# Массив для свободных коэффициентов
free_coeffs = []
number = int(input('Сколько уравнений? '))

for i in range(number):
    # Пустой массив, где будут коэффициенты
    coeffs.append([])
    for j in range(number):
        # Собираем коэффициенты
        coeffs[i].append(int(input(f'Введите {j+1}-й коэффициент {i+1}-го уравнения: ')))
    # Собираем свободные коэффициенты
    free_coeffs.append(int(input(f'Введите свободный коэффициент {i+1}-го уравнения: ')))

# Определитель матрицы
d = det.determinant(coeffs, number)

if d == 0:
    print("Определитель равен нулю")
else:
    # Для матрицы с ненулевым определителем
    for i in range(number):
        # Для каждой переменной
        line = copy.deepcopy(coeffs)
        for j in range(number):
            # Заменяем столбец с коэффициентами
            # при переменной на свободные
            line[j][i] = free_coeffs[j]
        # Находим определитель матрицы с заменёнными
        # коэффициентами
        line_det = det.determinant(line, number)
        # Выводим результаты переменных
        print(f'Переменная {i+1}: {line_det/d}')