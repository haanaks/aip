import my_functions as func
import matplotlib.pyplot as plt

while True:
    try:
        x = float(input('Enter lowest x'))
        x2 = float(input('Enter highest x'))
        h = float(input('Enter step'))
        a = float(input('Enter a'))
        s = int(input('Also please select a function'))

        mas_y, mas_x = [], []
        while x <= x2:
            if s == 1:
                try:
                    mas_x.append(x)
                    mas_y.append(func.g(x, a))
                    print(x, func.g(x, a))
                    x += h
                except ValueError:
                    print('Error')
            elif s == 2:
                try:
                    mas_x.append(x)
                    mas_y.append(func.f(x, a))
                    print(x, func.f(x, a))
                    x += h
                except ValueError:
                    print('Error')
            elif s == 3:
                try:
                    mas_x.append(x)
                    mas_y.append(func.y(x, a))
                    print(x, func.y(x, a))
                    x += h
                except ValueError:
                    print('Error')

        plt.plot(mas_x, mas_y)
        plt.title('График функции')
        plt.show()
    except KeyboardInterrupt:
        print('Bye')

    ex = input('Do you wanna repeat?(y or n)')
    if ex == 'y':
        pass
    else:
        raise SystemExit()
