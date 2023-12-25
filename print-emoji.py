# To print emojis in python, install the emoji module using pip(usually better in a virtual env)
#run 'pip install emoji'
# use the 'emoji.emojize' mthd and write the description of any emoji inside ::
# 1. :thumbs_up:
# 2. :red_heart:
# 3. :smiling_face:

# import emoji

# print(emoji.emojize("I love reading books :books:"))
# print(emoji.emojize("Some people have a very sensitive heart :red_heart:, please be kind with them.:hibiscus:"))

the_sum = [9, 41, 12, 3, 74, 15]
largest_so_far = -1 
print('Before', largest_so_far)

for largest in the_sum:
    if largest > largest_so_far:
        largest_so_far = largest

print('Largest number is: ', largest_so_far)

# Finding smallest number by first capturing the first value from the set
the_number = [9, 41, 12, 3, 74, 15]
smallest = None
print('Before')

for small in the_number:
    if smallest is None:
        smallest = small
    elif small < smallest:
        smallest = small

print('The smallest number is ', smallest)