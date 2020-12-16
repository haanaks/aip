import entering as en
import my_functions as func

g_values, f_values, y_values = [], [], []
en.x, en.x2, en.h, en.a = float(en.x), float(en.x2), float(en.h), float(en.a)
while True:
    try:
        while en.x <= en.x2:
            try:
                g_values.append(func.g(en.x, en.a))
                en.x += en.h
            except ValueError:
                print('Error')
            try:
                f_values.append(func.f(en.x, en.a))
                en.x += en.h
            except ValueError:
                print('Error')
            try:
                y_values.append(func.y(en.x, en.a))
                en.x += en.h
            except ValueError:
                print('Error')
        print(f'G: {g_values} \nF: {f_values} \nY: {y_values}')
    except KeyboardInterrupt:
        print('bye')
    ex = input('Do you wanna repeat?(y or n)')
    if ex == 'y':
        pass
    else:
        raise SystemExit()
