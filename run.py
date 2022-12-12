

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

ABC123 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
def pick_a_ship():
    pick_row = input('\nEnter row number 1-5:').upper()

    while pick_row not in '12345':
        print(f"{pick_row} is not a number between 1-5")
        pick_row = input('\nEnter row 1-5:')

    pick_column = input('\nPick column letter A-E:')

    while pick_column not in 'ABCDE':
        print(f"{pick_column} is not a letter between A-E")
        pick_column = input('\nPick column letter A-E:')

    return int(pick_row), ABC123[pick_column]                                                , ABC123[pick_column]

