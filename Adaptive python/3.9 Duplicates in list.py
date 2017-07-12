def search_dupl(l):
    tmp_list = list()
    for each in l:
        if l.count(each) > 1:
            tmp_list.append(each)
    tmp_list = sorted(tmp_list)
    print(" ".join(sorted(set(tmp_list))))


input_list = list(input().split(" "))
search_dupl(input_list)