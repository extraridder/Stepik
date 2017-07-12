def search_index(list_tmp, var):
    for x, y in enumerate(list_tmp):
        if y == var:
            print(x)
    if var not in list_tmp:
        print(None)

list_tmp = list(input().split(" "))
a = input()
search_index(list_tmp,a)