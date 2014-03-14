from pyquery import PyQuery as pq
from lxml import etree
import urllib

def toCategory(text):
	d = dict()
	name = None
	for line in text:
		if(line == None):
			continue
		j = pq(line)
		if name == None or len(list(j(".location-menu-category"))) == 1:
			name = j(".location-menu-category").html()
			d[name] = list()
		elif j(".location-menu-item").html() != None:
			d[name].append(j(".location-menu-item").html())
	print d
	return d


toCategory(open('in.txt', 'r').read().strip().split('\n'))
