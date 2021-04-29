#https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy
import requests
from bs4 import BeautifulSoup
import random

def wikiArticle(url):
	_url = requests.get(
		url=url,
	)
	soup = BeautifulSoup(_url.content, 'html.parser')
	allLinks = soup.find(id="bodyContent").find_all("a")
	#random.shuffle(allLinks)
	linkToScrape = 0

	for link in allLinks:
		# We are only interested in other wiki articles
		if (link['href'].find("/wiki/") == -1) :
			continue
		if (link['href'].find("/wiki/File") != -1): 
			continue
		if (link['href'].find("/wiki/Wikipedia") != -1): 
			continue

		# Use this link to scrape
		linkToScrape = link
		break
	print(linkToScrape)
	#link=(str)(soup.p.wrap(soup.new_tag("a href")))
	#print(link)
	#start=link.index('<a href="/wiki/')
	#end=link.index('"') #gives last index :(
	#res = [i for i in range(len(link)) if link.startswith('"', i)]
	#end=int(res[1])
	#name=link[start+15:end]
	#print(name)
	#name = name.replace(' ', '_')
	#print(name)
	#wikiArticle("https://en.wikipedia.org/wiki/" + name)
	#wikiArticle("https://en.wikipedia.org" + linkToScrape['href']) NOT NOW

wikiArticle("https://en.wikipedia.org/wiki/Linux")
