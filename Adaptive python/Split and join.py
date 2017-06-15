import re
s1 = input()
pattern = '\s+'
s2 = re.sub(pattern,'_',s1)
print(s2)