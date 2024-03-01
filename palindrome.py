# # Palindromes are words that are the same when read forward and backward.

# text = input("Enter your text: ")

# text = text.replace(" ", "")
# text2 = text[::-1]
# text = text.lower()
# text2 = text2.lower()
        
# if len(text) > 1 and all(elem.lower() == elem2.lower() for elem, elem2 in zip(text, text2)) :
#     print("It's a palindrome")
# else:
#     print("Not a palindrome")

# Python sum function using the 'reduce' function
from functools import reduce

numbers= [3, 4, 6, 9, 34, 12]
result = reduce(lambda x, y: x + y, numbers, 10)
print(result)

from functools import reduce 

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
        
result = list(map(round, [x**2 for x in my_floats], [3] * len(my_floats)))
print(result)

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

filtered = list(filter(lambda x: len(x) <= 7, my_names))
print(filtered)

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
red = reduce(lambda x, y: x * y, my_numbers)
print(red)