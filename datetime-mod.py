# # The datetime module in python

# from datetime import date
# import time

# today = date.today()
# timestamp = time.time()
# my_date = date(2024, 3, 5)

# ddate = date.fromtimestamp(timestamp)
# print(ddate)
# my_date = my_date.replace(year=1993, month=1, day=4)
# print(my_date)
# isodate = date.fromisoformat("2024-03-07")
# print("FromIsoformat", isodate)
# print(isodate.strftime("%Y/%m/%d %H:%M:%S"))

# print(time.ctime())     #prints the current time, u can also pass a timestamp arg.



# # THE os MODULE IN PYTHON
# import os
# import platform         #use the 'platform' mod if u're using windows
# print(platform.uname())

# # os.mkdir("sample_dir")
# print(os.listdir())
# # os.makedirs("first_dir/second_dir")
# return_value = os.system("mkdir first_dir")
# print("windows", return_value)
# os.chdir("first_dir")
# print(os.listdir())
# print(os.getcwd())
# # os.rmdir("second_dir")


# list1 = [2**x if x % 2 == 0 else 1 for x in range(5)]
# print(list1)

# # Caesar Cipher encoding

# text = input("Enter text to encode: ")
# try: 
#     shift = int(input("Enter an encoding value: "))
#     while shift not in range(1, 26):
#         shift = input("Enter encoding value in range 1-25: ")
# except Exception as e:
#     print("An integer value is expected")
#     shift = int(input("Enter an encoding value: "))

# encode = ""
# for cha in text:
#     if not cha.isalpha():
#         encode += cha
#     else:
#         cha_n = ord(cha) + shift
#         if cha.islower():
#             while cha_n not in range(ord('a'), ord('z')):
#                 cha_n = cha_n - ord('z')
#             code = chr(cha_n)
#             encode += code
#         if cha.isupper():
#             while cha_n not in range(ord('A'), ord('Z')):
#                 cha_n = cha_n - ord('Z')
#         code = chr(ord(cha) + shift)



# SUDOKU GAME

board = [[0 for i in range(9)] for j in range(9)]
# print(board)

def verify(val):
    if val:
        return "Yes"
    else: 
        return "No"

for row in range(9):
    user_input = input("Enter row #%d (9 consecutive digits btw 1-9): " %(row + 1))
    if len(user_input) != 9:
        print("Enter exactly 9 digits for the row: ")
        continue
    try:
        int(user_input)
    except Exception as e:
        print("Please enter only digits btw 1-9")
        continue
    
    row_values = [int(digit) for digit in user_input]
    board[row] = row_values

# Verify all rows are good
valid = True
for row in board:
    if not (all(elem in range(1, 10) for elem in row) and len(set(row)) == len(row)):
        valid = False 
        break   

print(verify(valid))

# Verify all columns
if verify(valid) == "Yes":
    is_col_valid = True
    for col in range(9):
        if not (all(1 <= elem <= 9 for elem in [board[i][col] for i in range(9)]) \
                and len(set(board[i][col] for i in range(9))) == 9):
            is_col_valid = False
            break

print(verify(is_col_valid))

# Verify all sub-squares(3x3)
if verify(is_col_valid) == "Yes":
    sub_sqr = []
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            # make a string containing all digits from a sub-square
            for i in range(3):
                sub_sqr.append(board[r+i][c:c+3])

# print(sub_sqr)
                