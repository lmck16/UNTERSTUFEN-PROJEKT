import sqlite3
from uuid import uuid4
from User import User

class Database():

    databaseFile = "data.db"

    def start(self):
        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = 'CREATE TABLE IF NOT EXISTS "gameSession"  ("gameSession_id"	TEXT NOT NULL UNIQUE,"winner"	INTEGER NOT NULL,"board"	INTEGER NOT NULL,"user_id"	INTEGER NOT NULL,"game"	INTEGER NOT NULL,PRIMARY KEY("gameSession_id"));'

        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()

        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = 'CREATE TABLE IF NOT EXISTS "user" ( "user_id"	INTEGER NOT NULL UNIQUE, "username"	TEXT NOT NULL, "password"	TEXT NOT NULL,PRIMARY KEY("user_id" AUTOINCREMENT));'

        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()

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

        sql = "SELECT * FROM gameSession WHERE user_id = '{}' AND game = '{}' LIMIT 10".format(usrId, dpName)

        self.cursor.execute(sql)

        records = self.cursor.fetchall()
        
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
