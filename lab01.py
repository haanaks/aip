import math


# Блок ввода переменных
a = float(input('Enter a '))
x = float(input('Enter x '))

# Блок вычисления функции G
C = 9 * (7 * a * a - 19 * a * x + 10 * x * x)
B = (25 * a * a + 30 * a * x + 9 * x * x)

# Блок вычисления функции F
F = -(math.sin(9 * a * a + a * x - 10 * x * x))

# Блок вычисления функции Y
Y = -5 * a * a + 12 * a * x + 9 * x * x + 1

# Блок вывода результатов
print('G=', C / B)
print('Y=', math.log(Y / math.log(10)))
print('F=', F)
