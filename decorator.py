# # Python Decorators
# # decos are useful when you want to add functionality to an original func without changing the original func source code

# def decorator_function(original_fun):
#     def wrapper_fun(*args, **kwargs):
#         print('wrapper executed this before {}'.format(original_fun.__name__))
#         return original_fun(*args, **kwargs)
#     return wrapper_fun

# @decorator_function
# def display():
#     print('display function ran')

# @decorator_function
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))

# # having '@decorator_function' above the 'display()' and 'display_info' is the same as
# # display = decorator_function(display) 

# #we can execute by doing:
# display()
# display_info('John', 30)


# PRACTICAL APPLICATION OF Decorator
# # in logging
# def my_logger(orig_func):
#     import logging
#     logging.basicConfig(filename='{}'.format(orig_func.__name__), level=logging.INFO)

#     def wrapper(*args, **kwargs):
#         logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
#         return(orig_func(*args, **kwargs))
    
#     return wrapper

# @my_logger
# def display_info(name, age):
#     print('display_info ran with argumens ({}, {})'.format(name, age))

# display_info('John', 25)



# # In how long a function runs
# import time
# def my_timer(orig_func):
#     import time

#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} ran in: {} sec'.format(orig_func.__name__, t2))
#         return result
    
#     return wrapper

# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info("Stone", 30)


# def func(ops) -> int:

#     value = []
#     for rec in ops:
#         try:
#             val = int(rec)
#             value.append(val)
#         except:
#             if rec == "C":
#                 if value:
#                     value.pop()
#             elif rec == "D":
#                 if value:
#                     val = 2 * value[-1]
#                     value.append(val)
#             else:
#                 if len(value) >= 2:
#                     val = value[-1] + value[-2]
#                     value.append(val)

#     result = sum(value)

#     return result

# print(func(["5", "2", "C", "D", "+"]))


# def organizingContainers(container):
#     # Calculate the total number of balls of each type
#     ball_counts = [sum(container[i][j] for i in range(len(container))) for j in range(len(container[0]))]
#     container_sizes = sorted([sum(row) for row in container])

#     print("ball", ball_counts)
#     print(container_sizes)

# containers = [[1, 1],[2, 2],[3, 3]]
# organizingContainers(containers)

# # OR

# def is_possible(containers):
#     ball_types = set()
#     for container in containers:
#         for ball in container:
#             ball_types.add(ball)
#     return len(ball_types) <= len(containers)

# # Example usage:
# containers = [[1, 4], [2, 3]]
# print("Possible" if is_possible(containers) else "Impossible")


# #ENCRYPTION
# from math import sqrt, floor, ceil
# def encryption(s):
#     # Write your code here
#     s = s.replace(' ', '')
#     length = len(s)
#     rows = floor(sqrt(length))
#     columns = ceil(sqrt(length))
    
#     while rows * columns < length:
#         rows += 1
    
#     grid = []
#     for i in range(rows):
#         row = s[i * columns : (i + 1) * columns]
#         grid.append(row)
#     # print(grid)
    
#     encoded = " ".join("".join(grid[j][i] for j in range(rows) if i < len(grid[j])) for i in range(columns))
#     # # This whole line is equal to this:
#     # rows = len(grid)
#     # columns = max(len(row) for row in grid)  # Find the length of the longest row

#     # encoded_message = ""

#     # # Loop through each column and build the message
#     # for col in range(columns):
#     #     column_message = ""
#     #     for row in range(rows):
#     #         if col < len(grid[row]):
#     #             cell_value = grid[row][col]
#     #             if cell_value is not None:  # Ignore empty cells
#     #                 column_message += cell_value
#     #     encoded_message += column_message + " "

#     # # Remove extra space at the end
#     # encoded_message = encoded_message.strip()


#     return encoded

# string = "I am going to be very successful starting from this year"
# print(encryption(string))

# # PRACTICE
# grid = [  # This is a sample grid, replace it with your actual grid data
#     ["1", "Aa", "Bb"],
#     ["2", "3", None],  
#     ["14", None, "Cc"]
# ]

# rows = len(grid)
# columns = max(len(row) for row in grid)

# # encode by join elems of each row
# row_elem = ""
# each_row = ""
# for row_line in grid:
#     for char in row_line:
#        if char != None:
#           row_elem += char
        
#     each_row += row_elem + " "
#     row_elem = ""
# each_row = each_row.rstrip()

# print(each_row)


#Time in Words
from num2words import num2words #run 'pip install num2words'

def timeInWords(h, m):
    # Write your code here
    hour = num2words(h)
    if m == 00:
        minutes = " o' clock"
        return hour + minutes
    elif 1 <= m <= 30:
        minutes = "past "
        if m == 15:
            return "quarter " + minutes + hour
        elif m == 30:
            return "half " + minutes + hour
        else:
            return num2words(m) + " " + minutes + hour
    else:
        minutes = "to"
        return num2words(60 - m) + " " + minutes + hour


# OR 
def timeInWords(h, m):
    # Write your code here
    numbers_to_word = {
      1: "one",
      2: "two",
      3: "three",
      4: "four",
      5: "five",
      6: "six",
      7: "seven",
      8: "eight",
      9: "nine",
      10: "ten",
      11: "eleven",
      12: "twelve",
      13: "thirteen",
      14: "fourteen",
      15: "quarter",
      16: "sixteen",
      17: "seventeen",
      18: "eighteen",
      19: "nineteen",
      20: "twenty",
      21: "twenty one",
        22: "twenty two",
        23: "twenty three",
        24: "twenty four",
        25: "twenty five",
        26: "twenty six",
        27: "twenty seven",
        28: "twenty eight",
        29: "twenty nine",
      30: "half past",
    }

    hour = numbers_to_word.get(h, "") 
    minutes = ""

    if m == 00:
        minutes = " o' clock"
        return hour + minutes
    elif 1 <= m <= 30:
        minutes = "past "
        minn = numbers_to_word.get(m, "")
        if m == 15:
            return minn + " " + minutes + hour
        else:
            return minn + " minutes " + minutes + hour
        #   minutes += numbers_to_word[int(m // 10) * 10] + " " + numbers_to_word[m % 10]
    else:
        minutes = " to "
        remaining_minutes = 60 - m
        minn = numbers_to_word.get(remaining_minutes, "")
        hr = h + 1
        hour = numbers_to_word.get(hr, "")
        return minn + ' minutes' + minutes + (hour)
        # minutes += numbers_to_word[int(remaining_minutes // 10) * 10] + " " + numbers_to_word[remaining_minutes % 10]