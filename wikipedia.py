#https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy
import requests
from bs4 import BeautifulSoup
import random

def wikiArticle(url):
	_url = requests.get(
		url=url,
	)
	soup = BeautifulSoup(_url.content, 'html.parser')
	allLinks = soup.find(id="mw-content-text").find(class_="mw-parser-output").find_all("p")
	#content_div = soup.find_all("p")
	linkToScrape = 0
	#print(allLinks)
	for link in allLinks:
		for x in link.find_all("a"):
			print(x)
	#wikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

wikiArticle("https://en.wikipedia.org/wiki/Linux")
