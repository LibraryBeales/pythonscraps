import re

f= open ("words")
stops = set()
for line in f:
	stops.add(line.strip())

f = open ("mountains")
mountains = list()
for line in f:
	mountains.extend(re.findall("[A-z\-\']+", line.strip()))#Eliminates numbers but includes hyphenated words, which is relevant to Loveraft's unique entity and place names

wcount = dict()
for w in mountains:
	if w in stops:
		continue
	if w in wcount:
		wcount[w]+=1
	else:
		wcount[w]=1

g = open ("sarnath")
sarnath = list()
for line in g:
	sarnath.extend(re.findall("[A-z\-\']+", line.strip()))

wcount2 = dict()
for w in sarnath:
	if w in stops:
		continue
	if w in wcount2:
		wcount2[w]+=1
	else:
		wcount2[w]=1


#wlist = sorted(wcount, key=wcount.get, reverse=True)
#for i in wlist[0:10]:
#	print i, wcount[ i ]

#wlist2 = sorted(wcount2, key=wcount2.get, reverse=True)
#for i in wlist2[0:10]:
#	print i, wcount2[ i ]

print wcount2


import textmining

def termdocumentmatrix_example():
    # import some sample documents
    #doc1 = open('lovecraftshort.txt', 'r')
   # doc2 = open('lovecraftshort2.txt', 'r')
    #doc3 = open('lovecraftshort3', 'r')
    

    
    doc1 = sarnath
    doc2 = mountains


    # Initialize class to create term-document matrix
    tdm = textmining.TermDocumentMatrix()
    
    # Add the documents
    tdm.add_doc(doc1)
    tdm.add_doc(doc2)
    
    # Write out the matrix to a csv file. Note that setting cutoff=1 means
    # that words which appear in 1 or more documents will be included in
    # the output (i.e. every word will appear in the output). The default
    # for cutoff is 2, since we usually aren't interested in words which
    # appear in a single document. For this example we want to see all
    # words however, hence cutoff=1.

    tdm.write_csv('hpmatrix.csv', cutoff=1)
    
    # Instead of writing out the matrix you can also access its rows directly.
    # Let's print them to the screen.
    
    for row in tdm.rows(cutoff=1):
        print row

termdocumentmatrix_example()