#! /usr/bin/env python
# this script goes over sameAs and curates it
import sys

crossrefs = []

def getit(n,s):
	return n.split('<%s>' % s)[1].split('</%s>' % s)[0]

def minstart(xs):
	s = ''
	for i in range(0,min(map(len,xs))):
		if map(lambda x:x[i],xs)==[xs[0][i]]*len(xs):
			s += xs[0][i]
		else:
			break
	s = s.strip()
	if s and s[-1] in ('(','-',':'):
		s = s[:-1].strip()
	return s

def allhave(xs,y):
	return reduce(lambda a,b:a and b.find(y)>-1, xs, True)

names = {}

sa = open('rdf/sameAs.txt','r')
for line in sa.readlines():
	x,r,y = line.strip().split('"')[1:4]
	if r == ' sameAs ':
		if y in names.keys():
			names[y].append(x)
		else:
			names[y] = [x]
sa.close()

cu = open('rdf/sameAs2.txt','w')
# hm = {}
for k in names.keys():
	# sz = len(names[k])
	# if sz not in hm.keys():
	# 	hm[sz] = 1
	# else:
	# 	hm[sz] += 1
	print '\nDealing with',k,'=',names[k]
	if len(names[k]) == 1:
		i = names[k][0].upper().find(k.upper())
		if i>-1:
			# print 'May I suggest',names[k][0][i:i+len(k)],'?'
			cu.write('"%s" sameAs "%s"\n' % (names[k][0],names[k][0][i:i+len(k)]))
			print 'Decision:',names[k][0][i:i+len(k)]
		else:
			# otherwise no good suggestion
			cu.write('"%s" sameAs "%s"\n' % (names[k][0],k.upper()))
			print 'Decision:',k.upper()
	else:
		if allhave(names[k],k.upper()):
			m = k.upper()
		else:
			m = minstart(names[k])
		if len(m)<2:
			m = k.upper()
		print 'Decision:',m
		for n in names[k]:
			if n != m:
				cu.write('"%s" sameAs "%s"\n' % (n,m))
cu.close()
	
