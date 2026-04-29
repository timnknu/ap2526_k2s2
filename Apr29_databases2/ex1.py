# custom functions for sqlite

import sqlite3
import re

conn = sqlite3.connect('../Apr22_databases1/db1')

conn.row_factory = sqlite3.Row

def myfuncimpl(*args):
    d = args[0]
    if re.match(r'\d{4}-\d{2}-\d{2}', d):
        return d
    elif re.match(r'\d{2}-\d{2}-\d{4}', d):
        vals = d.split('-')
        res = vals[2] + '-' + vals[0] + '-' + vals[1]
        return res
    else:
        raise ValueError('Wrong date format')

conn.create_function('myf', -1, myfuncimpl)

cur = conn.cursor()


cur.execute(f"SELECT *, myf(date) as X  FROM brth;")
for e in cur.fetchall():
    print(dict(e))


# for e in cur.execute(f"SELECT * FROM books WHERE year > ? ORDER BY title, year DESC;", params):
#     print(e['year'], e['title'])

conn.close()