#https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy
import requests
from bs4 import BeautifulSoup
import random
cnt = 0
def wikiArticle(url):
	_url = requests.get(
		url=url,
	)
	global cnt
	soup = BeautifulSoup(_url.content, 'html.parser')
	allLinks = soup.find(id="mw-content-text").find(class_="mw-parser-output").find_all("p")
	#content_div = soup.find_all("p")
	linkToScrape = 0
	#print(allLinks)
	for link in allLinks:
		for x in link.find_all("a"):
			if(x['href'].find("/wiki/") == -1):
				continue
			if(x['href'].find("/wiki/Help") != -1):
				continue
			if(x['href'].find("/wiki/File") != -1):
				continue
			#print(x)
			linkToScrape = x
			break
		if linkToScrape != 0 :
			break	
	#wikiArticle("https://en.wikipedia.org" + linkToScrape['href'])
	print(linkToScrape['href'])
	if cnt < 25:
		if(linkToScrape['href'].find("/wiki/Philosophy") == -1):
			cnt=cnt+1
			print(cnt)
			wikiArticle("https://en.wikipedia.org" + linkToScrape['href'])
	
wikiArticle("https://en.wikipedia.org/wiki/Special:Random")
