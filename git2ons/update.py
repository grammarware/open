#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
# from conflib import exists, implode, explode

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

def datelower(d1_,m1_,y1_,t1,d2_,m2_,y2_,t2):
	[d1,m1,y1,d2,m2,y2] = map(int,[d1_,m1_,y1_,d2_,m2_,y2_])
	# print 'datelower:',[d1,m1,y1,d2,m2,y2]
	# d1/m1/y1 - current
	# d2/m2/y2 - to-insert
	if y1 == y2:
		if m1 == m2:
			if d2 > d1:
				return False
			elif d1 == d2:
				if t1 and t2:
					return t1 > t2
				else:
					return True
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

def cmt2str1(cmt,name):
	return cmt2str(cmt,name)+'</entry>\n<entry>'

def cmt2str2(cmt,name):
	return '<entry>'+cmt2str(cmt,name)+'</entry>\n'

def cmt2str(cmt,name):
	# ['432c4d0651dd9c9e50cc163b26e5014f2b6b946c', '7', '17', '2012', '17:24:21', ['one-slide-DSL']]
	# <entry>
	# 	<ts d="10" m="7"/>
	# 	<text>Proper naming; legacy files will be removed later</text>
	# 	<commit hub="6aa5d57f585cc75c21e893e7fd4d6dce6e0a7c46">SLPS</commit>
	# </entry>
	s = '\n<ts d="%s" m="%s" y="%s" time="%s"/>' % (cmt[2], cmt[1], cmt[3], cmt[4])
	for t in cmt[5]:
		s += '<text>%s</text>' % t.replace('&','&amp;')
	if name in ('Personal','Work','AcceptWare'):
		# big bucket
		s += '<commit bit="%s">%s</commit>' % (cmt[0],name)
	else:
		# git hub
		s += '<commit hub="%s">%s</commit>' % (cmt[0],name)
	return s

def log2commits(fn):
	commits = []
	print fn
	fh = open(fn,'r')
	commit = ['','','','','',[]]
	lines = fh.readlines()
	cx = 0
	while cx < len(lines):
		if lines[cx].startswith('commit '):
			# TODO: parametrise with owner's emails
			if lines[cx+1].find('spider.vz@gmail.com') < 0 and lines[cx+1].find('vadim@grammarware.net') < 0:
				cx += 1
				while cx < len(lines) and not lines[cx].startswith('commit'): cx += 1
			else:
				commit[0] = lines[cx].split()[1]	# commit
				bys = lines[cx+2].split()
				commit[1] = str(1+months.index(bys[2]))	# month
				commit[2] = bys[3]	# day
				commit[3] = bys[5]	# year
				commit[4] = bys[4]  # time
				cx += 4
				commit[5] = []
				while cx < len(lines) and not lines[cx].startswith('commit'):
					if lines[cx].strip():
						commit[5].extend(lines[cx].strip().split('; '))
					cx += 1
				commit[5] = map(lambda x:x.startswith('* ') and x[2:] or x,commit[5])
				commits.append(commit[:])
		else:
			print lines[cx]
			cx += 1
	f.close()
	# print commits
	return commits

repos = {}

if __name__ == '__main__':
	f = open('repos.lst','r')
	for line in f.readlines():
		a,b = line.strip().split(' = ')
		repos[a] = b
	f.close()
	print repos
	f = open('2013.xml','r')
	blob = f.read()
	f.close()
	for r in repos.keys():
		onlines = map(lambda x:x.strip(),blob.split('\n'))
		# print 'cd %s/ && git log > tmp.log' % r
		os.system('cd %s/ && git log > tmp.log' % r)
		commits = []
		for cmt in log2commits('%s/tmp.log' % r):
			if cmt[3] != '2013':
				continue
			if blob.find(cmt[0]) > -1:
				break
			commits.append(cmt)
			print cmt
		os.system('rm %s/tmp.log' % r)
		cx = 0
		blob = ''
		for l in onlines:
			line = l.strip()
			# <ts d="3" m="1" y="2012" time="17:11:48"/>
			if line.startswith('<ts d="'):
				byq = line.split('"')
				d = byq[1]
				m = byq[3]
				y = byq[5]
				if len(byq)>7:
					time = byq[7]
				else:
					time = ''
				while len(commits)>0 and datelower(d,m,y,time,commits[-1][2],commits[-1][1],commits[-1][3],commits[-1][4]):
					blob += cmt2str1(commits.pop(),repos[r])
					cx += 1
			elif line=='</web:notebook>':
				while len(commits)>0:
					blob += cmt2str2(commits.pop(),repos[r])
					cx += 1
			blob += line+'\n' 
		print 'Done with %s, %i entries weaved in.' % (repos[r], cx)
	g = open('new.xml','w')
	g.write(blob)
	g.close()
	sys.exit(1)
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
