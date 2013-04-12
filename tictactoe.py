def oddTurn(board, oddMoves, evenMoves):
    """return True means odd has a winning strategy"""
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
                    return True
    return False

def evenTurn(board, oddMoves, evenMoves):
    """return True means odd wins no matter what even move"""
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
                    return False
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

import itertools

#oddMoves = set([1,3,5,7,9])
#evenMoves = set([2,4,6,8])
#board = [0]*9

moves = set(range(1,10))
for i in itertools.combinations(range(1,10), 5):
    games = 0
    p1Moves = set(i)
    p2Moves = moves - p1Moves
    board = [-100]*9
    oddWin = oddTurn(board, p1Moves, p2Moves)
    if oddWin is False:
        print "BIG PROBLEM"
        break
    print p1Moves, p2Moves, oddWin, games

#print oddTurn(board, oddMoves, evenMoves)