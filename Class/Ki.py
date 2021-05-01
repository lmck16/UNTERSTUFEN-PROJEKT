import random
from random import randrange


class KI:

    def __init__(self, spiel, settings):
        self.userSettings = settings
        self.spiel = spiel

        print(self.userSettings.getDepth(self.spiel.getDisplayname())) # Tiefe erhalten aus Settings

    def move_computer_random(self):
        if self.spiel.getDisplayname() == "Tic Tac Toe": 
            self.compMove()
        else:
            possible_moves = self.spiel.get_all_possible_moves()
            print("Liste möglicher Züge: ")
            print(possible_moves)

            self.spiel.makeMove(random.choice(possible_moves))

    def compMove(self):
        bestScore = -800
        bestMove = 0


        for row in range(len(self.spiel.board)):
            for col in range(len(self.spiel.board)):
                if self.spiel.board[row][col] == " ":
                    self.spiel.board[row][col] = "o"
                    score = self.minimax(0, False) 
                    self.spiel.board[row][col] = " "
                    if (score > bestScore):
                        bestScore = score
                        bestMove = [row, col]

        self.spiel.makeMove(bestMove)
        return 

    def minimax(self, depth, isMaximizing, r = None, c = None):
        if depth < 3:
            if r is not None and c is not None:
                if (self.spiel.checkWinForMark("x")):
                    return -1000
                #elif self.spiel.checkBlocked2(r, c, "x"):
                #    return 10
                elif (self.spiel.checkWinForMark("o")):
                    return 21
                elif (self.spiel.checkDraw()):
                    return 0
                #elif self.spiel.checkBlocked2(r, c, "x"):
                #    return 10
                #elif self.spiel.checkBetween(r, c, "x"):
                #    return 10


            if (isMaximizing):
                bestScore = -800
                for row in range(len(self.spiel.board)):
                    for col in range(len(self.spiel.board)):
                        if self.spiel.board[row][col] == " ":
                            self.spiel.board[row][col] = "o"
                            score = self.minimax(depth + 1, False, row, col)
                            self.spiel.board[row][col] = " "
                            if (score > bestScore):
                                bestScore = score
                return bestScore

            else:
                bestScore = 800
                for row in range(len(self.spiel.board)):
                    for col in range(len(self.spiel.board)):
                        if self.spiel.board[row][col] == " ":
                            self.spiel.board[row][col] = "x"
                            score = self.minimax(depth + 1, True)
                            self.spiel.board[row][col] = " "
                            if (score < bestScore):
                                bestScore = score
                return bestScore 
        return 0