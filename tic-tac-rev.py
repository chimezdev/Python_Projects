# Tic-Tac-Toe game written in python

from random import randrange

board = [ [i + 3 * (j - 1) for i in range(1, 4)] for j in range(1, 4) ] # make an empty board

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

print("WELCOME!")
display_board(board)

# comp = randrange(1, 9)
def enter_move(board):
    while True:
        try:
            user = int(input("Your turn, 'Make a move by entering the box number': "))
            found = False
            for i, row in enumerate(board):
                for j, col in enumerate(row):
                    if user == col:
                        board[i][j] = "O"
                        found = True
                        break
            if not found:
                print("Invalid move! Please choose a box with a number: ")
            else: break
        except ValueError as e:
            print("Invalid move!, 'Enter a valid box number': ")

def draw_move(board):
    while True:
        found = False
        comp = randrange(1, 10)
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if comp == col:
                    board[i][j] = 'X'
                    found = True
                    break
      # print('me', comp)
        if not found:
            continue
        else: break

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    empty_sq =list()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] in range(10):
                empty_sq.append((i, j))
    return empty_sq

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    if sign == 'X':
        who = 'me'
    elif sign == 'O':
        who = 'you'
    else: who = None

    # Check rows
    for row in board:
        if all(element == sign for element in row):
            return who

    # Check columns
    for col in range(3):
        if all(board[i][col] == sign for i in range(3)):
            return who

    # Check diagonals
    if all(board[i][i] == sign for i in range(3)):
        return who
    if all(board[i][2-i] == sign for i in range(3)):
        return who

    return None
            

print("I play first")
board[1][1] = "X"

free = make_list_of_free_fields(board)
human_turn = True

while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
        if victor == 'you':
            print('CONGRATULATIONS! YOU WON')
            break
        display_board(board)
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
        if victor == 'me':
            print('I WON!')
            break
        display_board(board)
    if victor == None and len(free) <= 2:
        print('DRAW!')
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)
