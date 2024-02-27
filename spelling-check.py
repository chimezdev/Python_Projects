# # say you have a block. You can use a python module called 'spellchecker' 
# # to correct any mispell
# # intall the package, 'pip install pyspellchecker'
# from spellchecker import SpellChecker
# corrector = SpellChecker()

# word = input("Enter a word : ")
# if word in corrector:
#     print("Correct")
# else:
#     correct_word = corrector.correction(word)
#     print("Correct spelling is ", correct_word)


# the_text = """A variation of the ordinary lorem ipsum
# text has been used in typesetting since the 1960s 
# or earlier, when it was popularized by advertisements 
# for Letraset transfer sheets. It was introduced to 
# the Information Age in the mid-1980s by the Aldus Corporation, 
# which employed it in graphics and word-processing templates
# for its desktop publishing program PageMaker (from Wikipedia)"""

# fnd = the_text.find('the')
# for txt in the_text:
#     if fnd != -1:
#         print(fnd)
#         fnd = the_text.find('the', fnd + 1)

# def mysplit(strng):
#     if not isinstance(strng, str):
#         return "Only string is allowed as argument"
#     to_list = list()
#     cur_word = ""
#     for char in strng:
#         if char == " ":
#             if cur_word:
#                 to_list.append(cur_word)
#                 cur_word = ""
#         else: cur_word += char
    
#     if cur_word:
#         to_list.append(cur_word)
        
#     return to_list
#     # put your code here
#     #

# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))
    
# digits = [ '1111110',  	# 0
# 	   '0110000',	# 1
# 	   '1101101',	# 2
# 	   '1111001',	# 3
# 	   '0110011',	# 4
# 	   '1011011',	# 5
# 	   '1011111',	# 6
# 	   '1110000',	# 7
# 	   '1111111',	# 8
# 	   '1111011',	# 9
# 	   ]


# def print_number(num):
# 	global digits
# 	digs = str(num)
# 	lines = [ '' for lin in range(5) ]
# 	for d in digs:
# 		segs = [ [' ',' ',' '] for lin in range(5) ]
# 		ptrn = digits[ord(d) - ord('0')]
# 		if ptrn[0] == '1':
# 			segs[0][0] = segs[0][1] = segs[0][2] = '#'
# 		if ptrn[1] == '1':
# 			segs[0][2] = segs[1][2] = segs[2][2] = '#'
# 		if ptrn[2] == '1':
# 			segs[2][2] = segs[3][2] = segs[4][2] = '#'
# 		if ptrn[3] == '1':
# 			segs[4][0] = segs[4][1] = segs[4][2] = '#'
# 		if ptrn[4] == '1':
# 			segs[2][0] = segs[3][0] = segs[4][0] = '#'
# 		if ptrn[5] == '1':
# 			segs[0][0] = segs[1][0] = segs[2][0] = '#'
# 		if ptrn[6] == '1':
# 			segs[2][0] = segs[2][1] = segs[2][2] = '#'
# 		for lin in range(5):
# 			lines[lin] += ''.join(segs[lin]) + ' '
# 	for lin in lines:
# 		print(lin)

# print_number(int(input("Enter the number you wish to display: ")))

