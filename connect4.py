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
    return boards


gameover = False
map = [[3,4,5,7,5,4,3],[4,6,8,10,8,6,4],[5,8,11,13,11,8,5],[5,8,11,13,11,8,5],[4,6,8,10,8,6,4],[3,4,5,7,5,4,3]]

def hardcode(board):
    
    num = 0
    for x in range(C):
        for y in range(R):
            if x == 'X':
                num+=map[x,y]
            elif y == 'O':
                num -=map[x,y]
    return num


def minimax(board, depth, player, evaluationFunction):
    
    #printBoard(board)
    # player can be 'X' or 'O'
    # evaluationFunction is a function

    # base case
    if depth == 0 or gameover == True:
        eval = evaluationFunction(board)
        print('eval here')
        print(eval)
        printBoard(board)
        return board, eval

    if player == 'X':
        maxEval = -100000000

        
        children = getChildren(board, player)
        for child in children:
            newBoard, eval = minimax(child, depth - 1, 'O', evaluationFunction)
            # maxEval = max(maxEval, eval)
            if eval > maxEval:
                maxEval = eval
                board = newBoard
            return board, maxEval

    else:
        minEval = 100000000

        children = getChildren(board, player)
        for child in children:
            newBoard, eval = minimax(child, depth - 1, 'X', evaluationFunction)
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


def compete(ALG1, D1, eval1, ALG2, D2, eval2):
    global gameover
    # create new board

    turn = 0
    while gameover == False:
        if turn % 2 == 0:
            ALG1(board, D1, 'X', eval1)
        else:
            ALG2(board, D2, 'O', eval2)
            


def main():
    global R
    global C
    global board

    try:
        # Input arguments from the command line
        _, ALG1, D1, EVAL1, ALG2, D2, EVAL2= sys.argv

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
        'hc': hardcode
    }
    ALG1 = ALGS[ALG1]
    ALG2 = ALGS[ALG2]
    eval1 =EVALS[EVAL1]
    eval2 = EVALS[EVAL2]

    # the game is played until a side wins or there is a draw
    print('hello')
    compete(ALG1, D1, eval1, ALG2, D2, eval2)


if __name__ == "__main__":
    main()
