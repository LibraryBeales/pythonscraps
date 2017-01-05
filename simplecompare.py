with open("wordshort") as f1,open("lovecraftshort") as f2:
    words=set(line.strip() for line in f1)   #create a set of words from dictionary file

    #why sets? sets provide an O(1) lookup, so overall complexity is O(N)

    #now loop over each line of other file (word, freq file)
    for line in f2:
        word,freq=line.split()   #fetch word,freq 
        if word in words:        #if word is found in words set then print it
            print word