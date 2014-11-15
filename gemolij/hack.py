#!/usr/bin/python

import sys

# Make a [Street, Nr, Nrs, Toev] struct out of a string
def str2struct(s):
	alts = s.strip().split(', ')
	ralts = []
	# print 'Processing:',s.strip()
	for a in alts:
		if a.replace(',','').strip().isdigit():
			ralts[-1] += ', '+a
		elif a.strip().isalpha():
			continue
		else:
			ralts.append(a)
	if len(ralts)>1:
		return [s.strip(),'','','',ralts]
	ps = alts[0].strip().split(' ')
	# Keizersgracht 18-18A
	# Amstelveld 1-3, Kerkstraat 330
	# Korte Prinsengracht 41-89, 93, Haarlemmerstraat 141-179
	# Korte Dijkstraat 2, Krom Boomssloot
	head = []
	last = []
	middle = False
	for i in range(0,len(ps)):
		if not ps[i].replace('.','').replace('(','').replace(')','').isalpha():
			middle = True
		if middle:
			last.append(ps[i])
		else:
			head.append(ps[i])
	last = ' '.join(last)
	# print 'HEAD-LAST:',head,last
	if last.isdigit() or last=='':
		street = ' '.join(head)
		nr1 = last
		nr2 = toev = ''
	elif last.find('-')>-1:
		street = ' '.join(head)
		nr1 = last.split('-')[0]
		nr2 = last
		if nr1.isdigit():
			toev = ''
		else:
			for i in range(0,len(nr1)):
				if not nr1[i].isdigit():
					break
			toev = nr1[i:]
			nr1 = nr1[:i]
	else:
		street = ' '.join(head)
		nr1 = last
		nr2 = ''
		if nr1.isdigit():
			toev = ''
		else:
			for i in range(0,len(nr1)):
				if not nr1[i].isdigit():
					break
			toev = nr1[i:]
			nr1 = nr1[:i]
	return [street,nr1,nr2,toev,[]]

# rec = fetch(a,mipdb)
def fetch(name,db):
	print 'Fetching',a,'...',
	# print db[0]
	f = []
	for e in db:
		if e[7] == a[0] and e[9] == a[1]:
			# and e[10] == a[2] and e[11] == a[3]:
			f = e
			print 'YES MATCH'
			break
	if f == []:
		print 'NO MATCH'
	for i in range(0,len(f)):
		if f[i]=='':
			f[i] = '\\N'
	return f

cx = 27

# ['278419', '508', 'MIPobj508', '11307', 'Noord-Holland', 'Amsterdam', 'Amsterdam', 'Vondelstraat',
# '1054 GS', '114', '116-134', '\\N', '\\N', '\\N', 'Concertgebouwbuurt / Vondelpar', 'Woonhuizen',
# 'Eclecticisme', '\\N', '\\N', '\\N', '\\N', 'Circa 1880-1890', '\\N', '119978', '486099', '\\N',
# 'Bouwkunst; woonhuis']

sents = []
ments = []
# Sanity check: need a space in every address
f = open('shortlist.txt','r')
for x in f.readlines():
	if x.strip().find(' ')<0:
		print 'Suspicious entry:',x.strip()
	sents.append(str2struct(x))
f.close()

# Stats
withtoev = multip = 0
for e in sents:
	if e[3]!='':
		withtoev += 1
	# if e[0].find(', ')>-1 and e[1]+e[2]+e[3]=='':
	if e[4]!=[]:
		multip += 1
		ess = []
		for sub in e[4]:
			# print 'IN:',sub
			se = str2struct(sub)
			if se[3]!='':
				withtoev += 1
			ess.append(se)
		e[4] = ess
print 'With multiple addresses:',multip
print 'With addition:',withtoev

# Sanity check: varying number of fields in a generated record
# NB: only works if newadam.csv is already generated
# f = open('newadam.csv','r')
# for x in f.readlines():
# 	d = x.strip().split('\t')
# 	if len(d)!=cx:
# 		print 'Suspicious record:',x.strip()
# 		print len(d), 'tabs here'
# f.close()

