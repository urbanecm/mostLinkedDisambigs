#!/usr/bin/env python
#-*- coding: utf-8 -*-

from wmflabs import db
conn = db.connect('cswiki')

sqlDisambigs = 'select page_title from page where page_id IN(select cl_from from categorylinks where cl_to="Wikipedie:Rozcestníky") and page_namespace=0 limit 10;'
sqlNumOfLinks = 'select count(*), pl_title from pagelinks where pl_title="###" and pl_from_namespace=0;'

cur = conn.cursor()
with cur:
	cur.execute(sqlDisambigs)
	data = cur.fetchall()

res = {}

for row in data:
	page = row[0]
	cur = conn.cursor()
	with cur:
		cur.execute(sqlNumOfLinks.replace('###', page))
		res[page] = cur.fetchall()[0][0]

sorted_res = sorted(res.items(), key=operator.itemgetter(1))
sorted_res.reverse()

wikitext = []
if len(sorted_res)>500:
	for i in range(0, 500):
		wikitext.append("# [[" + sorted_res[i][0] + "]] (" + sorted_res[i][1] + " odkazů)")
else:
	for i in sorted_res:
		wikitext.append("# [[" + i[0] + "]] (" + i[1] + " odkazů)")

for line in wikitext:
	print line
