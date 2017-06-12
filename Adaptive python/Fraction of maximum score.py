def count_(list, value):
    return list_.count(value) / len(list_)

x = "B"
list_ = input().split(" ")
y = count_(list_, x)
print('{:.2f}'.format(y))