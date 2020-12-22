import entering as en
import my_functions as func
from collections import defaultdict

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
        with open('function_values.txt', 'w+') as f:
            for key in range(1, 4):
                f.write(';'.join(str(values[key])))
                values[1].append(f.read())
        print(values[1])
    except KeyboardInterrupt:
        print('bye')
    ex = input('Do you wanna repeat?(y or n)')
    if ex == 'y':
        pass
    else:
        raise SystemExit()
