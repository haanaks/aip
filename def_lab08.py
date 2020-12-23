def points(x, y, x0, y0, r):
    if r ** 2 >= ((x - x0) ** 2 + (y - y0) ** 2):
        return 'yes'
    else:
        return 'no'


def counter(mas_x, mas_y, x0, y0, r):
    count = 0
    for x, y in zip(mas_x, mas_y):
        if r ** 2 >= ((x - x0) ** 2 + (y - y0) ** 2):
            count += 1
    return count
