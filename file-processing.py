# # Processing file in Python
from os import strerror
import sys

# try:
#     cha_counter = line_counter = 0
#     stream = open('text.txt', 'rt')
#     line = stream.readline()
#     while line != '':
#         line_counter += 1
#         for char in line:
#             print(char, end='')
#             cha_counter += 1
#         line = stream.readline()
#     stream.close()
#     print("\n\nCharacters in file:", cha_counter)
#     print("Lines in file:     ", line_counter)
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))


# Opening a stream object in write mode and using the 'write()' method

# try:
#     file = open("newtext.txt", "wt")
#     for i in range(1, 11):
#         s = "line #" + str(i) + "\n"
#         for char in s:
#             file.write(char)
#         #or
#         # file.write(s) to write by line instead of character
#     file.close()
# except IOError as e:
#     sys.stderr.write("I/O %d error occured" %(strerror(e.errno)))
#     print("I/O error occured: ", strerror(e.errno))



# For handling amorphous data such as a bitmap image, python provides containers 
# such as "bytearray". An array containing (amorphous) bytes.

# # bytearrays are just like lists
# data = bytearray(10) #creates a bytearray obj able 2 store 10 bytes and initially fills the whole array with zeros
# for i in range(len(data)):
#     data[i] = 10 - i

# for b in data:
#     print(hex(b))
    

# Writing a byte array to a binary file
data = bytearray(10)
for dat in range(len(data)):
    data[dat] = 10 + dat

try:
    bytefile = open('file.bin', 'wb')
    bytefile.write(data)
    bytefile.close()
except IOError as e:
    print("I/O error occured:", strerror(e.errno))
