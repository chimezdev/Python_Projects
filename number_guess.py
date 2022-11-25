# Python program to generate a random number that a player must guess right
# in order to be set free from the loop

import random

rand_num = random.randint(1, 10) #generate a random num btw 1-10, 10 inclusive
while True:
    user_input = int(input("Guess my number. It is between 1 - 10: "))
    if user_input == rand_num:
        print("Congrats muggle, you are free to go!")
        break
    else:
        if user_input < rand_num:
            print("Your number is too small Muggle")
        elif user_input > rand_num:
            print("Number too larg")
        #rand_num = random.randint(1, 10)
        continue
print(rand_num)
        