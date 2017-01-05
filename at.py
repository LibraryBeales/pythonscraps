ff = open("ath")

biggest=""
amt=0
for line in ff:
	row = line.split("\t")
	if int(row[3]) > amt:
		biggest=row[0]
		amt = int(row[3])
		print "new biggest", biggest, "with amount", amt