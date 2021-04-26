import sys


class Dame:
    # class-Variable für mögliche winning-condition
    end_game = [False, '']

    startKI = [[1,1],[2,2],[1,3],[2,4],[1,5],[2,6]]
    startPlayer = [[5,1],[6,2],[5,3],[6,4],[5,5],[6,6]]

    # Feld initialisieren, aktuellen Spieler auf 'x' setzen
    def __init__(self):
        self.board = [[' ', ' ', ' ', ' ', ' ', ' '],
                      ['x', ' ', ' ', ' ', 'o', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', 'o', ' ', ' ', ' '],
                      [' ', 'x', ' ', 'x', ' ', 'x'],
                      ['x', ' ', 'x', ' ', 'x', ' ']]
        self.length = 6
        self.current_player = "x"

    def positionKI(self):
        return [[1,1],[2,2],[1,3],[2,4],[1,5],[2,6]]

    def positionPlayer(self):
        return [[5,1],[6,2],[5,3],[6,4],[5,5],[6,6]]

    # Konsolen-Ausgabe des Feldes
    def print_board(self):
        print()
        print("       0     1     2     3     4     5  ")
        print()
        print("------------------------------------------")
        for row in range(self.length):
            sys.stdout.write("{}   |".format(row))
            for col in range(self.length):
                sys.stdout.write("  {}  |".format(self.board[row][col]))
            print()
            print("------------------------------------------")
        print()

    # Konditionen für einen Sieg bestimmen
    # 1. Keine Züge mehr möglich
    # 2. Oberen/Unteren Rand mit einer Figur erreicht
    # 3. Kein Stein mehr vorhanden
    def check_winning_conditions(self):
        if len(self.get_possible_moves()) == 0:
            if self.current_player == 'x':
                return 'o'
            else:
                return 'x'
        if self.end_game[0]:
            return self.end_game[1]
        return None

    # TODO: rekursion einbauen
    # TODO: minimax?!
    def make_move(self, move):
        start = [move[0][0], move[0][1]]
        end = [move[1][0], move[1][1]]
        self.board[end[0]][end[1]] = self.board[start[0]][start[1]]

        # wenn eine Figur die obere/untere Grenze erreicht hat, dann end_game setzen
        if (end[0] == (self.length - 1) and self.board[end[0]][end[1]] == 'o') or (
                end[0] == 0 and self.board[end[0]][end[1]] == 'x'):
            self.end_game = [True, self.current_player]
        self.board[start[0]][start[1]] = ' '

        # wenn Differenz gleich 2, dann wurde eine Figur übersprungen, d.h. eine gegnerische Spielfigur muss entfernt
        # werden
        if abs(end[0] - start[0]) == 2:
            self.board[(end[0] + start[0]) // 2][(end[1] + start[1]) // 2] = ' '

        # Nach jedem Zug den aktuellen Spieler wechseln
        if self.current_player == 'x':
            self.current_player = 'o'
        else:
            self.current_player = 'x'

    def get_possible_moves(self):
        # Wert der Figuren des anderen Spielers setzen
        if self.current_player == 'o':
            enemy_player = 'x'
        else:
            enemy_player = 'o'

        # Koordinaten aller möglichen Nachbarn der aktuellen Position
        if self.current_player == 'x':
            neighbors = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
        else:
            neighbors = [[1, -1], [1, 1], [-1, -1], [-1, 1]]

        # Liste für normale Züge
        possible_moves = []
        # zweite Liste, falls ein Gegner in diesem Zug geschlagen werden kann
        possible_moves_with_enemy = []
        # für alle Elemente innerhalb des Feldes
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col].lower() == self.current_player:
                    for index in range(4):
                        if self.board[row][col].islower() and index > 1:
                            continue

                        new_row = row + neighbors[index][0]
                        new_col = col + neighbors[index][1]
                        if 0 <= new_row < len(self.board) and 0 <= new_col < len(self.board[row]):
                            # alle möglichen Züge OHNE gegnerischen Kontakt der Liste hinzufügen
                            if self.board[new_row][new_col] == ' ':
                                possible_moves.append([[row, col], [new_row, new_col]])
                            # wenn ein Gegner geschlagen werden kann wird eine seperate Liste erstellt
                            elif self.board[new_row][new_col].lower() == enemy_player:
                                new_row = new_row + neighbors[index][0]
                                new_col = new_col + neighbors[index][1]
                                if 0 <= new_row < len(self.board) and 0 <= new_col < len(self.board[row]) and \
                                        self.board[new_row][new_col] == ' ':
                                    possible_moves_with_enemy.append([[row, col], [new_row, new_col]])

        # wenn ein Gegner geschlagen werden kann, dann muss dies priorisiert werden
        if len(possible_moves_with_enemy) > 0:
            return possible_moves_with_enemy
        else:
            return possible_moves
