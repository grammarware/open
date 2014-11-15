#!/usr/bin/python

import sys

cx = 27

# Sanity check: need a space in every address
f = open('shortlist.txt','r')
for x in f.readlines():
	if x.strip().find(' ')<0:
		print 'Suspicious entry:',x.strip()
f.close()

# Sanity check: varying number of fields in a generated record
# NB: only works if newadam.csv is already generated
f = open('newadam.csv','r')
for x in f.readlines():
	d = x.strip().split('\t')
	if len(d)!=cx:
		print 'Suspicious record:',x.strip()
		print len(d), 'tabs here'
f.close()

# Sanity check: varying number of fields in a record
# Convert the MIB entries to simple text in the same format shortlist supports
f = open('adam.csv','r')
g = open('miblist.txt','w')
for x in f.readlines():
	d = x.strip().split('\t')
	if len(d)!=cx:
		print 'Suspicious record:',x.strip()
		print len(d), 'tabs here'
	else:
		s = '%s %s' % (d[7],d[9])
		if d[10]!='\\N':
			s += ', '+d[10]
		g.write(s.strip()+'\n')
f.close()
g.close()

# Read the data once and for all
f = open('shortlist.txt','r')
g = open('miblist.txt','r')
sles = f.readlines()
mibes= g.readlines()
f.close()
g.close()

# Sanity check: alternatives (comma-separated) are mostly "street housenr"
for e in sles:
	alts = e.split(', ')
	for a in alts:
		if a.strip().find(' ')<0 and not a.strip().replace('-','').isdigit():
			print 'Suspicious alternative:',a.strip()

# Cross-check shortlist and miblist
incl = new = 0
kewl = []
for e in sles:
	alts = e.split(', ')
	# filter
	ralts = []
	for a in alts:
		if a.strip().replace('-','').isdigit():
			continue
		if a.find(' ')<0:
			continue
		ralts.append(a)
	match = False
	for a in ralts:
		if a in mibes:
			match = True
	if match:
		incl += 1
	else:
		new += 1
		kewl.append(e.strip())
print incl+new, 'entries processed:', incl, 'already known', new, 'new'

# Generate CSV for the database update
f = open('newadam.csv','w')
for e in kewl:
	alts = e.split(', ')
	if len(alts)==1:
		street = ' '.join(alts[0].split(' ')[:-1])
		nr1 = alts[0].split(' ')[-1]
		if nr1.find('-')<0:
			nr2 = '\\N'
		else:
			nr2 = nr1
			nr1 = nr1.split('-')[0]
	elif alts[1].strip().replace('-','').isdigit():
		street = ' '.join(alts[0].split(' ')[:-1])
		nr1 = alts[0].split(' ')[-1]
		if nr1.find('-')<0:
			nr2 = alts[1].strip()
		else:
			nr2 = nr1+', '+alts[1].strip()
			nr1 = nr1.split('-')[0]
	rec = []
	for i in range(0,27):
		if i == 7:
			rec.append(street)
		elif i == 9:
			rec.append(nr1)
		elif i == 10:
			rec.append(nr2)
		else:
			rec.append('\\N')
	f.write('\t'.join(rec)+'\n')
f.close()