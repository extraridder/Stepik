suit_card = ['C', 'D', 'H', 'S']
value_card = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

#print(value_card.index('10'))
def win(x1, x2, y1, y2, koz):
    if x2 == y2:
        if value_card.index(x1) > value_card.index(y1):
            print('First')
        else:
            print('Second')
    elif x2 != y2:
        if x2 == koz:
            print('First')
        elif y2 == koz:
            print('Second')
        else:
            print('Error')


x, y = input().split(" ")
koz = input()

xv = x[0:-1]
xs = x[-1]

yv = y[0:-1]
ys = y[-1]

#print(xv, xs)
#print(yv, ys)

win(xv, xs, yv, ys, koz)