from Dame import Dame
from Dame import sys
import random


def move_player(board):
    print('Spieler ' + board.current_player + ' am Zug')

    # alle möglichen Züge ziehen
    possible_moves = board.get_possible_moves()
    print("Liste möglicher Züge: ")
    print(possible_moves)

    valid_move = False
    # solange ausführen bis User einen validen Zug gewählt hat
    while not valid_move:
        print("Eingabe für Zug (für [4, 1] 41 eingeben), Start und Ende mit Leerzeichen separieren: ")
        start, end = map(int, sys.stdin.readline().split())
        # Eingabe für Koordinaten formatieren, Zehner und EInser separieren
        move = [[start // 10, start % 10], [end // 10, end % 10]]
        # vergleichen ob Usereingabe ein gültiger Zug ist
        if move in possible_moves:
            board.make_move(move)
            valid_move = True


def move_computer_random(board):
    print('Bot mit ' + board.current_player + ' am Zug')

    possible_moves = board.get_possible_moves()
    print("Liste möglicher Züge: ")
    print(possible_moves)

    board.make_move(random.choice(possible_moves))


if __name__ == "__main__":
    # Spielfeld der Konsole initialisieren und initial einmal ausgeben
    new_game = Dame()
    new_game.print_board()

    # Schleife solange ausführen bis ein Spieler gewonnen hat
    # nach jedem Zug wird der Spieler gewechselt
    while new_game.check_winning_conditions() is None:
        if new_game.current_player == 'x':
            move_player(new_game)
        # Vorerst AI mit nur zufälligen Zügen
        else:
            move_computer_random(new_game)
        # aktualisiertes Feld ausgeben
        new_game.print_board()

    print("Gewinner: " + new_game.check_winning_conditions())
