

# Import function to generate random integers
from random import randint


# Declaring sequences for the game board.
INVISIBLE_BOARD = [[' '] * 5 for b in range(5)] 
VISIBLE_BOARD = [[' '] * 5 for b in range(5)]


def shape_board(board):
    """
    Restuctures list sequence to a game board style.
    """
    rows = 1
    for row in board:
        print(rows, '|'.join(row))
        rows += 1


def make_ships(board):
    """
    Creates five ships in random locations.
    """
    for ship in range(5):
        ship_row = randint(0, 4)
        ship_column = randint(0, 4)
        while board[ship_row][ship_column] != 'X':
            board[ship_row][ship_column] = 'X'
            

def pick_a_ship():
    pass
