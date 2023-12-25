# READING FILES
# read = open(filename, mode)

# fhand = open('text.txt', 'r')
# lines = fhand.read()
# print(len(fhand))

# #finding lines that starts with a particular word
# for line in fhand:
#     line = line.rstrip()
#     if not line.startwith('From:'):
#         continue
#     print(line)
    
# #find the lines that contain a particular word
# for line in fhand:
#     line = line.rstrip()
#     if not '@gmail.com' in line:
#         continue
#     print(line)
    
    
# #use insurance incase of a bad file name:
# fname = input('Enter the file name: ')

# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     quit()

# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count+1
# print('There were', count, 'subject lines in', fname)


# # PYTHON DICTIONARY
# count = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     if name not in count:
#         count[name] = 1
#     else:
#         count[name] = count[name] + 1
# print(count)

# # cleaner version
# for name in names:
#     count[name] = count.get(name, 0) + 1
# print(count)


# # Retrieving lists of keys and values
# data = {'chuck' : 1, 'fred' : 42, 'jan': 1000}
# print(list(data)) # returns ['jan', 'chuck', 'fred']
# print(data.keys()) # returns ['jan'm 'chuck', 'fred']
# print(data.values()) #returns [100, 1, 42]
# print(data.items()) # returns [('jan', 100), ('chuck', 1), ('fred', 42)]

# # The items method gives us opportunity to do something only seen with python
# for key, value in data.items():
#     print(key, value)
    
    
# # Find the largest in a dictionary
# name = input('Enter file name: ')
# file = open(name)

# counts = dict()
# for line in file:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
        
# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword, bigcount)


# WORKING WITH DICTIONARY
fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # if w in di:
        #     di[w] = di[w] + 1
        # else:
        #     di[w] = 1
        #     print('**NEW**')
        # print(w, di[w])
        
        # using the power of dict
        di[w] = di.get(w, 0) + 1   # idiom: retrieve/create/update counter
        
print(di)

#Finding the most common word
most_word = None
most_value = None
for key, val in di.items():
    if most_word is None or val > most_value:
        most_word = key
        most_value = val

print(most_word, most_value)