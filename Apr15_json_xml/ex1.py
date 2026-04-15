import json

with open ('sample.json') as f:
    txt = f.read()

d = json.loads(txt)
print(type(d))
print(d['universities'][2]['un'])