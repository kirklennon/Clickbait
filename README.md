# Clickbait
a Django-powered JSON-returning API that generates Apple clickbait articles to use as lorem ipsum

## Finding source articles

The first helper script uses the Azure Cognitive Services Bing News search API to find new articles that include "Apple" and keywords common to clickbait articles such as "shiny." It stores the new article URLs in a SQLite database.

## Scraping for gold

A second helper script pulls new URLs from the database, requests the article itself, and uses Beautiful Soup to extract paragraphs. Paragraphs are checked for relevance and, if they pass, are inserted into a paragraphs table.

## Putting it all together

The Django app is fairly simple and simply queries the database for ten random paragraphs. One view returns it as a [pre-generated HTML file](https://api.lennon.dev), along with some basic statistics about the database, while [another view returns a JSON](https://api.lennon.dev/json) list. This can be iterated through with some vanilla JavaScript as provided for on this [reference implementation page](https://lennon.dev/reader.html).



