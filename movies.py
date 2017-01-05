
f = open ("/tmp/movies")
ratings = dict()
amt=100
for line in f:
	row = line.split("\t")
	if int(row[1]) > amt:
		#print row[2:4]
		name = row[3]
		ratings[name] = float(row[2])
ls = sorted (ratings, key=ratings.get, reverse=False)

for i in range (0,10):
	print ls[i], ratings[ls[i]]

#print ls[0:9]