# Sanity check: varying number of fields in a record
# Convert the MIP entries to simple text in the same format shortlist supports
f = open('adam.csv','r')
g = open('miplist.txt','w')
mipdb = []
for x in f.readlines():
	d = x.strip().split('\t')
	mipdb.append(d)
	if len(d)!=cx:
		print 'Suspicious record:',x.strip()
		print len(d), 'tabs here'
	else:
		street = d[7] if d[7]!='\\N' else ''
		nr1 = d[9] if d[9]!='\\N' else ''
		nr2 = d[10] if d[10]!='\\N' else ''
		toe = d[11] if d[11]!='\\N' else ''
		ments.append([street,nr1,nr2,toe,[]])
		s = '%s %s' % (d[7],d[9])
		if d[11]!='\\N':
			s += d[11]
		if d[10]!='\\N':
			s += ', '+d[10]
		g.write(s.strip()+'\n')
f.close()
g.close()

# Sarphatistraat 66-66a

# Read the data once and for all
f = open('shortlist.txt','r')
g = open('miplist.txt','r')
sles = f.readlines()
mipes= g.readlines()
f.close()
g.close()

# Sanity check: alternatives (comma-separated) are mostly "street housenr"
for e in sles:
	alts = e.split(', ')
	for a in alts:
		if a.strip().find(' ')<0 and not a.strip().replace('-','').isdigit() and not a.strip().isalpha():
			print 'Suspicious alternative:',a.strip()

f = open('mipentries.txt','w')
# ['Kerkstraat', '330', '\\N', '\\N', []]
for m in ments:
	f.write('%s\n' % m)
# for m in sents:
f.close()

g = open('shlentries.txt','w')
# Cross-check shortlist and miplist
# Algorithm variant #2
incl = new = 0
kewl = []
for e in sents:
	alts = [e[:]]
	if e[4]!=[]:
		alts[0][4] = []
		alts.extend(e[4])
	match = False
	g.write('%s\n=>\n' % e)
	for a in alts:
		g.write('\t%s\n' % a)
	for a in alts:
		if a in ments:
			match = True
			break
	if match:
		incl += 1
		# TODO: add matched entry
		rec = fetch(a,mipdb)
	else:
		new += 1
		rec = []
		for i in range(0,27):
			if i == 4:
				rec.append('Noord-Holland')
			elif i == 5 or i == 6:
				rec.append('Amsterdam')
			elif i == 7:
				rec.append(e[0] if e[0]!='' else '\\N')
			elif i == 9:
				rec.append(e[1] if e[1]!='' else '\\N')
			elif i == 10:
				rec.append(e[2] if e[2]!='' else '\\N')
			elif i == 11:
				rec.append(e[3] if e[3]!='' else '\\N')
			else:
				rec.append('\\N')
	kewl.append(rec)
g.close()

# for e in sles:
# 	alts = e.split(', ')
# 	# filter
# 	ralts = []
# 	for a in alts:
# 		if a.strip().replace('-','').isdigit():
# 			continue
# 		if a.find(' ')<0:
# 			continue
# 		ralts.append(a)
# 	match = False
# 	for a in ralts:
# 		if a in mipes:
# 			match = True
# 	if match:
# 		incl += 1
# 		print 'MATCH:',a,'FOR',e
# 	else:
# 		new += 1
# 		kewl.append(e.strip())
print incl+new, 'entries processed:', incl, 'already known', new, 'new'

# Generate CSV for the database update
f = open('newadam.csv','w')
for e in kewl:
	# alts = e.split(', ')
	# if len(alts)==1:
	# 	street = ' '.join(alts[0].split(' ')[:-1])
	# 	nr1 = alts[0].split(' ')[-1]
	# 	if nr1.find('-')<0:
	# 		nr2 = '\\N'
	# 	else:
	# 		nr2 = nr1
	# 		nr1 = nr1.split('-')[0]
	# elif alts[1].strip().replace('-','').isdigit():
	# 	street = ' '.join(alts[0].split(' ')[:-1])
	# 	nr1 = alts[0].split(' ')[-1]
	# 	if nr1.find('-')<0:
	# 		nr2 = alts[1].strip()
	# 	else:
	# 		nr2 = nr1+', '+alts[1].strip()
	# 		nr1 = nr1.split('-')[0]
	# rec = []
	# for i in range(0,27):
	# 	if i == 7:
	# 		rec.append(street)
	# 	elif i == 9:
	# 		rec.append(nr1)
	# 	elif i == 10:
	# 		rec.append(nr2)
	# 	else:
	# 		rec.append('\\N')
	# f.write('\t'.join(rec)+'\n')
	f.write('\t'.join(e)+'\n')
f.close()
