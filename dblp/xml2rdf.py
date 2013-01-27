#! /usr/bin/env python

import sys

crossrefs = []

def getit(n,s):
	#par.split('<author>')[1].split('</author>')[0])
	return n.split('<%s>' % s)[1].split('</%s>' % s)[0]

f = open('_everything.xml','r')
pa = open('rdf/publishedAt.raw','w')
cw = open('rdf/collabWith.raw','w')
po = open('rdf/partOf.raw','w')
buf = 1000000
cx = pcx = 0
tmp_lines = f.readlines(buf)
where = 0
# 0 - at the start
# 1 - inside <dblp>, outside any entry
# 2 - inside E
# 3 - at the end
while tmp_lines:
	for line in tmp_lines:
		if not line.strip():
			continue
		if where == 0:
			if line.strip() == '<dblp>':
				where = 1
			continue
		elif where == 1:
			if line.strip() == '</dblp>':
				where = 3
			tag = line.strip().split()[0][1:]
			cx += 1
			where = 2
			elines = []
			# need = line.strip().find('key="conf/'+sys.argv[1]+'/') > 0
		elif where == 2:
			if line.strip()[2:-1] == tag:
				if tag in ('www','proceedings'):
					# ignore web sources and editorial work
					where = 1
					continue
				# process elines
				authors = []
				cr = bt = j = ''
				for par in elines:
					# collect coauthors
					if par.find('<author>')>-1:
						authors.append(getit(par,'author'))
					# find out which conference we're at
					if par.find('<crossref>')>-1:
						cr = getit(par,'crossref')
						if cr not in crossrefs:
							crossrefs.append(cr)
					# find out the real conference name
					if par.find('<booktitle>')>-1:
						bt = getit(par,'booktitle')
					# if not a conference, get the journal name
					if par.find('<journal>')>-1:
						j = getit(par,'journal')
					# if par.find('<school>')>-1:
					# 	# special value for theses
					# 	j = 'PhD'
				if tag == 'book':
					j = 'monograph'
				if tag == 'phdthesis':
					# some theses do not have a school set
					j = 'PhD'
				if tag == 'mastersthesis':
					# some theses do not have a school set
					j = 'MSc'
				if len(authors)>1:
					for a1 in authors:
						for a2 in authors:
							cw.write('"%s" collaboratedWith "%s"\n' % (a1,a2))
				if cr:
					for a in authors:
						pa.write('"%s" publishedAt "%s"\n' % (a,cr))
					if bt:
						po.write('"%s" partOf "%s"\n' % (cr,bt))
					elif j:
						po.write('"%s" partOf "%s"\n' % (cr,j))
					else:
						print 'Warning: neither <booktitle> nor <journal> found for',cr
						po.write('"%s" partOf "%s"\n' % (cr,cr.split('/')[1]))
				elif j:
					# journals
					for a in authors:
						pa.write('"%s" publishedAt "%s"\n' % (a,j))
				elif bt:
					# only booktitle is available
					for a in authors:
						pa.write('"%s" publishedAt "%s"\n' % (a,bt))
				else:
					print 'Error: no information on the nature of the source is found!'
					print ''.join(elines)
				where = 1
				continue
			elines.append(line)
		else:
			print 'Skipped line "%s".' % line
			continue
	tmp_lines = f.readlines(buf)
	print 'Processed %i entries...' % cx
f.close()
pa.close()
cw.close()
po.close()
