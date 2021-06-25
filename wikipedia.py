#https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy

import re
import requests
from bs4 import BeautifulSoup
import random
cnt = 1
def wikiArticle(url):
	_url = requests.get(
		url=url,
	)
	global cnt
	print(cnt)
	soup = BeautifulSoup(_url.content, 'html.parser')
	allLinks = soup.find(id="mw-content-text").find(class_="mw-parser-output").find_all("p")
	linkToScrape = 0
	for link in allLinks:
		temp = (str)(link)
		temp = Remove(temp, '(', ')') # Remove text inside brackets 
		link=BeautifulSoup(temp, "html.parser")
		for t in link('i'): # Remove text in italics which come first in html but actually are not the first para
		     t.clear()
		for x in link.find_all("a"):
			if(x['href'].find("/wiki/") == -1):
				continue
			if(x['href'].find("/wiki/Help") != -1):
				continue
			if(x['href'].find("/wiki/File") != -1):
				continue
			if(x['href'].find("wiktionary") != -1):
				continue
			#print(x)
			linkToScrape = x
			break
		if linkToScrape != 0 :
			break	
	#wikiArticle("https://en.wikipedia.org" + linkToScrape['href'])
	print(linkToScrape['href'])
	if cnt < 30:
		if(linkToScrape['href'] != ("/wiki/Philosophy")):
			cnt=cnt+1
			wikiArticle("https://en.wikipedia.org" + linkToScrape['href'])
	else:
		print("Could not find Philosophy in 30, do the articles loop?")
def Remove(string, c1, c2):
	result = ''
	# paren counts the number of brackets encountered
	paren= 0
	for ch in string:
		# if the character is ( then increment the paren
		# and add ( to the resultant string.
		if ch == c1:
			paren =paren+ 1
			result = result + c1
		
		# if the character is ) and paren is greater than 0,
		# then increment the paren and
		# add ) to the resultant string.
		elif (ch == c2) and paren:
			result = result + c2
			paren =paren- 1
		
		# if the character neither ( nor then add it to
		# resultant string.
		elif not paren or ():
			result += ch
	return result
wikiArticle("https://en.wikipedia.org/wiki/Special:Random")

#Terminology Self loops
#Rule_of_inference loops
