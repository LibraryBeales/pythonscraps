ptext = open ("pride")
words = list()
for lines in ptext:
	words.extend(lines.split())
print words[0], words[1], "second word", words[2]
print "total length", len(words)
