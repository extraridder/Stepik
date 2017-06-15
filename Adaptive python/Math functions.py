def math_func(x):
    if x <= -2:
        # print('x <= -2')
        return 1 - (x +2) ** 2
    elif (x >= -2) and (x <= 2):
        # print('(x >= -2) or (x <= 2)')
        return -x / 2
    else:
        # print('else')
        return (x - 2) ** 2 + 1

x = float(input())
print(math_func(x))