import re, sys
import codecs
from pymarc import MARCReader

fh = open('umich_bib.marc', 'rb')
reader = MARCReader(fh)
names=dict()
booklist=dict()
nbooks = 0
z = 0

for record in reader:
	title = record.title().encode('ascii', 'ignore')
	try:
		author = record.author().encode('ascii', 'ignore')
	except:
		print "bad author", record.author()
	for line in file:  #read a line from the file
		if re.search(r"\bDiana", author):
			print author, "::", title
		if z>10:
			exit()
	z+=1