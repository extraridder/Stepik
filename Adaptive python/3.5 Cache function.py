tmp_dict = dict()
def cache(x):
    if x in tmp_dict:
        print(tmp_dict[x])
    else:
        tmp_dict[x] = f(x)
        print(tmp_dict[x])

n = int(input())
while n > 0:
    k = int(input())
    cache(k)
    n -= 1