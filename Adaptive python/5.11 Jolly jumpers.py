def jolly_jumpers(input_list):
    len_list = len(input_list)
    dif = len_list - 1
    # print(len_list)
    dif_list = list()
    if len_list == 1:
        print('Jolly')
        return
    else:
        for i in range(1,len_list):
            # print(abs(int(input_list[i]) - int(input_list[i - 1])))
            dif_list.append(abs(int(input_list[i]) - int(input_list[i - 1])))
    if set(dif_list) == set(list(range(1,len_list))):
        print('Jolly')
        return
    else:
        print('Not jolly')


# x = list('1 -3 -4 -1 1'.split(" "))
x = list('1 3 5'.split(" "))
# print(x)
jolly_jumpers(x)