import re

ff = open("lovecraft")
words=[]

for line in ff:
	words.extend(re.findall(r"\bcat[-\w]+", line))

print words