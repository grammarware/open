#! /usr/bin/env python
# this script goes over partOf and curates it according to sameAs
import sys

names = {}

sa = open('rdf/sameAs.really.curated.txt','r')
for line in sa.readlines():
	x,r,y = line.strip().split('"')[1:4]
	if r == ' sameAs ':
		names[x] = y
sa.close()

po = open('rdf/partOf.txt','r')
cu = open('rdf/partOf.curated.raw','w')
for line in po.readlines():
	x,r,y = line.strip().split('"')[1:4]
	if y in names.keys():
		y = names[y]
	if r == ' partOf ':
		cu.write('"%s" partOf "%s"\n' % (x,y))
po.close()
cu.close()
