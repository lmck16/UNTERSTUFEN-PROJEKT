import random
from random import randrange
from copy import deepcopy


class KI:

    def __init__(self, spiel, settings):
        self.userSettings = settings
        self.spiel = spiel

        print(self.userSettings.getDepth(self.spiel.getDisplayname()))  # Tiefe erhalten aus Settings
        self.count = 0

    def move_computer_random(self):

        if self.spiel.getDisplayname() == "Tic Tac Toe":
            possible_moves = self.spiel.get_all_possible_moves()
            self.spiel.makeMove(random.choice(possible_moves))
        else:
            KI_BEST_MOVE = self.minimax(self.spiel.getPositionKI(), self.spiel.getPositionPlayer(), 2, True)[1]
            z = deepcopy(self.spiel.getPositionKI())

            for x in self.spiel.getPositionKI():
                for y in KI_BEST_MOVE:
                    if x == y:
                        KI_BEST_MOVE.remove(x)
                        z.remove(x)
            make_move=[z[0],KI_BEST_MOVE[0]]
            self.spiel.makeMove(make_move)

    def evaluate(self, ki, player):
        return len(ki) - len(player)

    def minimax(self, KI_positions, player_positions, depth, max_player):
        if depth == 0 or self.spiel.gameOver():
            return self.evaluate(KI_positions, player_positions), KI_positions
        if max_player:
            max_eval = -1000
            best_move = None
            all_KI_possible_moves = []
            y = self.spiel.getAllPossibleMovesMark("o")
            for move_KI in self.spiel.getAllPossibleMovesMark("o"):
                x = deepcopy(KI_positions)
                x.remove(move_KI[0])
                x.append(move_KI[1])
                all_KI_possible_moves.append(x)

            for move_KI in all_KI_possible_moves:
                eval = self.minimax(x, player_positions, depth - 1, False)[0]
                max_eval = max(max_eval, eval)
                if max_eval == eval:
                    best_move = move_KI
            return max_eval, best_move
        else:
            min_eval = 1000
            best_move = None
            all_player_possible_moves = []
            y = self.spiel.getAllPossibleMovesMark("x")
            for move_player in self.spiel.getAllPossibleMovesMark("x"):
                x = deepcopy(player_positions)
                x.remove(move_player[0])
                x.append(move_player[1])
                all_player_possible_moves.append(x)
            for move_player in all_player_possible_moves:
                eval = self.minimax(KI_positions, x, depth - 1, True)[0] 
                min_eval = min(min_eval, eval)
                if min_eval == eval:
                    best_move = move_player
            return min_eval, best_move
