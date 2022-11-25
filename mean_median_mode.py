# Mean, median, and Mode are important statistical tools used daily while dealing
# with values. Programs to calculate the mean, median, and mode of a set of values 
# provided by user

# MEAN 
# The mean is the average value of all the values in a dataset.

values = []
user_input = 0
while True:
    try:
        user_input =  int(input("The 'mean' of how many numbers do you want to find? "))
        break
    except ValueError:
        print("Only natural integers values are allowed")
number = float(input("Enter a value: "))
values.append(number)

while len(values) < user_input:
    number = float(input("Enter a value: "))
    values.append(number)
sum = 0
if len(values) == user_input:
    for i in values:
        sum += i
mean = sum / user_input

# The Median is the middle value among all the values in sorted order.
values.sort()
if user_input % 2 == 0: # if no of values is an even number
    median = values[len(values) // 2] + values[(len(values) // 2) - 1] # add the 2 middle values and divide by 2
    median = median / 2
else:
    median = values[len(values) // 2]

# Mode is the most frequently occurring value among all the values.    
mode = 0
counters = {i : 0 for i in values} #generate a dictionary of elems of 'values' with their freq as values
for i in values:
    counters[i] += 1
    mode = max(mode, counters[i]) #get the max value
mode = [i for i in counters if counters[i] == mode] #get the dict key with the max value
    
print("The mean of the numbers is: ", mean)
print("The median of the values is: ", median)
print("The mode of the values is: ", mode)
    
# Instructor's code for mode
# Mode
# list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
# frequency = {}
# for i in list1:
#     frequency.setdefault(i, 0)
#     frequency[i]+=1

# frequent = max(frequency.values())
# for i, j in frequency.items():
#     if j == frequent:
#         mode = i
# print(mode)