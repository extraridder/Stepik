x, y = input().split(" ")
matrix = list()
for i in range(0, int(x)):
    matrix.append(list(input().split(" ")))
for each in zip(*matrix):
    print(" ".join(each))