import re
file = open ("pride")
words=[]  #define a list with nothing in it

for line in file:  #read a line from the file
	if re.search(r"\bdress", line):
		print line