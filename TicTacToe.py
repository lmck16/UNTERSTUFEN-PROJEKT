class TicTacToe:

    displayname = "Tic Tac Toe"

    n = 6

    positionKI = []   
    positionPlayer = []

    symbolKI = "O"
    symbolPlayer = "X"

    turn = True # TRUE = PLAYER / FALSE = KI

    def __init__(self):
        self.board = [[None for row in range(self.n)] for col in range(self.n)]
        self.genBoard()

    def newGame(self):
        self.positionKI = []
        self.positionPlayer = []
        self.board = [[None for row in range(self.n)] for col in range(self.n)]
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

    def nextTurn(self):
        return self.turn

    def makeMove(self, row, col):

        if self.turn:
            self.positionPlayer.append([row,col])
            self.turn = False
        else:
            self.positionKI.append([row,col])
            self.turn = True

        self.genBoard()

    def genBoard(self):
        for row in range(self.n):
            for col in range(self.n):
                if self.__isInArray(self.getPositionKI(), row, col) is True:
                    self.board[row][col] = "O"
                elif self.__isInArray(self.getPositionPlayer(), row, col) is True:
                    self.board[row][col] = "X"
                else:
                    self.board[row][col] = None

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
                    if self.board[row][i] != None:
                        for j in range(4):
                            if self.board[row][i] != self.board[row+j if row <= 2 else row-j][j+i]: break
                            if j == 3: return True

    def checkRowForWin(self):
        for row in range(len(self.board)):
            for i in range(3):
                if self.board[row][i] != None:
                    for j in range(4):
                        if self.board[row][i] != self.board[row][j+i]: break
                        if j == 3: return True
        return False

    def checkColForWin(self):
        for col in range(len(self.board)):
            for i in range(3):
                if self.board[i][col] != None:
                    for j in range(4):
                        if self.board[i][col] != self.board[j+i][col]: break
                        if j == 3: return True
        return False

    def __isInArray(self, arr, row, col):
        for x in range(len(arr)):
            if arr[x][0] == row and arr[x][1] == col:
                return True
        return False


    

