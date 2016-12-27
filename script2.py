#!/usr/bin/env python
#-*- coding: utf-8 -*-

##################### INIT ##################
#Import
import pywikibot
import urllib2
import json
import operator
from wmflabs import db
conn = db.connect('cswiki')

#Init lib
site = pywikibot.Site("cs", "wikipedia")


################### PROGRAM ################
res = urllib2.urlopen('https://quarry.wmflabs.org/run/138638/output/0/json?download=true')
from_quarry = res.read()
from__quarry = json.loads(from_quarry)
data = from__quarry['rows']

#Init loop
i = 0
links_res = {} 
print "START LOOP"
#Run for every disambig
for item in data:
	#Find page in Wikipedia
	page = pywikibot.Page(site, item[0])
	#Select links
	links = page.backlinks()
	#Init loop
	j = 0
	#Run for every link
	#Count links
	for link in links:
		j += 1
	#Add to result
	links_res[item[0]] = j
	print "----------------------------------"

	#End of loop
#	i += 1
#	if i == 100:
#		break

print "END LOOP"

sorted_links = sorted(links_res.items(), key=operator.itemgetter(1), reverse=True)

#Make text version of result
text = ""
for item in sorted_links:
	text += "# [[" + item[0] + "]] ([[Special:Whatlinkshere/" + item[0] + "|" + str(item[1]) + " odkazu]])\n"

#print text

page = pywikibot.Page(site, u"Wikipedista:UrbanecmBot/Pracovní")
page.text = text
page.save(u"update")
