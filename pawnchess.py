import sys
import random

class PawnChess:
    end_game = [False, ""]
    displayname = "PawnChess"
    startKI = [[0,1], [0,2], [0,3], [0,4], [0,5]]
    startPlayer = [[5,1], [5,2], [5,3], [5,4], [5,5]]
    length = 6
    current_player = "x"
    board = []

    def getDisplayname(self):
        return self.displayname

    def getStartKI(self):
        return self.startKI

    def getStartPlayer(self):
        return self.startPlayer

    def getPositionKI(self):
        board = []
        for row in range(self.length):
            for col in range(self.length):
                if self.board[row][col] == 'o':
                    board.append([row, col])
        return board

    def getPositionPlayer(self):
        board = []
        for row in range(self.length):
            for col in range(self.length):
                if self.board[row][col] == 'x':
                    board.append([row, col])
        return board
    
