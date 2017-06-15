a, op, b = input().split(" ")
if op == 'plus':
    print(int(a) + int(b))
elif op == 'minus':
    print(int(a) - int(b))
elif op == 'multiply':
    print(int(a) * int(b))
else:
    print(int(a) / int(b))