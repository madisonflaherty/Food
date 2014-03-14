"""
Test to determine easiness of pulling HTML from a website with python
Author: Madison Flaherty
Date: January 14, 2014
"""

import urllib.request
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
	"""
	creates second parser
	"""

	def handle_data(self, data):
		
		print("\n", data)

class MyHTMLParser2(HTMLParser):
	"""
	creates second parser
	"""

	def handle_data(self, data):
		print("    ", data)

def openURL(loc):
	"""
	Takes in the urls of the rit food websites. These update daily.
	"""
	if loc == "commons":
		commons = urllib.request.urlopen("http://www.rit.edu/fa/diningservices/commons")
		return commons
	if loc == "brick":
		brick = urllib.request.urlopen("http://www.rit.edu/fa/diningservices/brickcity")
		return brick
	if loc == "gv":
		gv = urllib.request.urlopen("http://www.rit.edu/fa/diningservices/gvcantinagrille")
		return gv
	if loc == "cross":
		cross = urllib.request.urlopen("http://www.rit.edu/fa/diningservices/crossroads")
		return cross
	if loc == "gracies":
		gracies = urllib.request.urlopen("http://www.rit.edu/fa/diningservices/content/gracies")
		return gracies
	if loc == "rSZ":
		rSZ = urllib.request.urlopen("http://www.rit.edu/fa/diningservices/content/ritz-sports-zone")
		return rSZ
	else: 
		return None

def ask():
	answer = input("Which dining location would you like to see? ")
	url = openURL(answer)
	if url == None:
		print("	No such dinning location exists...")
		ask()
	else:
		#print(url)
		#Print the day's menu'
		#url = str(url.read)
		#print(url)
		lst = lister(url)
		#print(lst)
		parcer(lst)

def parcer(lst):
	parser = MyHTMLParser()
	parser2 = MyHTMLParser2()
	for item in lst:
		value = '<div class="location-menu'
		print(item[0:25])
		if item[0:25] == value: #'<div class="location-menu':
			#print(item)
			if item[25:30] == '-item':
				parser2.feed(str(item))
			else:
				parser.feed(str(item))

def lister(url):
	lst = []
	for line in url:
		line = str(line)
		lst.append(line[2:].strip())#.replace("'", ""))
	return lst


def main():
	ask()

main()
