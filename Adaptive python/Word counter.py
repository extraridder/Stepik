def add_el(dict, value):
    if value in dict.keys():
        dict[value] += 1
    else:
        dict[value] = 1
d = dict()
list_words = input().lower().split(' ')
# print(list_words)
for each in list_words:
    add_el(d, each)

# print(d)
for key,value in d.items():
    print(key+ ' '+ str(value))