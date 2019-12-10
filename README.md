# Clickbait
a Django-powered JSON-returning API that generates Apple clickbait articles to use as lorem ipsum

## Finding source articles

The first helper script uses the Azure Cognitive Services Bing News search API to find new articles that include "Apple" and keywords common to clickbait articles such as "shiny." It stores the new article URLs in a SQLite database.

## Scraping for gold

A second helper script pulls new URLs from the database, requests the article itself, and uses Beautiful Soup to extract paragraphs. Paragraphs are checked for relevance and, if they pass, are inserted into a paragraphs table.

## Putting it all together

This part isn't written yet but upon request, paragraphs are pseudo-randomly (limited to one paragraph per source article) assembled into a new article.

## TBD

I haven't decided yet what to do about titles. I may manually assemble a format for them and randomly fill in the blanks.
