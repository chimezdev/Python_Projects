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


# PRACTICAL APPLICATION OF Decorator is in logging
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return(orig_func(*args, **kwargs))
    
    return wrapper

@my_logger
def display_info(name, age):
    print('display_info ran with argumens ({}, {})'.format(name, age))

display_info('John', 25)