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


