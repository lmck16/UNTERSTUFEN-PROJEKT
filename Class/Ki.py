import random
from random import randrange


class KI:

    def __init__(self, spiel, settings):
        self.userSettings = settings
        self.spiel = spiel

        print(self.userSettings.getDepth(self.spiel.getDisplayname())) # Tiefe erhalten aus Settings

    def move_computer_random(self):
        possible_moves = self.spiel.get_all_possible_moves()
        print("Liste möglicher Züge: ")
        print(possible_moves)

        self.spiel.makeMove(random.choice(possible_moves))
