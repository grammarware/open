#! /usr/bin/env python
# this script goes over partOf and curates it according to sameAs
import sys

venues = []
rel = sys.argv[1]
if len(sys.argv)>2:
	print 'Using','rdf/%s.really.curated.txt' % rel
	sa = open('rdf/%s.really.curated.txt' % rel,'r')
else:
	print 'Using','rdf/%s.curated.txt' % rel
	sa = open('rdf/%s.curated.txt' % rel,'r')
buf = 1000000
tmplines = sa.readlines(buf)
while tmplines:
	for line in tmplines:
		x,r,y = line.strip().split('"')[1:4]
		if r == (' %s ' % rel):
			z = x
			if z not in venues:
				venues.append(z)
	tmplines = sa.readlines(buf)
sa.close()

print len(venues)
