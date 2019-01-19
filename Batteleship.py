# welcome to battleship


# make a list of 5*5 board for game
board= []

for _ in [1,2,3,4,]:
    board.append(['0'])

def print_board(board):
    for row in board:
        print(' '.join(row))


print("Let's play the battleship !")

print_board(board)

from random import randint

def random_board(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

# Genearting the random row and col for ship location
ship_row = random_row(board)
ship_col = random_col(board)

print("ship row: %d" % (ship_row))
print("ship coloumn: %d " % (ship_col))

# Guessing row and cloumns by player

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

# This checks if you guessed correct
if (guess_row == ship_row) and (guess_col == ship_col):
    print("Congrats ! you sank my battleship !")


# This checks if you guessed in the location
else:
    print("you missed !")
    board[ship_row][ship_col] == 'x'
    print_board[board]

#Bad aim


if guess_row not in range(5) or guess_cols not in range(5):
    print("you guess outside range !")
    
    
    





















    
