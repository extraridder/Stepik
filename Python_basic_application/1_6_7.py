def searching_dict(x, y, i):
    #print(x,y,i)
    if i == 0:
        global answer
        answer = 'No'
    if y not in list(d.keys()):
        if i == 0:
            print(answer)
        return
    if d[y] == 'None':
        print(answer)
        return
    if x in d[y]:
        answer = 'Yes'
    elif x not in d[y]:
        for each in d[y]:
            searching_dict(x, each, 1)
    if i == 0:
        print(answer)

#searching_dict('D', 'A', 0)

d = dict()
n = int(input())

while n > 0:
    tmp_request = input()
    if len(tmp_request) == 1:
        d[tmp_request] = 'None'
    else:
        child, parent = tmp_request.split(":")
        if len(str(parent).strip()) != 1:
            tmp_list = list(str(parent).strip().replace(" ", ""))
            d[str(child).strip()] = tmp_list
        else:
            d[str(child).strip()] = [str(parent).strip()]
    n -= 1
#print(d)

q = int(input())

while q > 0:
    parent, child = input().split(" ")
    searching_dict(parent, child, 0)
    q -= 1