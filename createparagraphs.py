from bs4 import BeautifulSoup
import sqlite3
import requests

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
while True:
	row = None
	cur.execute('SELECT url, id FROM api_source WHERE visited=0 LIMIT 1')
	row = cur.fetchone()
	if row is None:
		print('All urls checked')
		break
	else:
		url = row[0]
		article_id = row[1]
	print('Requesting: ', url)
	try:
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')
	except:
		print('Failure to download/parse page')

	terms = ['Apple', 'iPhone', 'iPad', 'AirPods', 'MacBook']
	skip = ['motley fool', 'macrumors', 'giveaway']
	counter = 0
	paragraphs = soup.find_all('p')
	for p in paragraphs:	
		if len(p.text.strip()) < 80:
			continue
		if any (x in p.text.lower() for x in skip):
			continue
		if not any (x in p.text for x in terms):
			continue
		cur.execute('INSERT INTO api_paragraph (text, source_id) VALUES ( ?, ? )', ( p.text.strip(), article_id ) )
		counter += 1

	print('Added', counter, 'paragraphs!')
	cur.execute('UPDATE api_source SET visited=1 WHERE id=?', (article_id, ) )
	
conn.commit()
conn.close()