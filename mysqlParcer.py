"""
"""

from pyquery import PyQuery as pq
from lxml import etree
import urllib
import pprint
import MySQLdb
import re
db = MySQLdb.connect(host="localhost",
		user="root", 
		db = "poops")

cur = db.cursor()

def parser(d): 
	"""
	Parses through HTML and for each item that is under the class "current"
	and the class "menu-day-left" will be parsed. 
	***If RIT websites get updated, this will likely be the only place that
	needs revisions!***
	"""
	#Find items within the class "current" and "menu-day-content"
	p = d(".current .menu-day-content").items()

	#Go through them, get rid of all the junk
	for each in p:
		thing = str(each.html())
		thing2 = thing.replace("\t", "").strip()
		lst = thing2.split("\n")
		lst2 = []
		for item in lst:
			#Sometimes RIT websites are dumb and have empty
			#<div></div> tags... this gets rid of those...
			if len(item) < 7:
				continue
			#Appends items that are in this format:
			#<div class="location-menu-category">Soups</div>
			#or
			#<div class="location-menu-item">Chefs Choice</div>
			lst2.append(item)
		return toCategory(lst2)
	# only occurs if there is nothing within .current
	return toCategory(["It appears the location is closed or there are no specials."])

def toCategory(text):
	"""
	Take in the parsed lists of categorys/items from each venue and further
	parses them so that items within a certain category are put into a
	dictionary of category(key) and food items (values).
	"""
	d = dict()
	name = None
	for line in text:
		#skip line if None
		if(line == None):
			continue
		#makes each html line into a pyquery object
		j = pq(line)
		#If it is a valid category title, make it into the key, and make
		#its value an empty list
		if name == None or len(list(j(".location-menu-category"))) == 1:
			name = j(".location-menu-category").html()
			if name != None:
				d[name] = list()
		#Everything until the next valid category will be put into the 
		#last categories value list.
		elif j(".location-menu-item").html() != None:
			d[name].append(j(".location-menu-item").html())
	return d

def toDatabase(dic):
	"""
	Take the dictionary of information and put it into the mySQL database.
	"""
	# input all the food locations
	# The following is commented out because it only needs to be run once in
	# order to get the restaurant locations
	#for key in dic:
	#	exe = "INSERT INTO location (name) VALUES (\'" + key + "\')"
	#	cur.execute(exe)
	#	cur.execute("COMMIT")
	#	#input all the food category names

	# Takes in all of the categories and puts them in the category table
	cur.execute("DELETE FROM category;")
	for key in dic:
		for item in dic[key]:
			
			exe = "insert into category (name) values('%s');" % item
			cur.execute(exe)
	db.commit()

	rest = None
	cat = None
	locid = None
	catid = None
	cur.execute("DELETE FROM food_items;")
	for key in dic: 
		rest = key
		for item in dic[key]:
			cat = item
			for food in dic[key][item]:
				cur.execute("select id from location where name = \'" + rest + "\'")
				locid = int(cur.fetchone()[0])
				cur.execute("select id from category where name = \'" + item + "\'")
				catid = int(cur.fetchone()[0])
				exe = "INSERT INTO food_items (name, fk_locid, fk_catid) VALUES ('%s', '%d', '%d');" % (re.escape(food), locid, catid)
				cur.execute(exe)
				#print food + str(locid) + str(catid)
				exe = "select * from food_items left outer join location on food_items.fk_locid = location.id left outer join category on food_items.fk_catid = category.id;"
				cur.execute(exe)
	db.commit()
def main():
	"""
	Initializes P.O.O.P.S
	Takes in all the website addresses, creates a dictionary where the key is 
	the location's name and the value is the the location's website address.'
	"""
	#links for each of the different food venues
	#The pq is PyQuery... so each of the d# are actually the parced raw html
	
	#Commons:
	d1 = pq("http://www.rit.edu/fa/diningservices/commons")
	#Brick City:
	d2 = pq("http://www.rit.edu/fa/diningservices/brickcity")
	#Global Village Cantina and Grill:
	d3 = pq("http://www.rit.edu/fa/diningservices/gvcantinagrille")
	#CrossRoads
	d4 = pq("http://www.rit.edu/fa/diningservices/crossroads")
	#Gracies:
	d5 = pq("http://www.rit.edu/fa/diningservices/content/gracies")
	#Ritz Sports Zone:
	d6 = pq("http://www.rit.edu/fa/diningservices/content/ritz-sports-zone")
	
	#Create Dictionary
	d = {'Commons' : d1, 'Brick City' : d2, 'Global Village Grille' :d3,
			'Crossroads' : d4, 'Gracies' : d5,  "Ritz" : d6 }
	
	#For each key in the dictionary, parse the value (the webiste) and change the
	#value to the parsed HTML
	for key in d:
		dic = parser(d[key])
		d[key] = dic
	toDatabase(d)
main()
