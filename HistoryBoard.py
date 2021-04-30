class HistoryBoard():

    def __init__(self):
        self.fullArr = [None, None]
        self.locationKI = []
        self.locationUser = []

    def setLocation(self, ki, user):
        self.locationKI.append(ki.copy())
        print(self.locationKI)
        self.locationUser.append(user.copy())

    def mergeArrays(self):
        self.fullArr[0] = self.locationKI
        self.fullArr[1] = self.locationUser

        #print(self.locationKI)
        
    def getAllRounds(self):
        self.mergeArrays()
        return self.fullArr

    def reset(self):
        self.fullArr = [None, None]
        self.locationKI = []
        self.locationUser = []