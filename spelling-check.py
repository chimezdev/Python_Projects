# say you have a block. You can use a python module called 'spellchecker' 
# to correct any mispell
# intall the package, 'pip install pyspellchecker'
from spellchecker import SpellChecker
corrector = SpellChecker()

word = input("Enter a word : ")
if word in corrector:
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct spelling is ", correct_word)
