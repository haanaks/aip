import copy

def determinant(matrix, n):
    # Определитель единичной матрицы —
    # её единственный элемент
    if n == 1:
        return(matrix[0][0])
    # Если размерность матрицы равна двум,
    # то считаем определитель по специальной формуле
    elif n == 2:
        return(matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1])
    # Если размерность матрицы больше двух,
    # то рекурсивно считаем определитель
    # более маленьких матриц, размерность
    # которых постепенно доводим до двух
    else:
        c = 0
        for i in range(n):
            new_matrix = copy.deepcopy(matrix)
            new_matrix.pop(0)
            for j in range(n-1):
                new_matrix[j].pop(i)
            c += (-1)**i * matrix[0][i] * determinant(new_matrix, n - 1)
        return(c)

def cramer(coeffs,free_coeffs,n,d):
    result = []
    for i in range(n):
        # Для каждой переменной
        line = copy.deepcopy(coeffs)
        for j in range(n):
            # Заменяем столбец с коэффициентами
            # при переменной на свободные
            line[j][i] = free_coeffs[j]
        # Находим определитель матрицы с заменёнными
        # коэффициентами
        line_det = determinant(line, n)
        result.append(line_det/d)
    return result

def gauss(matrix,n):
    for i in range(0, n):
        maximum_el = abs(matrix[i][i])
        maximum_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > maximum_el:
                maximum_el = abs(matrix[j][i])
                maximum_row = j

        for j in range(i, n + 1):
            matrix[maximum_row][j], matrix[i][j] = matrix[i][j], matrix[maximum_row][j]

        for j in range(i + 1, n):
            res = -matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                if i == k:
                    matrix[j][k] = 0
                else:
                    matrix[j][k] += res * matrix[i][k]

    solve = [0 for el in range(n)]
    for i in range(n - 1, -1, -1):
        solve[i] = matrix[i][n] / matrix[i][i]
        for j in range(i - 1, -1, -1):
            matrix[j][n] -= matrix[j][i] * solve[i]
    return solve

