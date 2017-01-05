import re

f= open ("words")  #dictionary opens as a set.  This is just the Linux distribution English dictionary with some small edits to test different functions
stops = set()		#should probably use Moby dictionary or equivalent in the future
for line in f:
	stops.add(line.strip())

f = open ("azathoth") #Azathoth (1922)
azathoth = list() # lists allow duplicates!!
for line in f:
	azathoth.extend(re.findall("[A-z\-\']+", line.strip()))#Eliminates numbers but includes hyphenated words, which is relevant to Loveraft's unique entity and place names

azathothcount = list()
for w in azathoth:
	if w in stops:
		continue
	else:
		azathothcount.append(w)  #adds words that are not found in stops, !!Problems with capitlaization need to be sorted still
		
print azathothcount[1:10]

###
f = open ("cthulhu")  #The Call of the Cthulhu (1926)
cthulhu = list()
for line in f:
	cthulhu.extend(re.findall("[A-z\-\']+", line.strip()))

cthulhucount = list()   #Should create a function for this repeated code block.  
for w in cthulhu:
	if w in stops:
		continue
	else:
		cthulhucount.append(w)
		
print cthulhucount[1:10]

###

f = open ("beyondtwos") #Beyond the Wall of Sleep (1919)
beyondtwos = list()
for line in f:
	beyondtwos.extend(re.findall("[A-z\-\']+", line.strip()))

beyondtwoscount = list()
for w in beyondtwos:
	if w in stops:
		continue
	else:
		beyondtwoscount.append(w)
		
print beyondtwoscount[1:10]

###

f = open ("cdw")  #The Case of Charles Dexter Ward (1927)
cdw = list()
for line in f:
	cdw.extend(re.findall("[A-z\-\']+", line.strip()))

cdwcount = list()
for w in cdw:
	if w in stops:
		continue
	else:
		cdwcount.append(w)
		
print cdwcount[1:10]

###

f = open ("ulthar")  #The Cats of Ulthar (1920)
ulthar = list()
for line in f:
	ulthar.extend(re.findall("[A-z\-\']+", line.strip()))

ultharcount = list()
for w in ulthar:
	if w in stops:
		continue
	else:
		ultharcount.append(w)
		
print ultharcount[1:10]

###

f = open ("alchemist") #The Alchemist (1908)
alchemist = list()
for line in f:
	alchemist.extend(re.findall("[A-z\-\']+", line.strip()))

alchemistcount = list()
for w in alchemist:
	if w in stops:
		continue
	else:
		alchemistcount.append(w)
		
print alchemistcount[1:10]

###

f = open ("crawling")  ##The Crawling Chaos 1920/21
crawling = list()
for line in f:
	crawling.extend(re.findall("[A-z\-\']+", line.strip()))

crawlingcount = list()
for w in crawling:
	if w in stops:
		continue
	else:
		crawlingcount.append(w)
		
print crawlingcount[1:10]

###

f = open ("sarnath") ##The Doom That Came to Sarnath (1919)
sarnath = list()
for line in f:
	sarnath.extend(re.findall("[A-z\-\']+", line.strip()))

sarnathcount = list()
for w in sarnath:
	if w in stops:
		continue
	else:
		sarnathcount.append(w)
		
print sarnathcount[1:10]

###

f = open ("dunwich") ##The Dunwich Horror (1928)
dunwich = list()
for line in f:
	dunwich.extend(re.findall("[A-z\-\']+", line.strip()))

dunwichcount = list()
for w in dunwich:
	if w in stops:
		continue
	else:
		dunwichcount.append(w)
		
print dunwichcount[1:10]

###

f = open ("nyarlathotep") ##Nyarlathotep (1920)
nyarlathotep = list()
for line in f:
	nyarlathotep.extend(re.findall("[A-z\-\']+", line.strip()))

nyarlathotepcount = list()
for w in nyarlathotep:
	if w in stops:
		continue
	else:
		nyarlathotepcount.append(w)
		
print nyarlathotepcount[1:10]

###

f = open ("pickman") ##Pickman's Model 1926
pickman = list()
for line in f:
	pickman.extend(re.findall("[A-z\-\']+", line.strip()))

