import sqlite3

conn = sqlite3.connect('db1')

conn.row_factory = sqlite3.Row

cur = conn.cursor()
yearfrom = input('Рік, з якого показувати книжки:')

params = (yearfrom, )

cur.execute(f"SELECT * FROM books WHERE year > ? ORDER BY title, year DESC;", params)
for e in cur.fetchall():
    print(e['year'], e['title'])


# for e in cur.execute(f"SELECT * FROM books WHERE year > ? ORDER BY title, year DESC;", params):
#     print(e['year'], e['title'])

conn.close()