import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from Class.User import User
from Class.Database import Database
from Class.Settings import Settings


class PageHandler(tk.Tk):

    def __init__(self):
        super().__init__()

        self.db = Database()
        self.userSettings = Settings()

        self.colorKi = {}
        self.colorPlayer = {}

        self.colorKi['hex'] = self.userSettings.getColorKi()
        self.colorPlayer['hex'] = self.userSettings.getColorPlayer()


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

        self.userSettings = self.db.getUserSettings(self.user)

        self.gamemodePage()

    def reg(self):
        pw = self.passwortEntry.get()
        username = self.usernameEntry.get()

        if self.db.insertNewUser(username, pw) is False: messagebox.showinfo("USER EXISTIERT BEREITS", "USER EXISTIERT BEREITS")
        else: 
            self.loginPage()

    def settingsPage(self):
        self.resetWindow()
        self.geometry("{}x{}".format(330,300))
        self.grid_rowconfigure(7, minsize=100)
        self.grid_rowconfigure(4, minsize=0)

        self.title("EINSTELLUNGEN")

        self.mainText = tk.Label(self, text="EINSTELLUNGEN", font='Helvetica 18 bold')
        self.mainText.grid(row=1, column=2)

        self.tttText = tk.Label(self, text="Tic Tac Toe Tiefe : ")
        self.tttText.grid(row=2, column=1)
        self.tttSlider = Scale(self, from_=5, to=15, orient=HORIZONTAL)
        self.tttSlider.grid(row=2, column=2)
        self.tttSlider.set(self.userSettings.getDepth("Tic Tac Toe"))

        self.dameText = tk.Label(self, text="Dame Tiefe : ")
        self.dameText.grid(row=3, column=1)
        self.dameSlider = Scale(self, from_=5, to=15, orient=HORIZONTAL)
        self.dameSlider.grid(row=3, column=2)
        self.dameSlider.set(self.userSettings.getDepth("Dame"))

        self.bauernschachText = tk.Label(self, text="Bauernschach Tiefe: ")
        self.bauernschachText.grid(row=4, column=1)
        self.bauernschachSlider = Scale(self, from_=5, to=15, orient=HORIZONTAL)
        self.bauernschachSlider.grid(row=4, column=2)
        self.bauernschachSlider.set(self.userSettings.getDepth("Bauernschach"))


        self.colorKText = tk.Label(self, text="Farbe KI: ")
        self.colorKText.grid(row=5, column=1)
        self.colorKiButton = tk.Button(self, width = 15, bg=self.userSettings.getColorKi(), command = self.chooseColorKI)
        self.colorKiButton.grid(row=5, column=2)

        self.colorPlayerText = tk.Label(self, text="Farbe Spieler: ")
        self.colorPlayerText.grid(row=6, column=1)
        self.colorPlayerButton = tk.Button(self, width = 15, bg=self.userSettings.getColorPlayer(), command = self.chooseColorPlayer)
        self.colorPlayerButton.grid(row=6, column=2)

        self.backButton = tk.Button(self, text="<---", command=self.gamemodePage)
        self.backButton.grid(row=7, column=1)

        self.speichernButton = tk.Button(self, text="SPEICHERN", command=self.saveSettings)
        self.speichernButton.grid(row=7, column=2)

    def statsPage(self, game):
        self.resetWindow()
        self.geometry("{}x{}".format(360,500))
        self.grid_rowconfigure(4, minsize=0)
        
        table = self.db.getGameStats(game)

        self.title("Statistiken {}".format(game))

        self.mainText = tk.Label(self, text=game, font='Helvetica 18 bold')
        self.mainText.grid(row=1, column=2)

        self.backButton = tk.Button(self, text="<---", command=self.gamemodePage)
        self.backButton.grid(row=1, column=1)

        self.headCol1 = tk.Label(self, text="Spieler")
        self.headCol1.grid(row=2, column=1)

        self.headCol2 = tk.Label(self, text="Gewinner")
        self.headCol2.grid(row=2, column=2)

        self.headCol3 = tk.Label(self, text="Tiefe")
        self.headCol3.grid(row=2, column=3)

        for row in range(3, len(table) + 3):
            self.statTxT = tk.Label(self, text=table[row-3][1])
            self.statTxT.grid(row=row, column=1)

            if table[row-3][0] == "user": 
                self.statTxT = tk.Label(self, text="Spieler")
            else:
                self.statTxT = tk.Label(self, text="KI")
            self.statTxT.grid(row=row, column=2)

            self.statTxT = tk.Label(self, text=table[row-3][2])
            self.statTxT.grid(row=row, column=3)

    def chooseColorKI(self):
        self.colorKi['rgb'], self.colorKi['hex'] = colorchooser.askcolor(title ="Wähle eine Farbe")
        self.colorKiButton.configure(bg=self.colorKi['hex'])
        print(self.colorKi['hex'])

    def chooseColorPlayer(self):
        self.colorPlayer['rgb'], self.colorPlayer['hex'] = colorchooser.askcolor(title ="Wähle eine Farbe")
        self.colorPlayerButton.configure(bg=self.colorPlayer['hex'])
        print(self.colorKi['hex'])

    def saveSettings(self):
        self.userSettings = Settings(
            self.dameSlider.get(),
            self.tttSlider.get(),
            self.bauernschachSlider.get(),
            self.colorKi['hex'],
            self.colorPlayer['hex']
        )

        self.db.updateUserSettings(self.userSettings, self.user)

        self.gamemodePage()

    def registerPage(self):
        self.resetWindow()

        self.title("REGESTRIEREN")

        self.mainText = tk.Label(self, text="REGISTRIEREN", font='Helvetica 18 bold')
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

        self.mainText = tk.Label(self, text="LOGIN", font='Helvetica 18 bold')
        self.mainText.grid(row=1, column=2)

        self.usernameText = tk.Label(self, text="USERNAME : ")
        self.usernameText.grid(row=2, column=1)

        self.usernameEntry = tk.Entry(self)
        self.usernameEntry.grid(row=2, column=2)
        if self.user.getId() > 0: 
            self.usernameEntry.insert(0, self.user.getUsername())
            self.usernameEntry.config(state='disabled') 

        self.passwortText = tk.Label(self, text="PASSWORT : ")
        self.passwortText.grid(row=3, column=1)

        self.passwortEntry = tk.Entry(self, show="*")
        self.passwortEntry.grid(row=3, column=2)
        if self.user.getId() > 0: 
            self.passwortEntry.insert(0, "XXXXXXXXXXX")
            self.passwortEntry.config(state='disabled') 

        if self.user.getId() > 0: 
            self.loginButton = tk.Button(self, text="ABMELDEN", command=self.logout)
            self.loginButton.grid(row=4, column=2)
            self.noLoginButton = tk.Button(self, text="SPIELE", command=self.gamemodePage)
            self.noLoginButton.grid(row=4, column=1)
        else:
            self.loginButton = tk.Button(self, text="LOGIN", command=self.login)
            self.loginButton.grid(row=4, column=2)
            self.noLoginButton = tk.Button(self, text="OHNE LOGIN", command=self.gamemodePage)
            self.noLoginButton.grid(row=4, column=1)

        self.registerButton = tk.Button(self, text="REGISTRIEREN", command=self.registerPage)
        self.registerButton.grid(row=4, column=3)

    def logout(self):
        self.user = User()
        self.loginPage()

    def gamemodePage(self):
        self.resetWindow()

        self.title("Angemeldet als {}".format(self.user.getUsername()))

        self.mainText = tk.Label(self, text="SPIELMODUS")
        self.mainText.grid(row=0, column=2)

        self.bauernschachButton = tk.Button(self, text="BAUERNSCHACH", command= lambda: self.startLayout("bauernschach"), width = 15)
        self.bauernschachButton.grid(row=1, column=2)

        self.dameButton = tk.Button(self, text="DAME", command= lambda: self.startLayout("dame"), width = 15)
        self.dameButton.grid(row=2, column=2)

        self.tictactoeButton = tk.Button(self, text="TIC-TAC-TOE", command= lambda: self.startLayout("ttt"), width = 15)
        self.tictactoeButton.grid(row=3, column=2)

        if self.user.getId() > 0:
            self.historyButton = tk.Button(self, text="HISTORY", command= lambda: self.startLayout("history"), width = 15)
            self.historyButton.grid(row=4, column=2)

        self.backButton = tk.Button(self, text="<---", command=self.loginPage)
        self.backButton.grid(row=4, column=1)

        if self.user.getId() > 0:
            self.einstellungenButton = tk.Button(self, text="Einstellungen", command=self.settingsPage)
            self.einstellungenButton.grid(row=4, column=3)

            self.einstellungenButton = tk.Button(self, text="Stats", command= lambda: self.statsPage("Bauernschach"))
            self.einstellungenButton.grid(row=1, column=3)

            self.einstellungenButton = tk.Button(self, text="Stats", command= lambda: self.statsPage("Dame"))
            self.einstellungenButton.grid(row=2, column=3)

            self.einstellungenButton = tk.Button(self, text="Stats", command= lambda: self.statsPage("Tic Tac Toe"))
            self.einstellungenButton.grid(row=3, column=3)

    def resetWindow(self):
        self.geometry("{}x{}".format(330,200))
        self.grid_rowconfigure(7, minsize=0)
        self.grid_rowconfigure(4, minsize=100)
        for child in self.winfo_children():
            child.destroy()

    def void(self):
        print("VOID")

    def noLogin(self, game):
        self.gamemodePage()

    def startLayout(self, lay):
        from Class.Layout import Layout
        if lay == "dame":
            from Class.Dame import Dame
            game = Dame()
            layout = Layout(game, self.user, self.db, self.userSettings)
        elif lay == "ttt":
            from Class.TicTacToe import TicTacToe
            game = TicTacToe()
            layout = Layout(game, self.user, self.db, self.userSettings, True)
        elif lay == "bauernschach":
            from Class.Pawnchess import PawnChess
            game = PawnChess()
            layout = Layout(game, self.user, self.db, self.userSettings)
        elif lay == "history":
            from Class.HistoryLayout import HistoryLayout
            layout = HistoryLayout(self.user, self.userSettings)

        layout.mainloop()
