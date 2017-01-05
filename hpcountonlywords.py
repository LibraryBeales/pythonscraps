import textmining

tempwords = open("lovecraftshort", "r")
lines = tempwords.read().split(" ")
print lines
print len(lines)
tempwords.close()