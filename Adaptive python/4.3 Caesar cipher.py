def encrypt(strin, displace):
    tmp_string = str()
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    for each in strin:
        tmp_string += alphabet[alphabet.index(each) + (displace % 27)]
    print('Result: "{}"'.format(tmp_string))

n = int(input())
string = input()
encrypt(string, n)

