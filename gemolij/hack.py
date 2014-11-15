#!/usr/bin/python

import sys

# Sanity check: need a space in every address
f = open('shortlist.txt','r')
for x in f.readlines():
	if x.strip().find(' ')<0:
		print 'Suspicious:',x.strip()
f.close()

# Sanity check: varying number of fields in a record
# Convert the MIB entries to simple text in the same format shortlist supports
f = open('adam.csv','r')
g = open('miblist.txt','w')
cx = 27
for x in f.readlines():
	d = x.strip().split('\t')
	if len(d)!=cx:
		print 'Suspicious:',x.strip()
		print len(d), 'tabs here'
	else:
		s = '%s %s' % (d[7],d[9])
		if d[10]!='\\N':
			s += ' '+d[10]
		g.write(s.strip()+'\n')
f.close()
g.close()

# Cross-check shortlist and miblist
f = open('shortlist.txt','r')
g = open('miblist.txt','r')
sles = f.readlines()
mibes= g.readlines()
incl = new = 0
for e in sles:
	if e in mibes:
		incl += 1
	else:
		new += 1
print incl+new, 'entries processed:', incl, 'already known', new, 'new'
f.close()
g.close()
