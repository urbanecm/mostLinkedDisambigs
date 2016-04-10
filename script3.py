#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pywikibot

site = pywikibot.Site("cs", "wikipedia")

page = pywikibot.Page(site, u'Wikipedista:UrbanecmBot/Pískoviště')

text = page.text

array = text.split("\n")

result = array[:500]

text = ""
for item in result:
	text += item + "\n"

print text

page = pywikibot.Page(site, u"Wikipedista:UrbanecmBot/Pískoviště 2")
page.text = text
page.save(u"robotí editace pískoviště")
