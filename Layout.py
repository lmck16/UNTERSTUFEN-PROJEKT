import tkinter as tk
from ki import KI
from tkinter import messagebox
from HistoryBoard import HistoryBoard

class Layout(tk.Tk):

    n=6
    winsKI = 0
    winsPlayer = 0

    def __init__(self, spiel, user, db, ttt = False):
        super().__init__()

        self.db = db

        self.hrBoard = HistoryBoard()

        self.colours = ["#fefefe", "#7f7f7f"]

        self.locked = False

        self.locationKI = []
        self.locationUser = []
        self.colorKI = "#ffff00"
        self.colorUser = "#ff0000"

        self.lockedI = 0
        self.lockedJ = 0

        self.turn = True # TRUE = USER / FALSE = KI

        self.end = False


        self.spiel = spiel

        self.user = user

        self.ttt = ttt

        if self.ttt: self.colours[1] = self.colours[0]

        self.KI = KI(self.spiel)

        self.resizable(False,False)
        self.setScoreToDisplay(self.winsKI,self.winsPlayer)
        self.geometry("{}x{}".format(int((self.n*90)), int((self.n*90)+90)))

        self.canvas = tk.Canvas(self, width=int(self.n*90), height=int(self.n*90))
        self.canvas.grid(row=0, column=0, columnspan=6, rowspan=6)

        self.restartButton = tk.Button(self, text="{} neustarten".format(self.spiel.getDisplayname()), command=self.newBoard)
        self.restartButton.grid(row=7, column=0)

        self.board = [[None for row in range(self.n)] for col in range(self.n)]
        self.figures = [[None for row in range(self.n)] for col in range(self.n)]
        self.fieldObj = [[None for row in range(self.n)] for col in range(self.n)]
        self.field = [[None for row in range(self.n)] for col in range(self.n)]

        self.drawboard()
        self.initFigures(self.spiel.getStartKI(), self.spiel.getStartPlayer())


    def setScoreToDisplay(self, ki, user):
        self.title("{} - PUNKTE KI ({}) || PUNKTE {} ({})".format(self.spiel.getDisplayname(), ki, self.user.getUsername(), user))

    def drawboard(self):
        from itertools import cycle
        for col in range(self.n):
            color = cycle(self.colours[::-1] if not col % 2 else self.colours)
            for row in range(self.n):
                x1 = col * 90
                y1 = (5-row) * 90
                x2 = x1 + 90
                y2 = y1 + 90
                self.board[row][col] = self.canvas.create_rectangle(x1, y1, x2, y2, fill=next(color), tags=f"tile{col}{row}")
                self.canvas.tag_bind(f"tile{col}{row}","<Button-1>", lambda e, i=col, j=row: self.__keyDown(e,i,j))

    def highlightField(self, j, i, color = "#3bbbea"):
        self.canvas.itemconfig(self.board[j-1][i-1], fill=color)
        
    def highlightMultipleFields(self, coords, color = "#3bbbea"):
        for i in range(len(coords)):
            self.highlightField(coords[i][0]+1, coords[i][1]+1, color)

    def highlightFigure(self, j, i, color = "#3bbbea"):
        self.canvas.itemconfig(self.figures[j][i], fill=color)

    def highlightMultipleFigures(self, coords, color = "#800000"):
        for i in range(len(coords)):
            self.highlightFigure(coords[i][0], coords[i][1], color)

    def initFigures(self, locationKI, locationUser, colorKI = "#ffff00", colorUser = "#ff0000"):
        self.colorUser = colorUser
        self.colorKI = colorKI
        self.locationKI = locationKI
        self.locationUser = locationUser


        self.hrBoard.setLocation(self.locationKI, self.locationUser)
        self.hrBoard.getAllRounds()
        self.__setFigures(self.locationKI, self.colorKI)
        self.__setFigures(self.locationUser, self.colorUser)

    def removeAllFigures(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.figures[i][j] is not None:
                    self.canvas.delete(self.figures[i][j])

    def newBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] is not None:
                    self.canvas.delete(self.board[i][j])
        self.removeAllFigures()
        self.spiel.newGame()
        self.drawboard()
    
    def resetBoard(self, noFigures = False):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] is not None:
                    self.canvas.delete(self.board[i][j])
        self.drawboard()
        if noFigures is False: self.initFigures(self.spiel.getPositionKI(), self.spiel.getPositionPlayer(), self.colorKI, self.colorUser)

        #self.locked = False
        #self.turn = not self.turn

    def __setFigures(self, location, color):
        for i in range(len(location)):
            self.__drawFigures(location[i][1], location[i][0], color)
            
    def __refreshDraw(self):
        user = []
        ki = []

        for i in range(self.n):
            for j in range(self.n):
                if self.field[i][j] == "O":
                    user.append([j,i])
                elif self.field[i][j] == "X":
                    ki.append([j,i])
        self.removeAllFigures()
        print(ki)
        self.initFigures(ki, user)
        
    def __drawFigures(self, i, j, color):
        loc = self.canvas.coords(self.board[j][i])

        newCoords = [
            loc[0]+20,
            loc[1]+20,
            loc[2]-20,
            loc[3]-20
        ]

        if color == self.colorKI: 
            self.figures[j][i] = self.canvas.create_rectangle(newCoords,fill=color, tags=f"tile{i}{j}")
        else:
            self.figures[j][i] = self.canvas.create_oval(newCoords,fill=color, tags=f"tile{i}{j}")
        
        self.canvas.tag_bind(f"tile{i}{j}","<Button-1>", lambda e, i=i, j=j, color=color: self.__figurePressed(e,i,j, color))
        if self.ttt is False:
            self.highlightMultipleFigures(self.spiel.get_movable_figures(), "#800000")
        
    def moveFigure(self, oldI, oldJ, newI, newJ):
        self.__genCurrentField()
        self.field[oldI-1][oldJ-1] = self.field[newI-1][newJ-1]
        self.__refreshDraw()
        

    def gameHandler(self, figureJ, figureI, moveJ, moveI):
        print("MOVED ({}/{}) to ({}/{})".format(figureJ, figureI, moveJ, moveI))
        if self.ttt: self.spiel.makeMove(moveJ, moveI)
        else: self.spiel.makeMove([[figureJ, figureI], [moveJ, moveI]])

    def __isInArray(self, arr, i, j):
        for x in range(len(arr)):
            if arr[x][0] == i and arr[x][1] == j:
                return True
        return False

    def __figurePressed(self, event, i, j, color):
        print ("__figurePressed ({}/{})".format(j, i))
        self.resetBoard()
        if self.ttt is False:
            if self.turn is True:
                if self.__isInArray(self.spiel.getPositionPlayer(), j, i) and self.__isInArray(self.spiel.get_movable_figures(), j, i):
                    print("PLAYER : {}".format(self.spiel.getPositionPlayer()))
                    self.highlightMultipleFields(self.spiel.get_possible_moves_clicked(j, i))

                    #return

                    self.canvas.itemconfig(self.figures[j][i], fill="#40ff00")

                    self.lockedI = i
                    self.lockedJ = j

                    self.locked = True

    def __keyDown(self, event, i, j):
        print ("__keyDown ({}/{})".format(j, i))

        if self.ttt:
            self.gameHandler(self.lockedJ, self.lockedI, j, i)
            self.resetBoard()

            self.__checkWin()

            if self.spiel.getTurn() is False:
                tmp = self.KI.kiTurn()
                self.gameHandler(self.lockedJ, self.lockedI, tmp[1], tmp[0])
                self.resetBoard()

            self.__checkWin()

            self.highlightField(j+1, i+1)
        elif self.locked:
            if self.__isInArray(self.spiel.get_possible_moves_clicked(self.lockedJ, self.lockedI), j, i):
                self.locked = False

                self.gameHandler(self.lockedJ, self.lockedI, j, i)
                self.resetBoard()

                self.highlightField(j + 1, i + 1)
                if self.spiel.getTurn() is False:
                    self.KI.move_computer_random()
                    self.resetBoard()




    def __checkWin(self):
        if self.spiel.checkWin():
            if self.spiel.getTurn() is False:
                self.winsPlayer = self.winsPlayer + 1
                messagebox.showinfo("GEWONNEN", "SIE HABEN GEWONNEN")
                if self.user.getId() > 0: self.db.insertGameSession("user", self.hrBoard.getAllRounds(), self.user.getId())
            else:
                self.winsKI = self.winsKI + 1
                messagebox.showinfo("VERLOREN", "SIE HABEN VERLOREN")
                if self.user.getId() > 0: self.db.insertGameSession("ki", self.hrBoard.getAllRounds(), self.user.getId())
            self.hrBoard.reset()
            self.setScoreToDisplay(self.winsKI,self.winsPlayer)
            self.resetBoard(True)
            self.spiel.newGame()
            return

    def __genCurrentField(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.figures[i][j] is None and self.board[i][j] is not None:
                    self.fieldObj[i][j] = self.board[i][j]
                    self.field[i][j] = "_"

                    print("FIELD ({}/{} - {}) EMPTY".format(i+1, j+1, self.board[i][j]))
                else:
                    self.fieldObj[i][j] = self.figures[i][j]
                    color = self.canvas.itemcget(self.figures[i][j], "fill")
                    if color == "#ff0000":
                        self.field[i][j] = "X"
                    else:
                        self.field[i][j] = "O"

                    print("FIELD ({}/{} - {}) {}".format(i+1, j+1, self.figures[i][j], color))

    def getField(self):
        self.__genCurrentField()
        return self.field

    def getSpecificField(self, i, j):
        self.__genCurrentField()
        return self.field[i-1][j-1]

    def drawFieldToConsole(self):
        self.__genCurrentField()
        for i in range(self.n):
            print("{}{}{}{}{}{}".format(
            self.field[i][5],
            self.field[i][4],
            self.field[i][3],
            self.field[i][2],
            self.field[i][1],
            self.field[i][0]))




def main():

    new_game = Dame()
    new_game.print_board()

    board = Layout(new_game)
    board.drawboard()

    board.initFigures(new_game.startKI, new_game.startPlayer)
    board.drawFieldToConsole()


    board.mainloop()


#main()