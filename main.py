__author__ = 'a0866713'

from collections import defaultdict
import re
import random
#Initailzie a blank dictionary

rel = defaultdict()
#Open base file to build dictionary
file = open('pg11.txt', 'r')
for line in file:
    words = line.split()
    #-------------------------------------------------------------
    # Clean up the input so we have a good base of words to choose
    # from
    for x in range(0, len(words)):
        #words[x] = re.sub("[^0-9a-zA-Z]", "", words[x]).lower()
        words[x].lower()
    #-------------------------------------------------------------

    #-------------------------------------------------------
    #Loop through the words and add them to your dictionary
    for x in range(0, len(words)-1):
        if words[x] in rel:
            #print(x, " ", words[x], ' exists in the dict')
            if not(words[x+1] in rel[words[x]]):
                rel[words[x]].append(words[x+1])
        else:
            rel[words[x]] = [words[x+1]]
    #-------------------------------------------------------
file.close()
#------------------------------------------------------
#Loop through dictionary and build a sentence until you
#hit a period.
output_str = ""
flag = 0
while True:
    key = random.choice(rel.keys())
    if flag == 0 and str(key).isupper() and not str(key).endswith('.'):
        flag = 1
        output_str = str(key) + " "
    elif flag == 1 and str(key).endswith('.'):
        output_str = output_str + str(key) + " "
        break
    elif flag == 1:
            output_str = output_str + (random.choice(rel[key])) + " "

print(output_str)


