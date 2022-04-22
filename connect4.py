# Michael Dacanay, David Root, Matt Sohacki
# CSC520 Project
# Connect-4 is a two-player game in which players alternately
# place pieces on a N * M vertical board.

# An adversarial search would be the best model for this
# problem, because the two sides want to maximize their position.
import os
import sys
import math
import copy

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


def dropPiece(board, piece, col):
    """The piece drops to the lowest valid space in the given column. Returns new deepcopy of board."""
    b = copy.deepcopy(board)
    row = R - 1
    while row >= 0:
        if b[row][col] == '-':
            b[row][col] = piece
            return b
        row -= 1
    return False


def getChildren(board, piece):
    """Gets the possible board states"""
    boards = []

    # get possible moves
    for c in range(C):
        boards.append(dropPiece(board, piece, c))


gameover = False


def minimax(board, depth, player, evaluationFunction):
    # player can be 'X' or 'O'
    # evaluationFunction is a function

    # base case
    if depth == 0 or gameover == True:
        eval = evaluationFunction(board)
        return board, eval

    if player == 'X':
        maxEval = math.float('-inf')

        children = getChildren(board, player)
        for child in children:
            newBoard, eval = minimax(child, depth - 1, 'O')
            # maxEval = max(maxEval, eval)
            if eval > maxEval:
                maxEval = eval
                board = newBoard
            return board, maxEval

    else:
        minEval = math.float('inf')

        children = getChildren(board, player)
        for child in children:
            newBoard, eval = minimax(child, depth - 1, 'X')
            # minEval = min(minEval, eval)
            if eval < minEval:
                minEval = eval
                board = newBoard
            return board, minEval


def alphabeta(board, depth, player, evaluationFunction):
    # board, 4, 'X'
    # output: board
    # base case
    if depth == 0 or gameover == True:
        eval = evaluationFunction(board)
        return board, eval

    if player == 'X':
        maxEval = math.float('-inf')

        children = getChildren(board, player)
        for child in children:
            newBoard, eval = minimax(child, depth - 1, 'O')
            # maxEval = max(maxEval, eval)
            if eval > maxEval:
                maxEval = eval
                board = newBoard
            return board, maxEval

    else:
        minEval = math.float('inf')

        children = getChildren(board, player)
        for child in children:
            newBoard, eval = minimax(child, depth - 1, 'X')
            # minEval = min(minEval, eval)
            if eval < minEval:
                minEval = eval
                board = newBoard
            return board, minEval


def getColumn():
    c = int(input("Enter open column: "))
    while c < 0 or c >= C:
        c = int(input("Invalid column. Enter valid column: "))
    return c


def compete(ALG1, D1, ALG2, D2):
    global gameover
    # create new board

    turn = 0
    while gameover == False:
        if turn % 2 == 0:
            if ALG1 == 'MM':
                minimax(board, D1, 'X', evaluationFunction)
            elif ALG1 == 'AB':
                alphabeta(board, D1, 'X', evaluationFunction)
        else:
            if ALG2 == 'MM':
                minimax(board, D1, 'O', evaluationFunction)
            elif ALG2 == 'AB':
                alphabeta(board, D1, 'O', evaluationFunction)


def main():
    global R
    global C
    global board

    try:
        # Input arguments from the command line
        _, ALG1, D1, ALG2, D2 = sys.argv

        D1 = int(D1)
        D2 = int(D2)
    except:
        print("format: python connect4.py <ALG1> <DEPTH1> <ALG2> <DEPTH2>")
        return(False)

    # Board with 6 rows and 7 columns
    board = [['-' for _ in range(C)] for _ in range(R)]

    # dict
    ALGS = {
        'MM': minimax,
        'AB': alphabeta
    }
    EVALS = {
        'simple': simple,
        'complicated': complicated
    }
    ALG1 = ALGS[ALG1]
    ALG2 = ALGS[ALG2]

    # the game is played until a side wins or there is a draw
    compete(ALG1, D1, ALG2, D2)


if __name__ == "__main__":
    main()
