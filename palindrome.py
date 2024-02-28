# Palindromes are words that are the same when read forward and backward.

text = input("Enter your text: ")

text = text.replace(" ", "")
text2 = text[::-1]
text = text.lower()
text2 = text2.lower()
        
if all(elem.lower() == elem2.lower() for elem, elem2 in zip(text, text2)) :
    print("It's a palindrome")
else:
    print("Not a palindrome")
