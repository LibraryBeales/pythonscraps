import re

ff = open("/tmp/ath")

for line in ff:
	row = line.split("\t")

	if re.search ("State", row[0]):

		print row[0], row [1]