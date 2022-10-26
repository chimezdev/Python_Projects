from random import randrange

    # create a 3 X 3 list
board = [[3*j+i+1 for i in range(3)] for j in range(3)]
board[1][1] = 'X' # assigns 'X' to centre element also means computer is always first to play

def display_board(board): #prints the board shape and elements
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
		    print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

display_board(board)

def verify_winner(board): # verifies there is a winner or game is a draw
    if board[0][0] == board[0][1] == board[0][2] == 'O' or board[1][0] ==\
            board[1][1] == board[1][2] == 'O' or board[2][0] == board[2][1] == board[2][2] == 'O'\
                or board[0][0] == board[1][0] == board[2][0] == 'O' or board[0][1] == board[1][1] == board[2][1] == 'O'\
                    or board[0][2] == board[1][2] == board[2][2] == 'O' or board[0][0] == board[1][1] == board[2][2] == 'O'\
                       or board[0][2] == board[1][1] == board[2][0] == 'O':

        return "Congratulations! You Won" # returns string value to caller
            
    elif board[0][0] == board[0][1] == board[0][2] == 'X' or board[1][0] ==\
        board[1][1] == board[1][2] == 'X' or board[2][0] == board[2][1] == board[2][2] == 'X'\
            or board[0][0] == board[1][0] == board[2][0] == 'X' or board[0][1] == board[1][1] == board[2][1] == 'X'\
                or board[0][2] == board[1][2] == board[2][2] == 'X' or board[0][0] == board[1][1] == board[2][2] == 'X'\
                    or board[0][2] == board[1][1] == board[2][0] == 'X':
  
        return "You Loss!"
            
    else: 
        if len(player_list) == 4: #uses the number of elems in player_list to check number of iterations
            return "Its a Draw!"    # returns draw if iteration is 4 times
        else:
            return "None"

player_list = []
comp_list = [5]

def enter_move(board):
     
    for moves in range(4): # max iteration should be four
        # The function accepts the board's current status, asks the user to make move
        player1 = int(input("Enter integer between 1-9 to make a move: "))
        while not 1 <= player1 <= 9: # validates player1 input
            print("Wrong move")
            player1 = int(input("make a move: "))
            
        while player1 in comp_list or player1 in player_list: # validates that the move has not been made before
            print("Wrong move, player is on ", player1)
            player1 = int(input("make a move: "))
            
        player_list.append(player1)
        for col in range(3):
            for row in range(3):
                if board[col][row] == player1: #updates the board with the player's move.
                    board[col][row] = 'O'
                    display_board(board)
        
        if len(player_list) == 3: #checks for winner after 3 iteration play of player
            value = verify_winner(board) # call the 'verify_winner' and assign its return value to 'value'
            if value == "None":
                pass # game continues if there is no winner
            else:
                print(value)
                break # ends game if there is a winner
        if len(player_list) == 4: #checks for winner after 4 iteration
             value = verify_winner(board)
             if value == "None":
                pass
             else:
                print(value)
                break
                    
        computer = randrange(1, 10) # generates random integer between 1-10, 10 not included
        
        while computer in player_list or computer in comp_list: # repeat random num generation if a num has been moved to
            computer = randrange(1, 10)
        
        comp_list.append(computer) 
        # computer makes it move using the random number  
        print("Computer: I move to ",computer)
        for col in range(3):
            #print(col)
            for row in range(3):
                #print(row)
                if board[col][row] == computer:
                    board[col][row] = 'X'
                    display_board(board)
        
        if len(comp_list) == 3: #checks for winner after 3 iteration play of computer
            value = verify_winner(board)
            if value == "None":
                pass
            else:
                print(value)
                break
                        
        if len(comp_list) == 4: #checks for winner after 4 iteration play of computer
            value = verify_winner(board)
            if value == "None":
                pass
            else:
                print(value)
                break

enter_move(board)

# display_board(board)
# if victor == 'you':
# 	print("You won!")
# elif victor == 'me':
# 	print("I won")
# else:
# 	print("Tie!")
# assign 'X' or numbers from 1-9 where numbers means 'empty'
# board[0][0] = 1
# board[0][1] = 2
# board[0][2] = 3
# board[1][0] = 4
# board[1][1] = 'X'
# board[1][2] = 6
# board[2][0] = 7
# board[2][1] = 8
# board[2][2] = 9

# def display_board(board):
#     # The function accepts one parameter containing the board's current status
#     # and prints it out to the console.
#     return print(board)

# display_board(board)
        