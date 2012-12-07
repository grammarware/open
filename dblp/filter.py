#! /usr/bin/env python

import sys

f = open('_everything.xml','r')
r = open(sys.argv[1]+'.xml','w')
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
			r.write(line)
			if line.strip() == '<dblp>':
				where = 1
			continue
		elif where == 1:
			if line.strip() == '</dblp>':
				r.write(line)
				where = 3
			E = line.strip().split()[0][1:]
			cx += 1
			where = 2
			elines = [line]
			need = line.strip().find('key="conf/'+sys.argv[1]+'/') > 0
		elif where == 2:
			elines.append(line)
			if line.strip()[2:-1] == E:
				if need:
					for x in elines:
						r.write(x)
					pcx += 1
				where = 1
		else:
			print 'Skipped:',line
			continue
	tmp_lines = f.readlines(buf)
	print 'Extracted %i out of %i processed entries...' % (pcx,cx)
f.close()
r.close()
