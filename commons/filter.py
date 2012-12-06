#!/usr/local/bin/python

import sys

f = open(sys.argv[1],'r')
j = open('commons-jpg.txt','w')
g = open('commons-gif.txt','w')
p = open('commons-png.txt','w')
buf = 100000
cx = 0
tmp_lines = f.readlines(buf)
while tmp_lines:
	for line in tmp_lines:
		cx += 1
		fn = ':'.join(line.split(':')[2:])
		ext = fn.split('.')[-1].lower().strip()
		if fn.startswith('File:'):
			if ext == 'jpg' or ext == 'jpeg':
				j.write('http://commons.wikimedia.org/wiki/'+fn)
			elif ext == 'png':
				p.write('http://commons.wikimedia.org/wiki/'+fn)
			elif ext == 'gif':
				g.write('http://commons.wikimedia.org/wiki/'+fn)
		# else:
		# 	print 'Unknown extension:',ext
	tmp_lines = f.readlines(buf)
	print 'Processed %i files...' % cx
f.close()
j.close()
g.close()
p.close()
