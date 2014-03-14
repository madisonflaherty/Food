"""
Test for POOPS. Basic Parcing practice. 
"""
from html.parser import HTMLParser
from urllib import request

def openFile():
	"""Simply takes testfile and makes it into one large string
	Returns a list that represents all of the source html code of
	a webpage.
	"""
	#with open( "TestPage.html") as myfile:
	#	data = myfile.read()#.replace("\n", " ")
	#return data
	lst=[]
	for line in open("TestPage.html"):
		lst.append(line.strip())
	return lst

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

def printer(string):
	"""prints the websites html"""
	print("This is the website HTML: ")
	print(string)

def main():
	"""executes program"""
	parser = MyHTMLParser()
	parser2 = MyHTMLParser2()
	a = openFile()
	#will successfully pull every food item for all days available
	#on the site.
	for item in a:
		if item[0:25] == '<div class="location-menu':
			if item[25:30] == '-item':
				parser2.feed(item)
			else:
				parser.feed(item)
main()
