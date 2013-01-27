#! /usr/bin/env python
# this script goes over partOf and outputs unsorted raw sameAs relations for everything beside books
import sys

crossrefs = []

po = open('rdf/partOf.txt','r')
sa = open('rdf/sameAs.raw','w')
for line in po.readlines():
	x,r,y = line.strip().split('"')[1:4]
	if r == ' partOf ':
		c = x.split('/')
		if c[0] != 'books' and y.upper()!=c[1].upper():
			sa.write('"%s" sameAs "%s"\n' % (y,c[1]))
po.close()
sa.close()
