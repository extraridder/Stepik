def interval(x):
    if x == -10 or (x > -5 and x <= 3) or (x > 8 and x < 12) or (x >= 16):
        print('True')
    else:
        print('False')
x = int(input())
interval(x)