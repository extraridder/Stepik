def simlifier(x):
    if x > 0:
        return x % 27
    elif x == 0:
        return x
    elif x < 0:
        return int(str(-(abs(x) % 27)))


def encrypt(strin, displace):
    tmp_string = str()
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    displace = simlifier(displace)
    print("dis=", displace)
    for each in strin:
        tmp_string += alphabet[alphabet.index(each) + displace]
    return 'Result: "{}"'.format(tmp_string)


test_case = [(3, 'i am caesar', 'Result: "lcdpcfdhvdu"'), (-2, 'az', 'Result: "zx"'), (27, 'abc', 'Result: "abc"'), (-57, 'abc', 'Result: "yz "'),
             (0, 'i am caesar', 'Result: "i am caesar"'), (1, 'abxxyz', 'Result: "bcdyz "')]
i = 0
for n, s, r in test_case:
    print(i, s, n)
    print(r, encrypt(str(s), int(n)))
    assert encrypt(s, n) == r
    i += 1



'''

В комментраъ решение задачки.
 a = int(input())
b = input().strip()
alfavit = " abcdefghijklmnopqrstuvwxyz"
shifr = []
for i in b:
    shifr.append(alfavit[(alfavit.index(i)+a)%len(alfavit)])
mySTR = "".join(shifr)
print('Result: "{}"'.format(mySTR)) 
'''


