# Use the 'while loop' and 'if' statement to write the magician game.

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess_number = int(input("Enter a number: "))
while guess_number:
    if guess_number == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")
        guess_number = int(input("Enter a number: "))
    

# PYRAMID BLOCKS
# A pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
# Your task is to write a program which reads the number of blocks the builders have, and outputs 
# the height of the pyramid that can be built using these blocks.
# height of the pyramid is measured by the number of fully completed layers – 
# if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.
        
blocks = int(input("Enter the number of blocks: "))
#
# Write your code here.
try:
    for level in range(1, blocks+1):
        if blocks >= level: 
            height = level
            blocks -= level
    
    print("The height of the pyramid:", height)
except Exception as e:
    print("You have zero blocks", e)