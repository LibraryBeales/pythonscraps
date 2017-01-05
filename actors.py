
f = open ("actors.tsv")
names = set()
years = dict()
last = raw_input ("Gimme a name, a last name.")
for line in f:
	row = line.split("\t")
	if str(row[1]) == last:
		names.add(row[0])
		names.add(row[4])

print names
