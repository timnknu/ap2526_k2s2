import json

L = [
    {'hello': 'cat', 12: 'meow'},
    'some text',
    3.1415
]

s = json.dumps(L, indent=2)
print(s)

with open('1.json', 'w') as f:
    json.dump(L, f, indent=2)