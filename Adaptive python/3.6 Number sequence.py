def seq_num(x):
    result_list = list()
    num = 1
    while len(result_list) <= x:
        result_list.extend(num for j in range(num))
        num += 1
    return " ".join(map(str, result_list[:x]))

print(seq_num(int(input())))