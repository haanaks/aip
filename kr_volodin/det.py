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

