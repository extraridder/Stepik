start_num = int(input())
result_list = list()
tmp_num = start_num
while tmp_num != 1:
    result_list.append(int(tmp_num))
    if tmp_num % 2 == 0:
        tmp_num /= 2
    else:
        tmp_num = 3 * tmp_num + 1
result_list.append(1)
print(result_list)
print(" ".join(map(str, result_list)))
