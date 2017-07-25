rom=(('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),
      ('I',  1))

res = ''
# s= int(input())
s = 1000

#print(s)
while s != 0:
    for r, v in rom:
        # print(s, res)
        if v <= s:
            s -= v
            res += r
            break
print(res)