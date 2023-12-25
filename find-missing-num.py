
def find_missing_numbers(holder):
    numbers = set(holder) #create a set, (a datatype with curly braces, unordered, unchangeable)
    result = []
    for num in range(1, holder[-1]): #search to the elem before the last one
        if num not in numbers:
            result.append(num)
    return result


holder = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(find_missing_numbers(holder))
