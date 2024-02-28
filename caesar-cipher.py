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
