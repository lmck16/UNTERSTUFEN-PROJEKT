import tkinter as tk
from tkinter import *
from Database import Database
from ast import literal_eval

class HistoryLayout(tk.Tk):

    n=6

    startRow = 6

    def __init__(self, user):
        super().__init__()
        self.resizable(False,False)

        self.user = user

        self.db = Database()

        self.colours = ["#fefefe", "#7f7f7f"]

        self.canvas = tk.Canvas(self, width=int(self.n*90), height=int(self.n*90))
        self.canvas.grid(row=0, column=0, columnspan=6, rowspan=6)

        #self.geometry("{}x{}".format(500,500))

        #self.grid_columnconfigure(1, minsize=100)
        self.grid_columnconfigure(2, minsize=100)
        self.grid_columnconfigure(3, minsize=100)
        self.grid_columnconfigure(4, minsize=100)
        #self.grid_columnconfigure(5, minsize=100)

        self.btn = []

        self.ttt = self.db.getGameSession(self.user.getId(), "Tic Tac Toe")



        self.title("Spielverläufe")
        self.printButtons()
        self.board = [[None for row in range(self.n)] for col in range(self.n)]
        self.figures = [[None for row in range(self.n)] for col in range(self.n)]
        self.drawboard()

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

    def updateField(self, val):
        self.resetBoard()
        print("{} //// {}".format(self.currArr[0][int(val)], self.currArr[1][int(val)]))
        self.initFigures(self.currArr[0][int(val)], self.currArr[1][int(val)])

    def setSessionID(self, id):
        self.resetBoard()
        self.currArr = literal_eval(self.ttt[id][2])
        print(len(self.currArr[0]))
        print(self.currArr[0][4])
        self.mainSlider = Scale(self, from_=0, to=len(self.currArr[0])-1, orient=HORIZONTAL, command=self.updateField)
        self.mainSlider.grid(row=self.startRow, column=4)

    def printButtons(self):
        self.mainText = tk.Label(self, text="BAUERNSCHACH")
        self.mainText.grid(row=self.startRow, column=1)

        for i in range(len(self.ttt)):
            self.btn.append(tk.Button(self, text="BAUERNSCHACH {}".format(i+1), command= lambda: self.setSessionID(i), width = 15))
            self.btn[i].grid(row=self.startRow + i+2, column=1)

        #self.mainText = tk.Label(self, text="DAME")
        #self.mainText.grid(row=self.startRow, column=2)

        #for i in range(2, 10):
       #    self.btn = tk.Button(self, text="DAME {}".format(i), command= lambda: self.setSessionID("baurenschach"), width = 15)
       #     self.btn.grid(row=self.startRow + i, column=2)

        #self.mainText = tk.Label(self, text="TICTACTOE")
        #self.mainText.grid(row=self.startRow, column=3)

       # for i in range(2, 10):
       #     self.btn = tk.Button(self, text="TTT {}".format(i), command= lambda: self.setSessionID("baurenschach"), width = 15)
       #     self.btn.grid(row=self.startRow+i, column=3)

    def resetWindow(self):
        for child in self.winfo_children():
            child.destroy()

    def initFigures(self, locationKI, locationUser, colorKI = "#ffff00", colorUser = "#ff0000"):
        self.colorUser = colorUser
        self.colorKI = colorKI
        self.locationKI = locationKI
        self.locationUser = locationUser

        self.__setFigures(self.locationKI, self.colorKI)
        self.__setFigures(self.locationUser, self.colorUser)

    def __setFigures(self, location, color):
        for i in range(len(location)):
            self.__drawFigures(location[i][1], location[i][0], color)

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

    def resetBoard(self, noFigures = False):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] is not None:
                    self.canvas.delete(self.board[i][j])
        self.drawboard()


#x = HistoryLayout()
#x.mainloop()

