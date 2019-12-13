import requests
import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

subscription_key = 'CONFIDENTIAL'
search_term = '"apple" ("shiny" OR "dump" OR "analyst" OR "rumor")'
search_url = 'https://clickbait-searcher.cognitiveservices.azure.com/bing/v7.0/news/search'

headers = {'Ocp-Apim-Subscription-Key' : subscription_key}
params  = {'q': search_term, }
# 'freshness': 'Week'

response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

for article in search_results['value']:
	url = article['url']
	if '?' in url:
		url = url.split('?', 1)[0]
	try:
		cur.execute('INSERT OR IGNORE INTO Source (url, visited) VALUES (?, 0)', (url,))
	except:
		print('failed to save: ', url)

conn.commit()
conn.close()