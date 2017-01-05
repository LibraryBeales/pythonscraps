import re

f= open ("words")
f = [item.lower() for item in f] #Converts all the text to lowercase, case matters for comparison to dictionary
stops = set()
for line in f:
	stops.add(line.strip())

f = open ("lovecraft")
f = [item.lower() for item in f] #Converts all the text to lowercase, case matters for comparison to dictionary
words = list()
for line in f:
	words.extend(re.findall("[A-z\-\']+", line.strip()))#Eliminates numbers but includes hyphenated and contracted words, which is relevant to Loveraft's unique diction, entity and place names

wcount = dict()
for w in words:
	if w in stops:
		continue
	if w in wcount:
		wcount[w]+=1
	else:
		wcount[w]=1

wlist = sorted(wcount, key=wcount.get, reverse=True)
for i in wlist[0:100]:
	print (i, wcount[ i ])


import csv

my_dict = (wcount)

with open('hpcsvfile.csv', 'w') as f:  # Will have to use 'w' mode in 3.x
    w = csv.DictWriter(f, my_dict.keys())
    w.writeheader()
    w.writerow(my_dict)