# count lines, sentences, and words of a text file
# set counters to zero
lines, blanklines, sentences, words = 0, 0, 0, 0
print '-' * 50
try:
  
  filename = 'lovecraft'
  textf = open(filename, 'r')  # r=read
except IOError:
  print 'Cannot open file %s for reading' % filename #error checking
  import sys
  sys.exit(0)
# reads one line at a time
for line in textf:  #line
  print line,   # for testing  - line count wrong due to carriage return format - several character formats need to be fixed
  lines += 1
  
  if line.startswith('\n'):
    blanklines += 1
  else:
    # Only works if each sentence ends with . or ! or ? so just counting these characters abbreviations?
    sentences += line.count('.') + line.count('!') + line.count('?')
    
    # create a list of words
    # use None to split at any whitespace (double space counts as one space)
    tempwords = line.split(None)
    print tempwords  # for testing
    
    # total count
    words += len(tempwords)
    
textf.close()
print '-' * 50
print "Lines      : ", lines
print "Blank lines: ", blanklines
print "Sentences  : ", sentences
print "Words      : ", words


#need sanitized file - work on getting finereader access, or reformatting this file.
## optional console wait for keypress
raw_input('Press Enter...')