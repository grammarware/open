#! /usr/bin/env python
# this script computes the comminity changes with years: how many people come again the year after?
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

allys = sorted(years.keys())
for y in allys:
	print y,':'
	this = years[y]
	for i in range(allys.index(y)+1,len(allys)):
		prev = this
		this = []
		if prev == this:
			break
		# len(years[y]) people contributed in year y
		# how many still contributed in year allys[i]?
		for person in prev:
			if person in years[allys[i]]:
				this.append(this)
		print 'Left in',allys[i],':',len(this)
	print
