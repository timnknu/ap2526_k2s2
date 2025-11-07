import re
import datetime

d = datetime.datetime.now()
print(d.year, d.month, d.day, d.second, d.strftime("%d.%m.%Y"))

with open('ex1.txt') as f:
    txt = f.read()
    print(type(txt))
patt = r'_{2}\._{2}\._{4}'

def my_replacer(m):
    print('FUNC:', m.group(), m.groups())
    return d.strftime("%d.%m.%Y")
res = re.sub(patt, my_replacer, txt)
print(res)