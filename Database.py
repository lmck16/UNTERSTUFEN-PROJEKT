import sqlite3
from uuid import uuid4
from User import User

class Database():

    databaseFile = "data.db"

    #def __init__(self): 
        

    def login(self, username, password):
        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = "SELECT * FROM user WHERE username = '{}' AND password = '{}' limit 1".format(username, password)

        self.cursor.execute(sql)

        records = self.cursor.fetchall()
        for row in records:
            return User(username, password, row[0])

        self.cursor.close()
        self.connection.commit()
        self.connection.close()

    def insertNewUser(self, username, password):
        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = "INSERT INTO user VALUES(NULL, '{}', '{}')".format(username, password)

        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()
    
    def getGameSession(self, usrId, dpName):
        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = "SELECT * FROM gameSession WHERE user_id = '{}' AND game = '{}'".format(usrId, dpName)

        self.cursor.execute(sql)

        records = self.cursor.fetchall()
        #for row in records:
        #    print(row[0])
        #    print("----------------")

        self.cursor.close()
        self.connection.commit()
        self.connection.close()

        return records

    def insertGameSession(self, winner, board, usrId, dpName):
        session = uuid4()   

        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = "INSERT INTO gameSession VALUES('{}', '{}', '{}', '{}', '{}')".format(session, winner, board, usrId, dpName)

        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close() 