pickmancount = list()
for w in pickman:
	if w in stops:
		continue
	else:
		pickmancount.append(w)
		
print pickmancount[1:10]

###

f = open ("shadow") ##The Shadow Over Innsmouth (1931)
shadow = list()
for line in f:
	shadow.extend(re.findall("[A-z\-\']+", line.strip()))

shadowcount = list()
for w in shadow:
	if w in stops:
		continue
	else:
		shadowcount.append(w)
		
print shadowcount[1:10]

###

f = open ("thing") ##The Thing on the Doorsetp (1933)
thing = list()
for line in f:
	thing.extend(re.findall("[A-z\-\']+", line.strip()))

thingcount = list()
for w in thing:
	if w in stops:
		continue
	else:
		thingcount.append(w)
		
print thingcount[1:10]
raw_input('Press Enter...')
###Turn all the lists from above into strings to export as a file

azathothstr = ' '.join(azathothcount)
nyarlathotepstr = ' '.join(nyarlathotepcount)
cdwstr = ' '.join(cdwcount)
beyondtwosstr = ' '.join(beyondtwoscount)
sarnathstr = ' '.join(sarnathcount)
cthulhustr = ' '.join(cthulhucount)
dunwichstr = ' '.join(dunwichcount)
thingstr = ' '.join(thingcount)
shadowstr = ' '.join(shadowcount)
pickmanstr = ' '.join(pickmancount)
crawlingstr = ' '.join(crawlingcount)
ultharstr = ' '.join(ultharcount)
alchemiststr = ' '.join(alchemistcount)

allhp = (azathothstr, nyarlathotepstr, cdwstr, beyondtwosstr, sarnathstr, cthulhustr, dunwichstr, thingstr, shadowstr, pickmanstr, crawlingstr, ultharstr, alchemiststr)
allhpstr = ' '.join(allhp)
print allhpstr
raw_input('Press Enter...')

hp = open("hpwords.txt", "w")
hp.write(allhpstr)	
hp.close

## Everything below was textmining module code designed to create TDM.  Hyphens were being stripped, post up on stackoverflow, will return to investigate this method...

#print azathothstr
#raw_input('Press Enter...')
#print nyarlathotepstr
#raw_input('Press Enter...')


#import textmining

#def termdocumentmatrix_example():
    # Create some very short sample documents
#    doc1 = azathothstr
#    doc2 = cthulhustr
    #doc3 = (cdwcount)
    #doc4 = (beyondtwoscount)
    #doc5 = (sarnathcount)
    #doc6 = (nyarlathotepcount)
    #doc7 = (dunwichcount)
    #doc8 = (thingcount)
    #doc9 = (shadowcount)
    #doc10 = (pickmancount)
    #doc11 = (crawlingcount)
    #doc12 = (ultharcount)
    #doc13 = (alchemistcount)
    # Initialize class to create term-document matrix
#    tdm = textmining.TermDocumentMatrix()
    # Add the documents
#    tdm.add_doc(doc1)
#    tdm.add_doc(doc2)
    #tdm.add_doc(cdwcount)
    #tdm.add_doc(beyondtwoscount)
    #tdm.add_doc(sarnathcount)
    #tdm.add_doc(nyarlathotepcount)
    #tdm.add_doc(dunwichcount)
    #tdm.add_doc(thingcount)
    #tdm.add_doc(shadowcount)
    #tdm.add_doc(pickmancount)
    #tdm.add_doc(crawlingcount)
    #tdm.add_doc(ultharcount)
    #tdm.add_doc(alchemistcount)
    


    # Write out the matrix to a csv file. Note that setting cutoff=1 means
    # that words which appear in 1 or more documents will be included in
    # the output (i.e. every word will appear in the output). The default
    # for cutoff is 2, since we usually aren't interested in words which
    # appear in a single document. For this example we want to see all
    # words however, hence cutoff=1.
#    tdm.write_csv('matrixhp.csv', cutoff=1)
    # Instead of writing out the matrix you can also access its rows directly.
    # Let's print them to the screen.
#    for row in tdm.rows(cutoff=1):
#        print row
#raw_input('Press Enter...')
#termdocumentmatrix_example()
