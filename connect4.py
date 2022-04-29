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
    #print(col, ' ', row)
    while row >= 0:
        if b[row][col] == '-':
            b[row][col] = piece
            return b, row
        row -= 1
    return False, False


def getChildren(tboard, piece):
    """Gets the possible board states"""
    boards = []

    # get possible moves
    for c in range(C):
        board, row = dropPiece(tboard, piece, c)
        if board != False:
            
            endGame = False
            #horizontal checker
            if c-3 > 0 and board[row][c-3] == piece and c-2>0 and board[row][c-2] == piece and c-1>0 and board[row][c-1] == piece:
                endGame = True
            elif c-2>0 and board[row][c-2] == piece and c-1>0 and board[row][c-1] == piece and c+1<C and board[row][c+1] == piece:
                endGame = True
            elif c-1>0 and board[row][c-1] == piece and c+1<C and board[row][c+1] == piece and c+2<C and board[row][c+2] == piece:
                endGame = True
            elif c+1<C and board[row][c+1] == piece and c+2<C and board[row][c+2] == piece and c+3<C and board[row][c+3] == piece:
                endGame = True
            
            #vertical checker
            if row <= 1 and not endGame:
                if board[row+1][c] == piece and board[row+2][c] == piece and board[row+3][c] == piece:
                    endGame = True
            #diagonal left checker
            if c-3 >= 0 and row-3 >= 0 and board[row-3][c-3] == piece and c-2>=0 and row-2 >= 0 and board[row-2][c-2] == piece and c-1>=0 and row-1 >= 0 and board[row-1][c-1] == piece:
                endGame = True
            if c-2>=0 and row-2 >= 0 and board[row-2][c-2] == piece and c-1>=0 and row-1 >= 0 and board[row-1][c-1] == piece and c+1 < C and row+1 < R and board[row+1][c+1] == piece:
                endGame = True
            if c-1>=0 and row-1 >= 0 and board[row-1][c-1] == piece and c+1 < C and row+1 < R and board[row+1][c+1] == piece and c+2 < C and row+2 < R and board[row+2][c+2] == piece:
                endGame = True
            if c+1 < C and row+1 < R and board[row+1][c+1] == piece and c+2 < C and row+2 < R and board[row+2][c+2] == piece and c+3 < C and row+3 < R and board[row+3][c+3] == piece:
                endGame = True
            
            #diagonal right checker
            if c-3 >= 0 and row+3 < R and board[row+3][c-3] == piece and c-2>=0 and row+2 < R and board[row+2][c-2] == piece and c-1>=0 and row+1 < R and board[row+1][c-1] == piece:
                endGame = True
            if c-2>=0 and row+2 < R and board[row+2][c-2] == piece and c-1>=0 and row+1 < R and board[row+1][c-1] == piece and c+1 < C and row-1>=0 and board[row-1][c+1] == piece:
                endGame = True
            if c-1>=0 and row+1 <R and board[row+1][c-1] == piece and c+1 < C and row-1 >=0 and board[row-1][c+1] == piece and c+2 < C and row-2>=0 and board[row-2][c+2] == piece:
                endGame = True
            if c+1 < C and row-1>=0 and board[row-1][c+1] == piece and c+2 < C and row-2 >=0 and board[row-2][c+2] == piece and c+3 < C and row-3 >=0 and board[row-3][c+3] == piece:
                endGame = True

            print('child:', row, c, endGame)
            print('eval:', hardcode(board))
            printBoard(board)
            boards.append([board,c,endGame])
    print('len', len(boards))
    return boards


gameover = False

def weightedvalue(board):
    #x wants positive and O wants negative
    for col in range(C-1):
        for row in range(R-1):
            if board[row][col] == 'X':
                numConnected = 1
                line = 1
                


map = [[3,4,5,7,5,4,3],[4,6,8,10,8,6,4],[5,8,11,13,11,8,5],[5,8,11,13,11,8,5],[4,6,8,10,8,6,4],[3,4,5,7,5,4,3]]


def hardcode(board):
    global gameover
    num = 0
    total = 0
    for col in range(C):
        for row in range(R):
            if board[row][col] == 'X':
                num+=map[row][col]
                total+=1
                #print(x,' ',y,' ',map[x][y])
            elif board[row][col] == 'O':
                num -=map[row][col]
                total+=1
                #print(x,' ',y,' ',map[x][y])
    #print('eval ',num)
    #printBoard(board)
    if total == 42:
        gameover = True
    return num


def minimax(tboard, depth, player, evaluationFunction, moves):
    #print('depth ',depth)
    overallgameOver = False
    #printBoard(board)
    # player can be 'X' or 'O'
    # evaluationFunction is a function
    # base case
    total = 0
    num = 0
    
    if depth == 0 or gameover == True:
        eval = evaluationFunction(tboard)
        #print('eval here')
        #print(eval)
        #printBoard(board)
        return tboard, eval, moves, False

    elif player == 'X':
        maxEval = -100000000

        
        children = getChildren(tboard, player)
        
        for child in children:
            if child[2] == True:
                return tboard, 10000000, child[1], child[2]
            newBoard, eval, moves, gameOver = minimax(child[0], depth - 1, 'O', evaluationFunction, moves)
            # maxEval = max(maxEval, eval)
            if gameOver:
                maxEval = eval
                tboard = newBoard
                moves = child[1]
                return tboard, maxEval, moves, child[2]
            if eval > maxEval:
                maxEval = eval
                tboard = newBoard
                moves = child[1]
        return tboard, maxEval, moves, child[2]

    else:
        minEval = 100000000

        children = getChildren(board, player)
        
        for child in children:
            if child[2] == True:
                return tboard, -10000000, child[1], child[2]
            newBoard, eval, moves, gameOver = minimax(child[0], depth - 1, 'X', evaluationFunction, moves)
            # minEval = min(minEval, eval)
            if gameOver:
                maxEval = eval
                tboard = newBoard
                moves = child[1]
                return tboard, maxEval, moves, child[2]
            if eval < minEval:
                minEval = eval
                tboard = newBoard
                moves = child[1]
        return tboard, minEval, moves, child[2]


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
    global board
    turn = 0

    while gameover == False:
        printBoard(board)
        input()
        if turn % 2 == 0:
            tboard, eval, moves, gameover = ALG1(board, D1, 'X', eval1, -1)
            print('-----------')
            print('moves', moves)
            #printBoard(tboard)
            board, temp = dropPiece(board, 'X', moves)
        else:
            tboard, eval, moves, gameover = ALG2(board, D2, 'O', eval2, -1)
            print('-----------')
            print('moves', moves)
            #printBoard(tboard)

            board, temp = dropPiece(board, 'O', moves)
        turn+=1
    print('-----------')
    printBoard(board)


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
