import tkinter as tk
from tkinter import *
from tkinter import messagebox
from User import User
from Database import Database


class PageHandler(tk.Tk):

    user = "{USERNAME}"

    runningGames = []
    runningLayouts = []

    board = None

    def __init__(self):
        super().__init__()

        self.db = Database()


        self.resizable(False,False)
        self.geometry("{}x{}".format(330,200))
        self.title("UNTERSTUFEN PROJEKT")
        self.protocol("WM_DELETE_WINDOW", self.__killAll)

        self.user = User()

        self.grid_columnconfigure(1, minsize=100)
        self.grid_columnconfigure(2, minsize=100)
        self.grid_columnconfigure(3, minsize=100)
        self.grid_rowconfigure(4, minsize=100)

        self.grid_rowconfigure(2, minsize=40)

        self.loginPage()


    def __killAll(self):
        exit()

    def login(self):
        pw = self.passwortEntry.get()
        username = self.usernameEntry.get()

        if self.db.login(username, pw) is not None: self.user = self.db.login(username, pw)
        else: return

        self.gamemodePage()

    def reg(self):
        pw = self.passwortEntry.get()
        username = self.usernameEntry.get()

        self.db.insertNewUser(username, pw)

        self.loginPage()

    def registerPage(self):
        self.resetWindow()

        self.title("REGESTRIEREN")

        self.mainText = tk.Label(self, text="REGISTRIEREN")
        self.mainText.grid(row=1, column=2)

        self.usernameText = tk.Label(self, text="USERNAME : ")
        self.usernameText.grid(row=2, column=1)
        self.usernameEntry = tk.Entry(self)
        self.usernameEntry.grid(row=2, column=2)

        self.passwortText = tk.Label(self, text="PASSWORT : ")
        self.passwortText.grid(row=3, column=1)
        self.passwortEntry = tk.Entry(self, show="*")
        self.passwortEntry.grid(row=3, column=2)

        self.backButton = tk.Button(self, text="<---", command=self.loginPage)
        self.backButton.grid(row=4, column=1)

        self.registerButton = tk.Button(self, text="REGISTRIEREN", command=self.reg)
        self.registerButton.grid(row=4, column=2)

    def loginPage(self):
        self.resetWindow()

        self.title("LOGIN")

        self.mainText = tk.Label(self, text="LOGIN")
        self.mainText.grid(row=1, column=2)

        self.usernameText = tk.Label(self, text="USERNAME : ")
        self.usernameText.grid(row=2, column=1)

        self.usernameEntry = tk.Entry(self)
        self.usernameEntry.grid(row=2, column=2)

        self.passwortText = tk.Label(self, text="PASSWORT : ")
        self.passwortText.grid(row=3, column=1)

        self.passwortEntry = tk.Entry(self, show="*")
        self.passwortEntry.grid(row=3, column=2)

        self.loginButton = tk.Button(self, text="LOGIN", command=self.login)
        self.loginButton.grid(row=4, column=2)

        self.noLoginButton = tk.Button(self, text="OHNE LOGIN", command=self.gamemodePage)
        self.noLoginButton.grid(row=4, column=1)

        self.registerButton = tk.Button(self, text="REGISTRIEREN", command=self.registerPage)
        self.registerButton.grid(row=4, column=3)

    def gamemodePage(self):
        self.resetWindow()

        self.title("Angemeldet als {}".format(self.user.getUsername()))

        self.mainText = tk.Label(self, text="SPIELMODUS")
        self.mainText.grid(row=0, column=2)

        self.bauernschachButton = tk.Button(self, text="BAUERNSCHACH", command= lambda: self.startLayout("baurenschach"), width = 15)
        self.bauernschachButton.grid(row=1, column=2)

        self.dameButton = tk.Button(self, text="DAME", command= lambda: self.startLayout("dame"), width = 15)
        self.dameButton.grid(row=2, column=2)

        self.tictactoeButton = tk.Button(self, text="TIC-TAC-TOE", command= lambda: self.startLayout("ttt"), width = 15)
        self.tictactoeButton.grid(row=3, column=2)

        self.backButton = tk.Button(self, text="<---", command=self.loginPage)
        self.backButton.grid(row=4, column=1)

        self.einstellungenButton = tk.Button(self, text="Einstellungen", command=self.void)
        self.einstellungenButton.grid(row=4, column=3)

        self.einstellungenButton.config(state="disabled")

    def resetWindow(self):
        for child in self.winfo_children():
            child.destroy()

    def void(self):
        print("VOID")

    def noLogin(self, game):
        self.gamemodePage()

    def startLayout(self, game):
        #self.backButton.config(state="disabled")
        #self.tictactoeButton.config(state="disabled")
        #self.dameButton.config(state="disabled")
        #self.bauernschachButton.config(state="disabled")
        from Layout import Layout
        if game == "dame":
            from Dame import Dame
            game = Dame()
            layout = Layout(game, self.user, self.db)
        elif game == "ttt":
            from TicTacToe import TicTacToe
            game = TicTacToe()
            layout = Layout(game, self.user, self.db, True)
        elif game == "baurenschach":
            from pawnchess import PawnChess
            game = PawnChess()
            layout = Layout(game, self.user)

        print(layout)
        print(game)
        #self.runningLayouts[-1].protocol("WM_DELETE_WINDOW", lambda arg=self.runningLayouts[-1]: self.__on_closingg(arg))
        layout.mainloop()

        

    def __on_closing(self, win):
        self.backButton.config(state="active")
        self.tictactoeButton.config(state="active")
        self.dameButton.config(state="active")
        self.bauernschachButton.config(state="active")
        self.einstellungenButton.config(state="active")

        self.win.destroy()
        self.win = None

def main():
    gui = PageHandler()

    gui.mainloop()

main()