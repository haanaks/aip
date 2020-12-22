xa =[]
yx = []
x = [int(i) for i in input('Введите координаты х: ').split()]
print('Координаты х: ', x)
y = [int(i) for i in input('Введите координаты y: ').split()]
print('Координаты y: ', y)
a = float(input('Введите скаляр а: '))
print('Скаляр: ', a)
for elem_x in x:
    xa.append(elem_x * a)
print('Вектор х, умноженные на скаляр: ', xa)
for elem in zip(y, xa):
    x_elem, y_elem = elem
    yx.append(x_elem + y_elem)
print('Вектор у: ', yx)