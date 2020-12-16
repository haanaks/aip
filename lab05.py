import entering as en
import my_functions as func

k = 0
shablon = input('Enter shablon')
func_values = []
en.x, en.x2, en.h, en.a, en.s = float(en.x), float(en.x2), float(en.h), float(en.a), float(en.s)
while True:
    try:
        while en.x <= en.x2:
            if en.s == 1:
                try:
                    func_values.append(func.g(en.x, en.a))
                    en.x += en.h
                except ValueError:
                    print('Error')
            elif en.s == 2:
                try:
                    func_values.append(func.f(en.x, en.a))
                    en.x += en.h
                except ValueError:
                    print('Error')
            elif en.s == 3:
                try:
                    func_values.append(func.y(en.x, en.a))
                    en.x += en.h
                except ValueError:
                    print('Error')
        print('; '.join(str(i) for i in func_values))
        for i in func_values:
            if str(i) == shablon:
                k += 1
        print(k)
    except KeyboardInterrupt:
        print('bye')
    ex = input('Do you wanna repeat?(y or n)')
    if ex == 'y':
        pass
    else:
        raise SystemExit()
