#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
# from conflib import exists, implode, explode

def datelower(d1_,m1_,y1_,d2_,m2_,y2_):
	[d1,m1,y1,d2,m2,y2] = map(int,[d1_,m1_,y1_,d2_,m2_,y2_])
	# print 'datelower:',[d1,m1,y1,d2,m2,y2]
	# d1/m1/y1 - current
	# d2/m2/y2 - to-insert
	if y1 == y2:
		if m1 == m2:
			if d2 > d1:
				return False
			else:
				# print d2,'/',m2,'before',d1,'/',m1
				return True
		elif m2 < m1:
			# print d2,'/',m2,'before',d1,'/',m1
			return True
		else:
			return False
	else:
		print 'Happy new year!!!'
		return False

def cmt2str1(cmt):
	return cmt2str(cmt)+'</entry>\n<entry>'

def cmt2str2(cmt):
	return '<entry>'+cmt2str(cmt)+'</entry>\n'

def cmt2str(cmt):
	# ['432c4d0651dd9c9e50cc163b26e5014f2b6b946c', '7', '17', '2012', ['one-slide-DSL']]
	# <entry>
	# 	<ts d="10" m="7"/>
	# 	<text>Proper naming; legacy files will be removed later</text>
	# 	<commit hub="6aa5d57f585cc75c21e893e7fd4d6dce6e0a7c46">SLPS</commit>
	# </entry>
	s = '\n<ts d="'+cmt[2]+'" m="'+cmt[1]+'" y="'+cmt[3]+'"/>'
	for t in cmt[4]:
		s += '<text>%s</text>' % t.replace('&','&amp;')
	if sys.argv[4] in ('Personal','Work','AcceptWare'):
		# big bucket
		s += '<commit bit="%s">%s</commit>' % (cmt[0],sys.argv[4])
	else:
		# git hub
		s += '<commit hub="%s">%s</commit>' % (cmt[0],sys.argv[4])
	return s

if __name__ == '__main__':
	if len(sys.argv) < 5:
		print 'Migrate what?'
		sys.exit(-1)
	commits = []
	f = open(sys.argv[2],'r')
	blob = f.read()
	cf = open(sys.argv[1],'r')
	for l in cf.readlines():
		cmt = eval(l)
		if blob.find(cmt[0]) > -1:
			break
		commits.append(cmt)
		# print 'Yes to',cmt
	cf.close()
	cx = 0
	g = open(sys.argv[3],'w')
	for l in blob.split('\n'):
		line = l.strip()
		# <ts d="3" m="1" y="2012"/>
		if line.startswith('<ts d="'):
			d = line.split('"')[1]
			m = line.split('"')[3]
			if len(line.split('"'))>5:
				y = line.split('"')[5]
			else:
				y = '2012'
			while len(commits)>0 and datelower(d,m,y,commits[-1][2],commits[-1][1],commits[-1][3]):
				g.write(cmt2str1(commits.pop()))
				cx += 1
		elif line=='</web:notebook>':
			while len(commits)>0:
				g.write(cmt2str2(commits.pop()))
				cx += 1
		g.write( line+'\n' )
	f.close()
	g.close()
	print 'Done with %s, %i entries weaved in.' % (sys.argv[4], cx)
	sys.exit(0)
