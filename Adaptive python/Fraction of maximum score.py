def count_(list, value):
    return list_.count(value) / len(list_)

x = "A"
list_ = input().split(" ")
y = count_(list_, x)
print('{:.2f}'.format(y))