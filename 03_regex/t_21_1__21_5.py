import re

with open('ex1.txt') as f:
    txt = f.read()
    print(type(txt))
patt = r'(?P<v1>(?P<year>\d{4})[/\-](?P<month>\d{1,2})[/\-](?P<day>\d{1,2}))|(?P<v2>(?P<day2>\d{1,2})\.(?P<month2>\d{1,2})\.(?P<year2>\d{4}))'
# res = re.findall(patt, txt)
# print(res)

def my_replacer(m):
    print('FUNC:', m.group(), m.groups(), m.group(2), m.groupdict())
    #return 'REPLACED!!!'
    # year = m.groupdict()['year']
    # month = m.groupdict()['month']
    # day = m.groupdict()['day']
    # if len(month)==1:
    #     month = "0" + month
    # return day + "." + month + "." + year
    if m['v1'] is not None:
        return m['day'] + '.' + m['month'] + '.' + m['year']
    else:
        return m['day2'] + '.' + m['month2'] + '.' + m['year2']
res = re.sub(patt, my_replacer, txt)
print(res)