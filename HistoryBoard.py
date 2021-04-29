class HistoryBoard():

    def __init__(self):
        self.fullArr = [None, None]
        self.locationKI = []
        self.locationUser = []

    def setLocation(self, ki, user):
        self.locationKI.append(ki)
        self.locationUser.append(user)

    def mergeArrays(self):
        self.fullArr[0] = self.locationKI
        self.fullArr[1] = self.locationUser
        
    def getAllRounds(self):
        self.mergeArrays()
        return self.fullArr

    def reset(self):
        self.fullArr = [None, None]
        self.locationKI = []
        self.locationUser = []