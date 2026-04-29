# custom functions for sqlite

import sqlite3

conn = sqlite3.connect('../Apr22_databases1/db1')

conn.row_factory = sqlite3.Row

def myfuncimpl(*args):
    print('myfuncimpl called with', args)
    return -100500

conn.create_function('myf', -1, myfuncimpl)

cur = conn.cursor()


cur.execute(f"SELECT *, myf(date) as X  FROM brth;")
for e in cur.fetchall():
    print(dict(e))


# for e in cur.execute(f"SELECT * FROM books WHERE year > ? ORDER BY title, year DESC;", params):
#     print(e['year'], e['title'])

conn.close()