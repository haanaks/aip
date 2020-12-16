import my_functions as func

while True:
    try:
        x = float(input('Enter lowest x'))
        x2 = float(input('Enter highest x'))
        h = float(input('Enter step'))
        a = float(input('Enter a'))
        s = int(input('Also please select a function'))
        func_values = []
        while x <= x2:
            if s == 1:
                try:
                    print(f"| X = {x} | Y = {func.g(x, a)} ")
                    func_values.append(func.g(x, a))
                    x += h
                except ValueError:
                    print('Error')
            elif s == 2:
                try:
                    print(f"| X = {x} | Y = {func.f(x, a)}   ")
                    func_values.append(func.f(x, a))
                    x += h
                except ValueError:
                    print('Error')
            elif s == 3:
                try:
                    print(f"| X = {x} | Y = {func.y(x, a)} ")
                    func_values.append(func.y(x, a))
                    x += h
                except ValueError:
                    print('Error')
    except KeyboardInterrupt:
        print('Bye')
    print(f"max = {max(func_values)}  min = {min(func_values)}")
    ex = input('Do you wanna repeat?(y or n)')
    if ex == 'y':
        pass
    else:
        raise SystemExit()
