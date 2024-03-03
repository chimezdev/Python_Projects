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
    

# # Writing a byte array to a binary file
# data = bytearray(10)
# for dat in range(len(data)):
#     data[dat] = 10 + dat

# try:
#     bytefile = open('file.bin', 'wb')
#     bytefile.write(data)
#     bytefile.close()
# except IOError as e:
#     print("I/O error occured:", strerror(e.errno))


# # Reading binary file using 'readinto()' method
# # data = bytearray(10)
# try:
#     binary_file = open('file.bin', 'rb')
#    # binary_file.readinto(data)      
#     data = bytearray(binary_file.read(5)) #if used, 'data = bytearray(10)' is needed
#     binary_file.close()

#     for b in data:
#         print(hex(b), end=' ')
# except IOError as e:
#     print("I/O error occured:", strerror(e.errno))



# COPYING FILE
from os import strerror

srcname = input("Enter the source file: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

print(total,'byte(s) succesfully written')
src.close()
dst.close()