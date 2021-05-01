class TicTacToe:

    displayname = "Tic Tac Toe"

    n = 6

    symbolKI = "o"
    symbolPlayer = "x"

    def __init__(self):
        self.positionKI = []   
        self.positionPlayer = []
        self.turn = True # TRUE = PLAYER / FALSE = KI

        self.board = [[" " for row in range(self.n)] for col in range(self.n)]
        self.genBoard()

    def newGame(self):
        self.positionKI = []
        self.positionPlayer = []
        self.board = [[" " for row in range(self.n)] for col in range(self.n)]
        self.turn = True

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

    def checkBlocked2(self, row, col, sym):
        if row is None and col is None: return False
        if row > 1:
            if self.board[row-1][col] == sym and self.board[row-2][col] == sym: return True
        elif row < 4:
            if self.board[row+1][col] == sym and self.board[row+2][col] == sym: return True
        elif col > 1:
            if self.board[row][col-1] == sym and self.board[row][col-2] == sym: return True
        elif col < 4:
            if self.board[row][col+1] == sym and self.board[row][col+2] == sym: return True
        elif row > 1 and col > 1:
            if self.board[row-1][col-1] == sym and self.board[row-2][col-2] == sym: return True
        elif row < 4 and col < 4:
            if self.board[row+1][col+1] == sym and self.board[row+2][col+2] == sym: return True
        elif row > 1 and col < 4:
            if self.board[row-1][col+1] == sym and self.board[row-2][col+2] == sym: return True
        elif row < 4 and col > 1:
            if self.board[row+1][col-1] == sym and self.board[row+2][col-2] == sym: return True
        return False

    def checkBlocked3(self, row, col, sym):
        if row is None and col is None: return False
        if row > 2:
            if self.board[row-1][col] == sym and self.board[row-2][col] == sym and self.board[row-3][col] == sym: return True
        elif row < 3:
            if self.board[row+1][col] == sym and self.board[row+2][col] == sym and self.board[row+3][col] == sym: return True
        elif col > 2:
            if self.board[row][col-1] == sym and self.board[row][col-2] == sym and self.board[row][col-3] == sym: return True
        elif col < 3:
            if self.board[row][col+1] == sym and self.board[row][col+2] == sym and self.board[row][col+3] == sym: return True
        elif row > 2 and col > 2:
            if self.board[row-1][col-1] == sym and self.board[row-2][col-2] == sym and self.board[row-3][col-3] == sym: return True
        elif row < 3 and col < 3:
            if self.board[row+1][col+1] == sym and self.board[row+2][col+2] == sym and self.board[row+3][col+3] == sym: return True
        elif row > 2 and col < 3:
            if self.board[row-1][col+1] == sym and self.board[row-2][col+2] == sym and self.board[row-3][col+3] == sym: return True
        elif row < 3 and col > 2:
            if self.board[row+1][col-1] == sym and self.board[row+2][col-2] == sym and self.board[row+3][col-3] == sym: return True
        return False

    def checkBetween(self, row, col, sym):
        if row is None and col is None: return False
        if row > 1 and row < 4:
            if self.board[row-1][col] == sym and self.board[row+1][col] == sym: return True
        if col > 1 and col < 4:
            if self.board[row][col-1] == sym and self.board[row][col+1] == sym: return True
        if col > 1 and row > 1 and col < 4 and row < 4:
            if self.board[row-1][col-1] == sym and self.board[row+1][col+1] == sym: return True
        if col > 1 and row > 1 and col < 4 and row < 4:
            if self.board[row+1][col-1] == sym and self.board[row-1][col+1] == sym: return True
        



    def checkDraw(self):
        for row in range(len(self.board)):
                for col in range(len(self.board)):
                    if self.board[row][col] == " ":
                        return False   
        return True

    def checkWinForMark(self, sym):
        if sym == "x" and self.turn is False and self.checkWin(): 
            return True
        elif sym == "o" and self.turn is True and self.checkWin(): 
            return True
        else: 
            return False

    def get_all_possible_moves(self):
        returnArr = []
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == " ":
                    returnArr.append([row, col])
        return returnArr

    def makeMove(self, move):
        if self.turn:
            self.positionPlayer.append(move)
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

    def checkWin(self):
        if self.checkRowForWin() or self.checkColForWin() or self.checkDiaForWin(): return True
        return False

    def checkDiaForWin(self):
        for row in range(len(self.board)):
                for i in range(3):
                    if self.board[row][i] != " ":
                        for j in range(4):
                            if self.board[row][i] != self.board[row+j if row <= 2 else row-j][j+i]: break
                            if j == 3: return True

    def checkRowForWin(self):
        for row in range(len(self.board)):
            for i in range(3):
                if self.board[row][i] != " ":
                    for j in range(4):
                        if self.board[row][i] != self.board[row][j+i]: break
                        if j == 3: return True
        return False

    def checkColForWin(self):
        for col in range(len(self.board)):
            for i in range(3):
                if self.board[i][col] != " ":
                    for j in range(4):
                        if self.board[i][col] != self.board[j+i][col]: break
                        if j == 3: return True
        return False

    def __isInArray(self, arr, row, col):
        for x in range(len(arr)):
            if arr[x][0] == row and arr[x][1] == col:
                return True
        return False


    

