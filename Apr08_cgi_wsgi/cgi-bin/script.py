#!/bin/env python

import os
import urllib
import urllib.parse


print("Content-type: text/plain")
print()

print("This is the form result")
qs = os.environ.get('QUERY_STRING', '')
cl = os.environ.get('CONTENT_LENGTH', '')
print(qs)
print(cl)

par_dict = urllib.parse.parse_qs(qs)
print("DICT:", par_dict)