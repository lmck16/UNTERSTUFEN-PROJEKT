import tkinter as tk
from tkinter import *
from tkinter import messagebox



class PageHandler(tk.Tk):

    user = "{USERNAME}"

    runningGames = []

    board = None

    def __init__(self):
        super().__init__()
        self.resizable(False,False)
        self.geometry("{}x{}".format(330,200))
        self.title("UNTERSTUFEN PROJEKT")
        self.protocol("WM_DELETE_WINDOW", self.__killAll)

        self.grid_columnconfigure(1, minsize=100)
        self.grid_columnconfigure(2, minsize=100)
        self.grid_columnconfigure(3, minsize=100)
        self.grid_rowconfigure(4, minsize=100)

        self.grid_rowconfigure(2, minsize=40)

        self.loginPage()


    def __killAll(self):
        if self.board is not None:
            self.board.destroy()
        self.destroy()

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
        self.passwortEntry = tk.Entry(self)
        self.passwortEntry.grid(row=3, column=2)

        self.backButton = tk.Button(self, text="<---", command=self.loginPage)
        self.backButton.grid(row=4, column=1)

        self.registerButton = tk.Button(self, text="REGISTRIEREN", command=self.void)
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

        self.passwortEntry = tk.Entry(self)
        self.passwortEntry.grid(row=3, column=2)

        self.loginButton = tk.Button(self, text="LOGIN", command=self.login)
        self.loginButton.grid(row=4, column=2)

        self.noLoginButton = tk.Button(self, text="OHNE LOGIN", command=self.void)
        self.noLoginButton.grid(row=4, column=1)

        self.registerButton = tk.Button(self, text="REGISTRIEREN", command=self.registerPage)
        self.registerButton.grid(row=4, column=3)

    def settingsPage(self):
        self.resetWindow()

        self.title("EINSTELLUNGEN")

        self.mainText = tk.Label(self, text="EINSTELLUNGEN")
        self.mainText.grid(row=0, column=2)

        self.bauernschachButton = tk.Button(self, text="BAUERNSCHACH", command=self.void, width = 15)
        self.bauernschachButton.grid(row=1, column=2)

        self.dameButton = tk.Button(self, text="DAME", command=self.void, width = 15)
        self.dameButton.grid(row=2, column=2)

        self.tictactoeButton = tk.Button(self, text="TIC-TAC-TOE", command=self.void, width = 15)
        self.tictactoeButton.grid(row=3, column=2)

        self.backButton = tk.Button(self, text="<---", command=self.loginPage)
        self.backButton.grid(row=4, column=1)

        self.einstellungenButton = tk.Button(self, text="Einstellungen", command=self.void)
        self.einstellungenButton.grid(row=4, column=3)

    def gamemodePage(self):
        self.resetWindow()

        self.title("GAMEMODE")

        self.mainText = tk.Label(self, text="SPIELMODUS")
        self.mainText.grid(row=0, column=2)

        self.bauernschachButton = tk.Button(self, text="BAUERNSCHACH", command= lambda: self.startLayout("dame"), width = 15)
        self.bauernschachButton.grid(row=1, column=2)

        self.dameButton = tk.Button(self, text="DAME", command= lambda: self.startLayout("dame"), width = 15)
        self.dameButton.grid(row=2, column=2)

        self.tictactoeButton = tk.Button(self, text="TIC-TAC-TOE", command= lambda: self.startLayout("ttt"), width = 15)
        self.tictactoeButton.grid(row=3, column=2)

        self.backButton = tk.Button(self, text="<---", command=self.loginPage)
        self.backButton.grid(row=4, column=1)

        self.einstellungenButton = tk.Button(self, text="Einstellungen", command=self.void)
        self.einstellungenButton.grid(row=4, column=3)


    def all_children (self):
        _list = self.winfo_children()

        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())

        return _list

    def resetWindow(self):
        for child in self.winfo_children():
            child.destroy()


    def void(self):
        print("")

    def login(self):
        self.gamemodePage()

    def noLogin(self, game):
        self.gamemodePage()

    def startLayout(self, game):
        self.backButton.config(state="disabled")
        self.tictactoeButton.config(state="disabled")
        self.dameButton.config(state="disabled")
        self.bauernschachButton.config(state="disabled")
        self.einstellungenButton.config(state="disabled")

        from Layout import Layout
        if game == "dame":
            from Dame import Dame
            new_game = Dame()
            self.board = Layout(new_game)
        elif game == "ttt":
            from TicTacToe import TicTacToe
            new_game = TicTacToe()
            self.board = Layout(new_game, True)

        self.board.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.board.mainloop()

    def __on_closing(self):
        self.backButton.config(state="active")
        self.tictactoeButton.config(state="active")
        self.dameButton.config(state="active")
        self.bauernschachButton.config(state="active")
        self.einstellungenButton.config(state="active")

        self.board.destroy()
        self.board = None

def main():
    gui = PageHandler()

    gui.mainloop()

main()