# Michael Dacanay, David Root, Matt Sohacki
# CSC520 Project
# Connect-4 is a two-player game in which players alternately
# place pieces on a N * M vertical board.

# An adversarial search would be the best model for this
# problem, because the two sides want to maximize their position.
import os
import sys

global R
global C
R = 6
C = 7
global board


def printBoard(board):
    """Print board"""
    for i in range(R):
        for j in range(C):
            print(board[i][j], end=' ')
        print()
    print()


def dropPiece(piece, col):
    """The piece drops to the lowest valid space in the given column."""
    row = R - 1
    while row >= 0:
        # print('row:', row)
        if board[row][col] == '-':
            board[row][col] = piece
            return True
        row -= 1
    return False


def minimax():
    pass


def alphabeta():
    # board, 4, 'X'
    # output: board
    pass


def getColumn():
    c = int(input("Enter open column: "))
    while c < 0 or c >= C:
        c = int(input("Invalid column. Enter valid column: "))
    return c


def main():
    global R
    global C
    global board

    try:
        # Input arguments from the command line
        _, ALG, D1, ALG2, D2 = sys.argv
        D1 = int(D1)
        D2 = int(D2)
    except:
        print("format: python connect4.py <ALG1> <DEPTH1> <ALG2> <DEPTH2>")
        return(False)

    # Board with 6 rows and 7 columns
    board = [['-' for _ in range(C)] for _ in range(R)]

    # the game is played until a side wins
    while True:
        printBoard(board)
        col = getColumn()

        # Player
        while dropPiece('X', col) == False:
            col = getColumn()

        if ALG == 'MM':
            minimax()
        elif ALG == 'AB':
            alphabeta()


if __name__ == "__main__":
    main()
