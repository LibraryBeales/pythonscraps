import re

f = open ("words") #
f = [item.lower() for item in f]
stops = set()
for line in f:
	stops.add(line.strip())

f = open ("lovecraft") #Opens the lovecraft text file
f = [item.lower() for item in f] #Converts all the text to lowercase, case matters for comparison to dictionary
words = list()
for line in f:
	words.extend(re.findall("[A-z\-\']+", line.strip()))#Eliminates numbers but includes hyphenated words, which is relevant to Loveraft's unique entity and place names


wcount = list()
for w in words:
	if w in stops:
		continue
	else:
		wcount.append(w)
		
print (wcount[1:100])


