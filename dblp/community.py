#! /usr/bin/env python
# this script computes the comminity size per year
import sys

names = {}

po = open('rdf/partOf.curated.txt','r')
for line in po.readlines():
	x,r,y = line.strip().split('"')[1:4]
	if r == ' partOf ' and y == "MoDELS":
		names[x] = []
po.close()

pa = open('rdf/publishedAt.txt','r')
buf = 1000000
tmplines = pa.readlines(buf)
while tmplines:
	for line in tmplines:
		x,r,y = line.strip().split('"')[1:4]
		if r == ' publishedAt ':
			if y in names.keys():
				if x not in names[y]:
					names[y].append(x)
	tmplines = pa.readlines(buf)
pa.close()

years = {}
for n in names.keys():
	y = n.replace('/','').replace('-','')
	for x in range(ord('a'),ord('z')+1):
		y = y.replace(chr(x),'')
	y = y[0:4]
	if y not in years:
		years[y] = []
	for name in names[n]:
		if name not in years[y]:
			years[y].append(name)

for y in sorted(years.keys()):
	print y,'   ',len(years[y])
