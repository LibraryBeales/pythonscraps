import re
def wordsinline(line):
        return len(re.findall("\w+", line))  

while (True):
        try:
                s = raw_input("type something: ")
                print wordsinline(s)
        except:
                print "you finished"
                quit()