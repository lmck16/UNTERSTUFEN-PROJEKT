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

        KI_BEST_MOVE= self.minimax(self.spiel.getPositionKI(), self.spiel.getPositionPlayer(), 4, True)[1]
        print(KI_BEST_MOVE)
        self.spiel.makeMove(KI_BEST_MOVE)

    def evaluate(self, ki, player):
        return len(ki) - len(player)

    def minimax(self, KI_positions, player_positions, depth, max_player):
        if depth == 0 or self.spiel.gameOver():
            return self.evaluate(KI_positions, player_positions), KI_positions
        if max_player:
            max_eval = -1000
            best_move = None
            ## all possible moves [0]and[1] are the current position [2]and[3] the possible move
            for move_KI in self.spiel.getAllPossibleMovesMark("o"):
                print("MOVE KI {}".format(move_KI))
                print("KI_positions {}".format(KI_positions))
                print("player_positions {}".format(player_positions))
                x = deepcopy(KI_positions)
                x.remove(move_KI[0])
                x.append(move_KI[1])
                print("X {}".format(x))
                eval = self.minimax(x, player_positions, depth - 1, False)[0]  ## how do i know the state here???
                max_eval = max(max_eval, eval)
                if max_eval == eval:
                    best_move = move_KI
            return max_eval, best_move
        else:
            min_eval = 1000
            best_move = None
            ## all possible moves [0]and[1] are the current position [2]and[3] the possible move
            for move_player in self.spiel.getAllPossibleMovesMark("x"):
                x = deepcopy(player_positions)
                x.remove(move_player[0])
                x.append(move_player[1])
                eval = self.minimax(KI_positions, x, depth - 1, True)[0]  ## how do i know the state here???
                min_eval = min(min_eval, eval)
                if min_eval == eval:
                    best_move = move_player
            return min_eval, best_move