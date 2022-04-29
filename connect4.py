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
        #print('child:', c)
        #printBoard(tboard)
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

            #print('child:', piece, row, c, endGame)
            #print('eval:', owneval(board))
            #printBoard(board)
            boards.append([board,c,endGame])
    #print('len', len(boards))
    return boards

gameover = False
def calcEvalAdd(connected):
    eval = 0
    if connected >= 4:
        eval = 10000000
        return eval
    elif connected == 3:
        eval += 1000
    elif connected == 2:
        eval += 10
    else:
        eval += 1
    return eval
def weightedvalue(board):
    #x wants positive and O wants negative
    eval = 0
    for col in range(C):
        for row in range(R):
            if board[row][col] == 'X':
                piece = 'X'
                
                #horizontal check
                counter = 1
                connected = 1
                left = True
                right = True
                while counter < 4:
                    if left and col-counter >= 0 and board[row][col-counter] == piece:
                        connected+=1
                    else:
                        left = False
                    if right and col+counter < C and board[row][col+counter] == piece:
                        connected+=1
                    else:
                        right = False
                    counter+=1
                eval+=calcEvalAdd(connected)
                #vertical
                counter = 1
                connected = 1
                up = True
                down = True
                while counter < 4:
                    if up and row-counter >= 0 and board[row-counter][col] == piece:
                        connected+=1
                    else:
                        up = False
                    if down and row+counter < R and board[row+counter][col] == piece:
                        connected+=1
                    else:
                        down = False
                    counter+=1
                eval+=calcEvalAdd(connected)
                #diagonal left
                counter = 1
                connected = 1
                leftup = True
                rightdown = True
                while counter < 4:
                    if leftup and row-counter >= 0 and col-counter >= 0 and board[row-counter][col-counter] == piece:
                        connected+=1
                    else:
                        leftup = False
                    if rightdown and row+counter < R and col+counter < C and board[row+counter][col+counter] == piece:
                        connected+=1
                    else:
                        rightdown = False
                    counter+=1
                eval+=calcEvalAdd(connected)
                #diagonal right
                counter = 1
                connected = 1
                rightup = True
                leftdown = True
                while counter < 4:
                    if rightup and row-counter >= 0 and col+counter <C and board[row-counter][col+counter] == piece:
                        connected+=1
                    else:
                        rightup = False
                    if leftdown and row+counter < R and col-counter >=0 and board[row+counter][col-counter] == piece:
                        connected+=1
                    else:
                        leftdown = False
                    counter+=1
                eval+=calcEvalAdd(connected)
            elif board[row][col] == 'O':
                piece = 'O'
                
                #horizontal check
                counter = 1
                connected = 1
                left = True
                right = True
                while counter < 4:
                    if left and col-counter >= 0 and board[row][col-counter] == piece:
                        connected+=1
                    else:
                        left = False
                    if right and col+counter < C and board[row][col+counter] == piece:
                        #print('rights working')
                        connected+=1
                    else:
                        right = False
                    counter+=1
                eval-=calcEvalAdd(connected)
                #vertical
                counter = 1
                connected = 1
                up = True
                down = True
                while counter < 4:
                    if up and row-counter >= 0 and board[row-counter][col] == piece:
                        connected+=1
                    else:
                        up = False
                    if down and row+counter < R and board[row+counter][col] == piece:
                        connected+=1
                    else:
                        down = False
                    counter+=1
                eval-=calcEvalAdd(connected)
                #diagonal left
                counter = 1
                connected = 1
                leftup = True
                rightdown = True
                while counter < 4:
                    if leftup and row-counter >= 0 and col-counter >= 0 and board[row-counter][col-counter] == piece:
                        connected+=1
                    else:
                        leftup = False
                    if rightdown and row+counter < R and col+counter < C and board[row+counter][col+counter] == piece:
                        connected+=1
                    else:
                        rightdown = False
                    counter+=1
                eval-=calcEvalAdd(connected)
                #diagonal right
                counter = 1
                connected = 1
                rightup = True
                leftdown = True
                while counter < 4:
                    if rightup and row-counter >= 0 and col+counter <C and board[row-counter][col+counter] == piece:
                        connected+=1
                    else:
                        rightup = False
                    if leftdown and row+counter < R and col-counter >=0 and board[row+counter][col-counter] == piece:
                        connected+=1
                    else:
                        leftdown = False
                    counter+=1
                eval-=calcEvalAdd(connected)
    return eval
                
                
                




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

