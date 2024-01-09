# REGULAR EXPRESSION
import re

hand = open('youtube/clown.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^Freom: ', line): # the '^' in front of 'From' is regex syntax saying if the line begins with 'From'
        print(line)
        
# #The above code is the same as this:
# hand = open('intro.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)


# Matching and Extracting Data 
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)         # the regex says find any digit btw 0-9, while the '+' says 1 or more of the digits that matches.
print(y)
# ['2', '19', '42']


# Fine-Tuning String Extraction
# parentheses are not part of the match = but they tell where to start and stop strin to extract
data = "Frome stephen.margquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('\S+@\S+', data)      # '\S' indicates non white space, '+' says one or more, followed by an '@' sign
print(y)
# ['stephen.margquard@uct.ac.za']


# extracting school domain without regex
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos) #look for where there is whitespace starting from where u have '@'
print(sppos)

host = data[atpos + 1: sppos] # starting from after '@' to but not including sppos
print(host)
# [uct.ac.za]

# USING REGEX
y = re.findall('@([^ ]*)', data)        # says, starting from '@', the '()' means extract only what is in the (), '^ ' means any xter but not what space, * means 0 or more times
print(y)    

# Being more precise, we can extract only from lines that starts with 'From ' by doing:
re. findall('^From .*@([^ ]*)', data) # starting from 'From' followed by space, then '.' means any number of xters, followed by '@'. The parenthasis after '@' means return only what is in the '()'


#FULL CODE
import re
hand = open('youtube/intro.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) !=1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
    