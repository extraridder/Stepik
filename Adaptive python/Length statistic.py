def add_len(dict, value):
    if value in dict.keys():
        dict[value] += 1
    else:
        dict[value] = 1
list_words = input().split(' ')
# print(list_words)
d = dict()
for each in list_words:
    add_len(d, len(each))
# print(d)
len_list_sort = sorted(d.keys())
# print(len_list_sort)
for each in len_list_sort:
    print(str(each)+': '+str(d[each]))