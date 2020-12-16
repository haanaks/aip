import my_functions


a = float(input('Please enter a'))
x = float(input('Please enter x'))
s = int(input('Also please select a function: [G-1];[F-2];[Y-3]'))

if s == 1:
    try:
        print(my_functions.g(x, a))
    except ValueError:
        print('error')
elif s == 2:
    try:
        print(my_functions.f(x, a))
    except ValueError:
        print('error')
elif s == 3:
    try:
        print(my_functions.y(x, a))
    except ValueError:
        print('error')
else:
    print('Sorry,you have wrote invalid number')
