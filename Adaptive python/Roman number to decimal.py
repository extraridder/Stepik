rom=(('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),
      ('I',  1))

res = 0
# s= input()
s = 'MCMLXXXIV'

#print(s)
while s > '':
    for r, v in rom:
        if s.startswith(r):
            # print()
            # print(s, res)
            res += v
            s = s[len(r):]
            # print(s, res)
            # print()

print(res)