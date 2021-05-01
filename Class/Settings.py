class Settings:

    def __init__(self, dame = 5, ttt = 5, bauernschach = 5, colorKi = "#ffff00", colorPlayer = "#ff0000"):
        self.depth = dict()
        self.depth["Dame"] = dame
        self.depth["Tic Tac Toe"] = ttt
        self.depth["Bauernschach"] = bauernschach
        self.colorKi = colorKi
        self.colorPlayer = colorPlayer

    def getDepth(self, index):
        return self.depth[index]

    def getColorKi(self):
        return self.colorKi

    def getColorPlayer(self):
        return self.colorPlayer
