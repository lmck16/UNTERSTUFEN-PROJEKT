class User():

    def __init__(self, username = "Mustermann", password = "", id = -1):

        self.id = id
        self.password = password
        self.username = username 

    def getUsername(self):
        return self.username

    def getId(self):
        return self.id