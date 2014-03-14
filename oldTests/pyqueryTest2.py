"""
Test 2. 
"""

from pyquery import PyQuery as pq
from lxml import etree
import urllib
import pprint

def parser(d): 
	p = d(".current .menu-day-content").items()
	for each in p:
		thing = str(each.html())
		thing2 = thing.replace("\t", "").strip()
		lst = thing2.split("\n")
		lst2 = []
		for item in lst:
			if len(item) < 7:
				continue
			lst2.append(item)
		return toCategory(lst2)
	#print only occurs if there is nothing within .current
	print "It appears the location is closed or there are no specials."

def toCategory(text):
	d = dict()
	name = None
	for line in text:
		#print line
		if(line == None):
			continue
		print (type(line))
		j = pq(line)
		print type(j)
		if name == None or len(list(j(".location-menu-category"))) == 1:
			name = j(".location-menu-category").html()
			if name != None:
				d[name] = list()
		elif j(".location-menu-item").html() != None:
			d[name].append(j(".location-menu-item").html())
	return d


def main():
	#temporarily will only work with commons
	d = pq("http://www.rit.edu/fa/diningservices/commons")
	#day = d(".current").html
	#print ("Meals available on ", \day)
	parser(d)

main()
