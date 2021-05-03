import random
from random import randrange
from copy import deepcopy


class KI:

    def __init__(self, spiel, settings):
        self.userSettings = settings
        self.spiel = spiel

        print(self.userSettings.getDepth(self.spiel.getDisplayname())) # Tiefe erhalten aus Settings
        self.count = 0

    def move_computer_random(self):
        if self.spiel.getDisplayname() == "Tic Tac Toe": 
            self.compMove()
        else:
            possible_moves = self.spiel.get_all_possible_moves()
            print("Liste möglicher Züge: ")
            print(possible_moves)

            self.spiel.makeMove(random.choice(possible_moves))

    def compMove(self):
        bestScore = -10
        bestMove = 0

        board = self.spiel.getPerformanceBoard()
        print("FAKE Board = {}".format(board))
        print("REAL Board = {}".format(self.spiel.board))
        possible_moves = self.spiel.get_all_possible_moves(board)
        print("Moves Fake Board = {}".format(possible_moves))

        for i in range(len(possible_moves)):
            print(i)
            self.spiel.board[possible_moves[i][0]][possible_moves[i][1]] = "o"
            score = self.minimaxTTT(self.spiel.board, 0, True) 
            self.spiel.board[possible_moves[i][0]][possible_moves[i][1]] = " "
            if (score > bestScore):
                bestScore = score
                bestMove = possible_moves[i]
                #print(score)
                #print(bestMove)
        
        print(score)
        print(bestMove)

        #for row in range(len(self.spiel.board)):
        #    for col in range(len(self.spiel.board)):
        #        if self.spiel.board[row][col] == " ":
        #            self.spiel.board[row][col] = "o"
        #            score = self.minimax(0, True) 
        #            self.spiel.board[row][col] = " "
        #            if (score > bestScore):
        #                bestScore = score
        #                bestMove = [row, col]
        self.spiel.makeMove(bestMove)
        return 
    def minimax(self):


    def compMoveTTT(self):

        print(self.spiel.checkBlocked2(self.spiel.board, 1, 1, "x"))


        bestScore = -10
        bestMove = 0

        board = self.spiel.getPerformanceBoard()
        print("FAKE Board = {}".format(board))
        print("REAL Board = {}".format(self.spiel.board))
        possible_moves = self.spiel.get_all_possible_moves(board)
        print("Moves Fake Board = {}".format(possible_moves))

        for i in range(len(possible_moves)):
            print(i)
            self.spiel.board[possible_moves[i][0]][possible_moves[i][1]] = "o"
            score = self.minimaxTTT(self.spiel.board, 0, True) 
            self.spiel.board[possible_moves[i][0]][possible_moves[i][1]] = " "
            if (score > bestScore):
                bestScore = score
                bestMove = possible_moves[i]
                #print(score)
                #print(bestMove)
        
        print(score)
        print(bestMove)

        #for row in range(len(self.spiel.board)):
        #    for col in range(len(self.spiel.board)):
        #        if self.spiel.board[row][col] == " ":
        #            self.spiel.board[row][col] = "o"
        #            score = self.minimax(0, True) 
        #            self.spiel.board[row][col] = " "
        #            if (score > bestScore):
        #                bestScore = score
        #                bestMove = [row, col]
        self.spiel.makeMove(bestMove)
        return 

    def minimaxTTT(self, board, depth, isMaximizing, r = None, c = None):
        self.count = self.count + 1
        #print(self.count)

        if depth < 4:
            #print(self.spiel.checkBlocked2(self.spiel.board, r, c, "x"))

            if (self.spiel.checkWinForMark(self.spiel.board, "x")):
                print('(self.spiel.checkWinForMark(self.spiel.board, "x")):')
                return -1000
            elif self.spiel.checkBlocked3(self.spiel.board, r, c, "x"):
                #print('self.spiel.checkBlocked3(self.spiel.board, r, c, "x"):')
                return 50
            elif (self.spiel.checkWinForMark(self.spiel.board, "o")):
                #print('(self.spiel.checkWinForMark(self.spiel.board, "o")):')
                return 100
            elif (self.spiel.checkDraw()):
                #print('(self.spiel.checkDraw()):')
                return 0
            elif self.spiel.checkBlocked2(self.spiel.board, r, c, "x"):
                #print('self.spiel.checkBlocked2(self.spiel.board, r, c, "x"):')
                return 25
            #elif self.spiel.checkBetween(self.spiel.board, r, c, "x"):
            #    print('self.spiel.checkBetween(self.spiel.board, r, c, "x"):')
            #    return 10
                #print('depth > 3:')
            

            if (isMaximizing):
                bestScore = -1

                #performanceBoard = self.spiel.getPerformanceBoard()
                possible_moves = self.spiel.get_all_possible_moves(self.spiel.board)

                for i in range(len(possible_moves)):
                    self.spiel.board[possible_moves[i][0]][possible_moves[i][1]] = "o"
                    score = self.minimaxTTT(self.spiel.board, depth + 1, False, possible_moves[i][0], possible_moves[i][1]) 
                    self.spiel.board[possible_moves[i][0]][possible_moves[i][1]] = " "
                    if (score > bestScore):
                        bestScore = score
                return bestScore

            else:
                bestScore = 1

                #performanceBoard = self.spiel.getPerformanceBoard()
                possible_moves = self.spiel.get_all_possible_moves(self.spiel.board)

                for i in range(len(possible_moves)):
                    self.spiel.board[possible_moves[i][0]][possible_moves[i][1]] = "x"
                    score = self.minimaxTTT(self.spiel.board, depth + 1, True, possible_moves[i][0], possible_moves[i][1]) 
                    self.spiel.board[possible_moves[i][0]][possible_moves[i][1]] = " "
                    if (score > bestScore):
                        bestScore = score
                return bestScore
        return 0

     