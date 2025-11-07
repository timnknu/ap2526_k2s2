import re

with open('ex1.txt') as f:
    txt = f.read()
    print(type(txt))
patt = r'(\d{4})/(\d{1,2})/(\d{1,2})'
# res = re.findall(patt, txt)
# print(res)

def my_replacer(m):
    #print('FUNC:', m.group(), m.groups(), m.group(2))
    #return 'REPLACED!!!'
    year, month, day = m.groups()
    if len(month)==1:
        month = "0" + month
    return day + "." + month + "." + year
res = re.sub(patt, my_replacer, txt)
print(res)