#1st store the start time of a program in a variable
import time

start = time.time() #creates a timestamp obj from the time the program starts
print(start)
#program that should be executed
# python program to create acronyms
word = "Artificial Intelligence"
text = word.split() #converts the string into a list of 2 elems

a = " " #assign spacebar xter to a variable
for i in text:
    a = a+str(i[0]).upper() # take the first char of each word in list text 
    
print(a)

# get the program end time
end = time.time()
print(end)
# calc program exec time
execution_time = end - start
print("Execution Time : ", round(execution_time, 9))#round to 9dp
