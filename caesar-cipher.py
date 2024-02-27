#Encryption method used by the acient Roman soldiers
# modified to assume that the romans used numbers,  and spaceing

text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
