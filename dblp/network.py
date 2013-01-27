#! /usr/bin/env python
# this script computes the extended comminity size per year
import sys

buf = 1000000

names = {}
po = open('rdf/partOf.curated.txt','r')
for line in po.readlines():
	x,r,y = line.strip().split('"')[1:4]
	if r == ' partOf ' and y == "MoDELS":
		names[x] = []
po.close()

pa = open('rdf/publishedAt.txt','r')
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
	y = int(y[0:4])
	if y not in years:
		years[y] = []
	for name in names[n]:
		if name not in years[y]:
			years[y].append(name)

extyears = {}
for y in years.keys():
	extyears[y] = years[y][:]

cw = open('rdf/collabWith.txt','r')
tmplines = cw.readlines(buf)
while tmplines:
	for line in tmplines:
		x,r,y = line.strip().split('"')[1:4]
		if r == ' collaboratedWith ':
			for yr in years.keys():
				if x in years[yr]:
					if y not in extyears[yr]:
						extyears[yr].append(y)
	tmplines = cw.readlines(buf)
cw.close()

for y in sorted(years.keys()):
	print y,'   ',len(extyears[y])
