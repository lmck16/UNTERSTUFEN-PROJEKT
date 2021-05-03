from copy import deepcopy

class TicTacToe:

    displayname = "Tic Tac Toe"

    n = 6

    symbolKI = "o"
    symbolPlayer = "x"

    def __init__(self):
        self.positionKI = []   
        self.positionPlayer = []
        self.turn = True # TRUE = PLAYER / FALSE = KI
        self.lastMove = None
        self.board = [[" " for row in range(self.n)] for col in range(self.n)]
        self.genBoard()

    def newGame(self):
        self.positionKI = []
        self.positionPlayer = []
        self.board = [[" " for row in range(self.n)] for col in range(self.n)]
        self.lastMove = None
        self.turn = True # TRUE = PLAYER / FALSE = KI

    def getDisplayname(self):
        return self.displayname

    def getTurn(self):
        return self.turn

    def getPositionKI(self):
        return self.positionKI

    def getPositionPlayer(self):
        return self.positionPlayer

    def getStartPlayer(self):
        return []

    def getStartKI(self):
        return []

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def nextTurn(self):
        return self.turn

    def checkBlocked2(self, brd, row, col, sym):
        if row is None and col is None: return False
        con = len(brd) - 2
        #print(brd)
        #print(con)
        if row > 1:
            if brd[row-1][col] == sym and brd[row-2][col] == sym: 
                print("1")
                return True
        if row < con:
            if brd[row+1][col] == sym and brd[row+2][col] == sym: 
                print("2")
                return True
        if col > 1:
            if brd[row][col-1] == sym and brd[row][col-2] == sym:
                print("3")
                return True
        if col < con:
            if brd[row][col+1] == sym and brd[row][col+2] == sym: 
                print("4")
                return True
        if row > 1 and col > 1:
            if brd[row-1][col-1] == sym and brd[row-2][col-2] == sym: 
                print("5")
                return True
        if row < con and col < con:
            if brd[row+1][col+1] == sym and brd[row+2][col+2] == sym: 
                print("6")
                return True
        if row > 1 and col < con:
            if brd[row-1][col+1] == sym and brd[row-2][col+2] == sym: 
                print("7")
                return True
        if row < con and col > 1:
            if brd[row+1][col-1] == sym and brd[row+2][col-2] == sym: 
                print("8")
                return True
        return False

    def checkBlocked3(self, brd, row, col, sym):
        if row is None and col is None: return False
        con = len(brd) - 3
        #print(con)
        if row > 2:
            if brd[row-1][col] == sym and brd[row-2][col] == sym and brd[row-3][col] == sym: return True
        if row < con:
            if brd[row+1][col] == sym and brd[row+2][col] == sym and brd[row+3][col] == sym: return True
        if col > 2:
            if brd[row][col-1] == sym and brd[row][col-2] == sym and brd[row][col-3] == sym: return True
        if col < con:
            if brd[row][col+1] == sym and brd[row][col+2] == sym and brd[row][col+3] == sym: return True
        if row > 2 and col > 2:
            if brd[row-1][col-1] == sym and brd[row-2][col-2] == sym and brd[row-3][col-3] == sym: return True
        if row < con and col < con:
            if brd[row+1][col+1] == sym and brd[row+2][col+2] == sym and brd[row+3][col+3] == sym: return True
        if row > 2 and col < con:
            if brd[row-1][col+1] == sym and brd[row-2][col+2] == sym and brd[row-3][col+3] == sym: return True
        if row < con and col > 2:
            if brd[row+1][col-1] == sym and brd[row+2][col-2] == sym and brd[row+3][col-3] == sym: return True
        return False

    def checkBetween(self, brd, row, col, sym):
        if row is None and col is None: return False
        con = len(brd) - 1
        if row > 1 and row < con:
            if brd[row-1][col] == sym and brd[row+1][col] == sym: return True
        if col > 1 and col < con:
            if brd[row][col-1] == sym and brd[row][col+1] == sym: return True
        if col > 1 and row > 1 and col < con and row < con:
            if brd[row-1][col-1] == sym and brd[row+1][col+1] == sym: return True
        if col > 1 and row > 1 and col < con and row < con:
            if brd[row+1][col-1] == sym and brd[row-1][col+1] == sym: return True
        return False

    def checkDraw(self, brd = None):
        if brd is None: brd = self.board
        for row in range(len(brd)):
                for col in range(len(brd)):
                    if brd[row][col] == " ":
                        return False   
        return True

    def getPerformanceBoard(self):
        lastRow = self.lastMove[0]
        lastCol = self.lastMove[1]

        board = deepcopy(self.board)

        if lastRow in (0,1,2) and lastCol in (0,1,2): 
            for i in range(self.n):
                board[i][4] = "o"
                board[i][5] = "o"
                board[4][i] = "o"
                board[5][i] = "o"      
            return board
        elif lastRow in (0,1,2) and lastCol in (3,4,5): 
            for i in range(self.n):
                board[i][0] = "o"
                board[i][1] = "o"
                board[4][i] = "o"
                board[5][i] = "o"
            return board
        elif lastRow in (3,4,5) and lastCol in (0,1,2): 
            for i in range(self.n):
                board[i][4] = "o"
                board[i][5] = "o"
                board[0][i] = "o"
                board[1][i] = "o"
            return board
        elif lastRow in (3,4,5) and lastCol in (3,4,5): 
            for i in range(self.n):
                board[i][0] = "o"
                board[i][1] = "o"
                board[0][i] = "o"
                board[1][i] = "o"
            return board
        else: return None

    def checkWinForMark(self, board, sym):
        if sym == "x" and self.turn is False and self.checkWin(board): 
            return True
        elif sym == "o" and self.turn is True and self.checkWin(board): 
            return True
        else: 
            return False

    def get_all_possible_moves(self, board = None):
        if board is None: board = self.board
        returnArr = []
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == " ":
                    returnArr.append([row, col])
        return returnArr

    def makeMove(self, move):
        if self.turn:
            self.positionPlayer.append(move)
            self.lastMove = move
            self.turn = False
        else:
            self.positionKI.append(move)
            self.turn = True

        self.genBoard()

    def genBoard(self):
        for row in range(self.n):
            for col in range(self.n):
                if self.__isInArray(self.getPositionKI(), row, col) is True:
                    self.board[row][col] = "o"
                elif self.__isInArray(self.getPositionPlayer(), row, col) is True:
                    self.board[row][col] = "x"
                else:
                    self.board[row][col] = " "

    def checkDiagonals(self, board):
        if len(set([board[i][i] for i in range(len(board))])) == 1:
            return board[0][0]
        if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
            return board[0][len(board)-1]
        return 0

    def checkWin(self, board = None):
        if board is None: board = self.board
        if self.checkRowForWin(board) or self.checkColForWin(board) or self.checkDiaForWin(board): return True
        return False

    def checkDiaForWin(self, board):
        for row in range(len(board)):
            for i in range(3):
                if board[row][i] != " ":
                    for j in range(4):
                        if board[row][i] != board[row+j if row <= 2 else row-j][j+i]: break
                        if j == 3: return True
        return False

    def checkRowForWin(self, board):
        for row in range(len(board)):
            for i in range(3):
                if board[row][i] != " ":
                    for j in range(4):
                        if board[row][i] != board[row][j+i]: break
                        if j == 3: return True
        return False

    def checkColForWin(self, board):
        for col in range(len(board)):
            for i in range(3):
                if board[i][col] != " ":
                    for j in range(4):
                        if board[i][col] != board[j+i][col]: break
                        if j == 3: return True
        return False

    def __isInArray(self, arr, row, col):
        for x in range(len(arr)):
            if arr[x][0] == row and arr[x][1] == col:
                return True
        return False

    

