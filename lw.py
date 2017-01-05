ptext = open ("pride")
words = list()
for lines in ptext:
	words.extend(lines.split())

longest=""
leng = 0

for w in words:
	if len(w) > leng:
		longest=w
		leng =len(w)

print longest, leng 

nn = 0
for w in words:
	if w == "Bingley":
		nn+= 1
print nn
