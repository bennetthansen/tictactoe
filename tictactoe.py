def oddTurn(board, oddMoves, evenMoves):
    """return True means odd has a winning strategy"""
    tupleBoard = tuple(board)
    if knownBoards.has_key(tupleBoard):
        return knownBoards.get(tupleBoard)
    for i in range(9):
        if board[i]==-100:
            for j in oddMoves:
                newboard = board[:]
                newboard[i] = j
                #print newboard
                if isGameOver(newboard)==1:
                    return True
                elif isGameOver(newboard)==2:
                    return False
                newoddMoves = oddMoves-set([j])
                newevenMoves = evenMoves.copy()
                if evenTurn(newboard, newoddMoves, newevenMoves) is True:
                    symmetries(tupleBoard, True)
                    return True
    symmetries(tupleBoard, False)
    return False

def evenTurn(board, oddMoves, evenMoves):
    """return True means odd wins no matter what even move"""
    tupleBoard = tuple(board)
    if knownBoards.has_key(tupleBoard):
        return knownBoards.get(tupleBoard)
    for i in range(9):
        if board[i]==-100:
            for j in evenMoves:
                newboard = board[:]
                newboard[i] = j
                #print newboard
                if isGameOver(newboard)==1:
                    return False
                newoddMoves = oddMoves.copy()
                newevenMoves = evenMoves-set([j])
                if oddTurn(newboard, newoddMoves, newevenMoves) is False:
                    symmetries(tupleBoard, False)
                    return False
    symmetries(tupleBoard, True)
    return True

def isGameOver(board):
    """return 0 for unfinished, 1 for win, 2 for tie"""
    global games
    games += 1
    if sum(board[0::3])==15 or sum(board[1::3])==15 or sum(board[2::3])==15 or sum(board[0:3])==15 or sum(board[3:6])==15 or sum(board[6:9])==15 or sum(board[0::4])==15 or sum(board[2:7:2])==15:
        #print board
        return 1
    if sum(board)>0:
        return 2
    return 0

def symmetries(board, value):
    global knownBoards
    #boardCopy = board[:]
    boardReflectHorizontal = tuple([board[2], board[1], board[0], board[5], board[4], board[3], board[8], board[7], board[6]])
    boardReflectVertical = tuple([board[6], board[7], board[8], board[3], board[4], board[5], board[0], board[1], board[2]])
    boardReflectDiagonal1 = tuple([board[8], board[5], board[2], board[7], board[4], board[1], board[6], board[3], board[0]])
    boardReflectDiagonal2 = tuple([board[0], board[3], board[6], board[1], board[4], board[7], board[2], board[5], board[8]])
    boardRotate1 = tuple([board[6], board[3], board[0], board[7], board[4], board[1], board[8], board[5], board[2]])
    boardRotate2 = tuple([board[8], board[7], board[6], board[5], board[4], board[3], board[2], board[1], board[0]])
    boardRotate3 = tuple([board[2], board[5], board[8], board[1], board[4], board[7], board[0], board[3], board[6]])
    knownBoards.update({board : value, boardReflectHorizontal : value, boardReflectVertical : value, boardReflectDiagonal1 : value, boardReflectDiagonal2 : value, boardRotate1 : value, boardRotate2 : value, boardRotate3 : value})

import itertools

#oddMoves = set([1,3,5,7,9])
#evenMoves = set([2,4,6,8])
#board = [0]*9

knownBoards = {}
games = 0

def runGame():
    global games
    global knownBoards
    knownBoards.clear()
    moves = set(range(1,10))
    for i in itertools.combinations(range(1,10), 5):
        games = 0
        p1Moves = set(i)
        p2Moves = moves - p1Moves
        board = [-100]*9
        knownBoards.clear()
        oddWin = oddTurn(board, p1Moves, p2Moves)
        if oddWin is False:
            print "No winning strategy for Player 1"
            break
        print p1Moves, p2Moves, oddWin, games
        break

#print oddTurn(board, oddMoves, evenMoves)