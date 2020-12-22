from collections import defaultdict
import entering as en
import my_functions as func

values = defaultdict(list)
en.x, en.x2, en.h, en.a = float(en.x), float(en.x2), float(en.h), float(en.a)
while True:
    try:
        while en.x <= en.x2:
            try:
                values[1].append(func.g(en.x, en.a))
                values[2].append(func.f(en.x, en.a))
                values[3].append(func.y(en.x, en.a))
                en.x += en.h
            except ValueError:
                print('Error')
        print(f'G: {values[1]} \nF: {values[2]} \nY: {values[3]}')
    except KeyboardInterrupt:
        print('bye')
    ex = input('Do you wanna repeat?(y or n)')
    if ex == 'y':
        pass
    else:
        raise SystemExit()
