import sys
words = sys.argv [1:]

longest=""
leng = 0

for w in words:
	if len(w) > leng:
		longest=w
		leng =len(w)

print longest, leng 


