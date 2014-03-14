"""
Test 2. 
"""
#pyramid imports
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
#pyquery imports
from pyquery import PyQuery as pq
from lxml import etree
import urllib

def parser(d): 
	p = d(".current .menu-day-content").items()
	for each in p:
		thing = str(each.html())
		thing2 = thing.replace("\t", "").strip()
		lst = thing2.split("\n")
		for item in lst:
			if len(item) < 7:
				continue
			item2 = pq(item)
			print type(item2)
			return item2#.text()
def main():
	#temporarily will only work with commons
	d = pq("http://www.rit.edu/fa/diningservices/commons")
	#day = d(".current").html
	#print ("Meals available on ", day)
	return Response(parser(d))

if __name__ == '__main__':
	config = Configurator()
	config.add_view(main)
	app = config.make_wsgi_app()
	server = make_server("129.21.105.93", 8080, app)
	server.serve_forever()
main()
