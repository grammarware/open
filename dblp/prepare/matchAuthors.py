#! /usr/bin/env python
import sys

# reverse author-of
rao = {}

ao = open('../cache/authorOf.rdf','r')
for line in ao.readlines():
	c = line.split('"')
	if c[3] not in rao.keys():
		rao[c[3]] = []
	rao[c[3]].append(c[1])
ao.close()

print 'AuthorOf read!'

ps = open('pi.all','r')
ass = open('ai.all','w')
for line in ps.readlines():
	paper = line.strip()
	if paper in rao.keys():
		for a in rao[paper]:
			ass.write('%s\n' % a)
	else:
		print 'Unknown paper:',paper
ps.close()
ass.close()