def owneval(board):
    num = weightedvalue(board)
    for col in range(C):
        for row in range(R):
            if board[row][col] == 'X':
                num+=map[0][col]
                
                #print(x,' ',y,' ',map[x][y])
            elif board[row][col] == 'O':
                num -=map[0][col]
    return num
def minimax(tboard, depth, player, evaluationFunction, moves):
    #print(player)
    tboard = copy.deepcopy(tboard)
    #print('start of minimax')
    #printBoard(tboard)
    #print('depth ',depth)
    overallgameOver = False
    #printBoard(board)
    # player can be 'X' or 'O'
    # evaluationFunction is a function
    # base case
    total = 0
    num = 0
    tmoves = 0
    if depth == 0 or gameover == True:
        eval = evaluationFunction(tboard)
        #print('eval here')
        #print(eval)
        #printBoard(tboard)
        return tboard, eval, moves, False

    
    elif player == 'X':
        maxEval = -100000000000

        
        children = getChildren(tboard, player)
        l = 0
        for child in children:
            #print('minmax')
            #printBoard(child[0])
            if child[2] == True:
                return child[0], 1000000, child[1], child[2]
            newBoard, eval, tmoves, gameOver = minimax(child[0], depth - 1, 'O', evaluationFunction, moves)
            #print('childBoard')
            #printBoard(newBoard)
            # maxEval = max(maxEval, eval)
            
            if eval > maxEval:
                maxEval = eval
                tboard = newBoard
                moves = child[1]
                #print('best X move:', moves)
            
        #print('best X move before returning:', moves)
       
        return tboard, maxEval, moves, False

    elif player == 'O':
        minEval = 1000000000000

        children = getChildren(tboard, player)
        
        for child in children:
            #print('child')
            #printBoard(child[0])
            if child[2] == True:
                #print('eval here finish')
                #print(-100000000)
                #printBoard(tboard)
                return child[0], -1000000, child[1], child[2]
            newBoard, eval, tmoves, gameOver = minimax(child[0], depth - 1, 'X', evaluationFunction, moves)
            # minEval = min(minEval, eval)
            
            if eval < minEval:
                minEval = eval
                tboard = newBoard
                moves = child[1]
                #print('best O move:', moves)
            
        #print('best O move before returning:', moves)
        return tboard, minEval, moves, False


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
def player(tboard, depth, player, evaluationFunction, moves):
    print('pick a column', player )
    col = int(input())
    return tboard, 0, col, False

def compete(ALG1, D1, eval1, ALG2, D2, eval2):
    global gameover
    # create new board
    global board
    turn = 0

    while gameover == False:
        printBoard(board)
        input()
        temp = 0
        if turn % 2 == 0:
            tboard, eval, moves, gameover = ALG1(board, D1, 'X', eval1, -1)
            
            print('-----------\n----------')
            print('X moves', moves)
            #printBoard(tboard)
            #print(temp)
            if gameover:
                print ('X wins!')
            board, temp = dropPiece(board, 'X', moves)
        else:
            tboard, eval, moves, gameover = ALG2(board, D2, 'O', eval2, -1)
            print('-----------\n----------')
            print('O moves', moves)
            #print(temp)
            #printBoard(tboard)
            if gameover:
                print ('O wins!')
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
        'AB': alphabeta,
        'PL': player
    }
    EVALS = {
        'hc': hardcode,
        'wv': weightedvalue,
        'oe': owneval
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
