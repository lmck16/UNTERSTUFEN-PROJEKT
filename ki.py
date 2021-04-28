from random import randrange

class KI:
    
    def __init__(self, spiel):
        self.spiel = spiel

    def getMove(self):
        if self.spiel.displayname == "ttt":
            return self.kiTurn()

    def kiTurn(self):
        self.spiel.genBoard()
        brd = self.spiel.getBoard()
        loop = True
        while loop:
            row = randrange(len(self.spiel.board))
            col = randrange(len(self.spiel.board))

            print(brd)

            if self.__isInArray(self.spiel.getPositionPlayer(), row, col) is False and self.__isInArray(self.spiel.getPositionKI(), row, col) is False:
                print(brd[row][col])
                print("ROW {} und COL {} ARE FREE KAPP".format(row, col))
                loop = False
                
            print("{}, {}".format(row, col))

        print("{}, {}".format(row, col))   
        return [row,col]

    def __isInArray(self, arr, row, col):
        print(arr)
        for i in range(len(arr)):
            if arr[i][0] == col and arr[i][1] == row:
                return True
        return False