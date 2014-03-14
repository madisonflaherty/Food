"""
Test to determine whether pyquery will be a valid alternative to current
methods of parsing
Author: Madison Flaherty
Date: February 8, 2014
"""

from pyquery import PyQuery as pq
from lxml import etree
import urllib

def printer(d):
		
	loc = d(".current .location-menu-category").items()
	items = d(".current .location-menu-item").items()
	for i in range(len(loc)):
		#print(each.html())
		print loc[i]
		print items[i]
	
def curry(loc, item):
	loc = list(i for i in loc)
	item = list(n for n in item)
	def nextTwo():
		if(len(loc) > 0):
			itmLst = []
			if(len(item) > 0):
				lst.append(item.pop(0))
					return (loc.pop(0), itmLst)
	return nextTwo

def main():
	"""
	Initiates the program.
	"""
	#Temporarily will only work with commons
	d = pq("http://www.rit.edu/fa/diningservices/commons")
	#printer(d)
	loc = d(".current .location-menu-category").items()
	items = d(".current .location-menu-item").items()
	func = curry(loc, items)
	while(True):
		n = func()
		if(n == None):
			break
		print n[0].html()
		print n[1].html()
main()
