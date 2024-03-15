#Encryption method used by the acient Roman soldiers
# modified to assume that the romans used numbers, lower-case letters and spaceing

text = input("Enter your message: ")
try:
    shift = int(input("Enter encryption value(1-25): "))
    while shift not in range(1, 26):
        shift = int(input("Enter number between 1-25: "))
except ValueError as e:
    print("Encryption value must be an integer number btw 1-25!", e)

cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    #char = char.upper()
    if char.islower():
        code = ord(char) + shift
        if code > ord('z'):
            code = (code - ord('z') - 1) + ord('a')
        cipher += chr(code)

    if char.isupper():
        code = ord(char) + shift
        if code > ord('Z'):
            code = (code - ord('Z') - 1) + ord('A')
        cipher += chr(code)
        
print(cipher)

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
#             cha_n = ord(cha) + shift
#             while cha_n not in range(ord('a'), ord('z') + 1):
#                 cha_n = (cha_n - ord('z') - 1) + ord('a')
#             code = chr(cha_n)
#             encode += code
#         if cha.isupper():
#             cha_n = ord(cha) + shift
#             while cha_n not in range(ord('A'), ord('Z')):
#                 cha_n = (cha_n - ord('Z') - 1) + ord('A')
#             code = chr(cha_n)
#             encode += code
# print(encode)