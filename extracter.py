import sqlite3

body = []

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute('SELECT text FROM api_paragraph')
rows = cur.fetchall()
for row in rows:
	body.append(row[0])
conn.close()

page = open('data.txt','w+')
page.write('\n'.join(body))
page.close()
