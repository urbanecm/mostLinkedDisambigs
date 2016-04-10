#!/usr/bin/env python
#-*- coding: utf-8 -*-

##################### INIT ##################
#Import
import pywikibot
import urllib2
import json
import operator

#Init lib
site = pywikibot.Site("cs", "wikipedia")


################### PROGRAM #################

#Get and parse JSON data from Quarry
response = urllib2.urlopen("https://quarry.wmflabs.org/run/46181/output/0/json?download=true")
json_data = response.read()
parsed_json = json.loads(json_data)

#Init loop
i = 0
links_res = {} 
print "START LOOP"
#Run for every disambig
for item in parsed_json['rows']:
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

print text

page = pywikibot.Page(site, u"Wikipedista:UrbanecmBot/Pískoviště")
page.text = text
page.save(u"Robotická editace pískoviště")
