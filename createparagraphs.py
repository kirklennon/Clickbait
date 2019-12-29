from bs4 import BeautifulSoup
import sqlite3
import requests

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute('SELECT url, article_id FROM Source WHERE visited=0 LIMIT 1')
try:
	row = cur.fetchone()
	url = row[0]
	article_id = row[1]
except:
	print('All urls checked')
	quit()
print('Requesting: ', url)
try:
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
except:
	print('Failure to download/parse page')

terms = ['Apple', 'iPhone', 'iPad', 'AirPods']
skip = ['Motley Fool']
counter = 0
paragraphs = soup.find_all('p')
for p in paragraphs:	
	if len(p.text.strip()) < 80:
		continue
	if any (x in p.text for x in skip):
		continue
	if not any (x in p.text for x in terms):
		continue
	cur.execute('INSERT INTO Paragraphs (text, source_article) VALUES ( ?, ? )', ( p.text.strip(), article_id ) )
	counter += 1

print('Added', counter, 'paragraphs!')
cur.execute('UPDATE Source SET visited=1 WHERE article_id=?', (article_id, ) )
	
conn.commit()
conn.close()
