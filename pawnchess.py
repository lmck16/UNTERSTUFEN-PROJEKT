import sys
import random

class PawnChess:
    displayname = "Bauernschach"

    def __init__(self):
        self.startKI = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
        self.startPlayer = [[5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
        # class-Variable für mögliche winning-condition
        self.end_game = [False, '']
        self.board = [['o', 'o', 'o', 'o', 'o', 'o'],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' '],
                      ['x', 'x', 'x', 'x', 'x', 'x']]
        self.length = 6
        self.current_player = "x"

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

    def move_player(self):
        print('Spieler ' + self.current_player + ' am Zug')
        # alle möglichen Züge ziehen
        possible_moves = self.get_movable_figures()
        print("Positionen beweglicher Figuren: ")
        print(possible_moves)
        start = int(input())
        valid_move = False
        # solange ausführen bis User einen validen Zug gewählt hat
        while not valid_move:
            possible_moves_clicked = self.get_possible_moves_clicked(start // 10, start % 10)
            print("Wohin Figur ziehen?")
            print(possible_moves_clicked)
            end = int(input())
            # Eingabe für Koordinaten formatieren, Zehner und EInser separieren
            move = [end // 10, end % 10]
            # vergleichen ob Usereingabe ein gültiger Zug ist
            if move in possible_moves_clicked:
                self.makeMove([[start // 10, start % 10], move])
            valid_move = True

    def makeMove(self, move):
        start = [move[0][0], move[0][1]]
        end = [move[1][0], move[1][1]]
        self.board[end[0]][end[1]] = self.board[start[0]][start[1]]

        # wenn eine Figur die obere/untere Grenze erreicht hat, dann end_game setzen
        if (end[0] == (self.length - 1) and self.board[end[0]][end[1]] == 'o') or (
                end[0] == 0 and self.board[end[0]][end[1]] == 'x'):
            self.end_game = [True, self.current_player]
        self.board[start[0]][start[1]] = ' '

        # Nach jedem Zug den aktuellen Spieler wechseln
        if self.current_player == 'x':
            self.current_player = 'o'
        else:
            self.current_player = 'x'

    def check_winning_conditions(self):
        if len(self.get_all_possible_moves()) == 0:
            if self.current_player == 'x':
                return 'o'
            else:
                return 'x'
        if self.end_game[0]:
            return self.end_game[1]
        return None

    def get_movable_figures(self):
        possible_moves = self.get_all_possible_moves()
        movable_figures = [i[0] for i in possible_moves]
        movable_figures_no_dupe = []
        for i in movable_figures:
            i = tuple(i)
            movable_figures_no_dupe.append(i)
        return list(dict.fromkeys(movable_figures_no_dupe))

    def move_computer_random(self):
        print('Bot mit ' + self.current_player + ' am Zug')

        possible_moves = self.get_all_possible_moves()
        print("Liste möglicher Züge: ")
        print(possible_moves)

        self.makeMove(random.choice(possible_moves))

    def get_possible_moves_clicked(self, row, col):
        if self.current_player == "o":
            enemy_player = "x"
        else:
            enemy_player = "o"
        
        if self.current_player == 'x':
            neighbours = [[1, -1], [1, 0], [1, 1]]
        else:
            neighbours = [[-1, -1], [-1, 0], [-1, 1]]
        
        possibleMoves = []

        if self.board[row][col].lower() == self.current_player:
            for index in range(3):
                new_row = row + neighbours[index][0]
                new_col = col + neighbours[index][1]
                if 0 <= new_row < len(self.board) and 0 <= new_col < len(self.board[row]):
                    if index == 1 and self.board[new_row][new_col] == ' ':
                        possibleMoves.append([[row, col], [new_row, new_col]])
                    if index == 0 and self.board[new_row][new_col] == enemy_player:
                        possibleMoves.append([[row, col], [new_row, new_col]])
                    if index == 2 and self.board[new_row][new_col] == enemy_player:
                        possibleMoves.append([[row, col], [new_row, new_col]])
        return possibleMoves

    def get_all_possible_moves(self):
        if self.current_player == "o":
            enemy_player = "x"
        else:
            enemy_player = "o"
        
        if self.current_player == 'x':
            neighbours = [[1, -1], [1, 0], [1, 1]]
        else:
            neighbours = [[-1, -1], [-1, 0], [-1, 1]]
        
        possibleMoves = []
       
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col].lower() == self.current_player:
                    for index in range(3):
                        new_row = row + neighbours[index][0]
                        new_col = col + neighbours[index][1]
                        if 0 <= new_row < len(self.board) and 0 <= new_col < len(self.board[row]):
                            if index == 1 and self.board[new_row][new_col] == ' ':
                                possibleMoves.append([[row, col], [new_row, new_col]])
                            if index == 0 and self.board[new_row][new_col] == enemy_player:
                                possibleMoves.append([[row, col], [new_row, new_col]])
                            if index == 2 and self.board[new_row][new_col] == enemy_player:
                                possibleMoves.append([[row, col], [new_row, new_col]])
        return possibleMoves
                                
    def getDisplayname(self):
        return self.displayname

    def getStartKI(self):
        return self.startKI

    def getStartPlayer(self):
        return self.startPlayer
    
    def getTurn(self):
        if self.current_player == 'x':
            return True
        else:
            return False

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