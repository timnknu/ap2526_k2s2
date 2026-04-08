#!/bin/env python

import os
import urllib
import urllib.parse
import sys


print("Content-type: text/plain")
print()

print("This is the form result")
qs = os.environ.get('QUERY_STRING', '')
cl = os.environ.get('CONTENT_LENGTH', '0')
print(qs)
print(cl)
try:
    cl = int(cl)
except:
    cl = 0

post_data = sys.stdin.read(cl)
print('POST DATA:', )
par_dict = urllib.parse.parse_qs(post_data)
print("DICT:", par_dict)