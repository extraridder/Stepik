import re
string_ = 'aaaa'
pattern = 'aa'
str_d = string_
list_ = list()
i = 0
while len(str_d) >= len(pattern):
    print(str_d.index(pattern))
    list_.append(str_d.index(pattern)+ i)
    i += len
    str_d = str_d[1:]
