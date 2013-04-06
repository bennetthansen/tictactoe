oddMoves = set([1,3,5,7,9])
evenMoves = set([2,4,6,8])
board = [0]*9

def oddTurn(board, oddMoves, evenMoves):
    """return True means odd has a winning strategy"""
    for i in range(9):
        if board[i]==0:
            for j in oddMoves:
                newboard = board[:]
                newboard[i] = j
                print newboard
                if isGameOver(newboard)==1:
                    return True
                elif isGameOver(newboard)==2:
                    return False
                newoddMoves = oddMoves-set([j])
                newevenMoves = evenMoves.copy()
                if evenTurn(newboard, newoddMoves, newevenMoves) is False:
                    return False
    return True

def evenTurn(board, oddMoves, evenMoves):
    """return True means odd wins no matter what even move"""
    for i in range(9):
        if board[i]==0:
            for j in evenMoves:
                newboard = board[:]
                newboard[i] = j
                print newboard
                if isGameOver(newboard)==1:
                    return False
                newoddMoves = oddMoves.copy()
                newevenMoves = evenMoves-set([j])
                if oddTurn(newboard, newoddMoves, newevenMoves) is True:
                    return True
    return False

def isGameOver(board):
    """return 0 for unfinished, 1 for win, 2 for tie"""
    if board[0]+board[1]+board[2]==15 or board[3]+board[4]+board[5]==15 or board[6]+board[7]+board[8]==15 or board[0]+board[3]+board[6]==15 or board[1]+board[4]+board[7]==15 or board[2]+board[5]+board[8]==15 or board[0]+board[4]+board[8]==15 or board[2]+board[4]+board[6]==15:
        return 1
    if board[0]!=0 and board[1]!=0 and board[2]!=0 and board[3]!=0 and board[4]!=0 and board[5]!=0 and board[6]!=0 and board[7]!=0 and board[8]!=0:
        return 2
    return 0

oddTurn(board, oddMoves, evenMoves)
