import sqlite3
from uuid import uuid4
from User import User
from Settings import Settings

class Database():

    databaseFile = "data.db"

    def start(self):
        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = 'CREATE TABLE IF NOT EXISTS "gameSession" (	"gameSession_id"	TEXT NOT NULL UNIQUE,	"winner"	INTEGER NOT NULL,	"board"	INTEGER NOT NULL,	"user_id"	INTEGER NOT NULL,"game"	INTEGER NOT NULL,"depth"	INTEGER NOT NULL,PRIMARY KEY("gameSession_id"))'
        self.cursor.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS "user" ( "user_id"	INTEGER NOT NULL UNIQUE, "username"	TEXT NOT NULL, "password"	TEXT NOT NULL,PRIMARY KEY("user_id" AUTOINCREMENT));'
        self.cursor.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS "userSettings" ( "userSettings_id"	INTEGER NOT NULL UNIQUE, "depth_ttt" INTEGER NOT NULL, "depth_dame"	INTEGER NOT NULL,	"depth_bauernschach"	INTEGER NOT NULL,	"colorKI"	INTEGER NOT NULL,	"colorPlayer"	INTEGER NOT NULL,	"user_id"	INTEGER NOT NULL,	PRIMARY KEY("userSettings_id" AUTOINCREMENT));'
        self.cursor.execute(sql)

        sql = 'CREATE VIEW IF NOT EXISTS gameStats AS SELECT gameSession.winner, gameSession.game, gameSession.depth, user.username FROM gameSession INNER JOIN user ON gameSession.user_id=user.user_id'
        self.cursor.execute(sql)


        self.connection.commit()
        self.connection.close()

    def login(self, username, password):
        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = "SELECT * FROM user WHERE username = '{}' AND password = '{}' limit 1".format(username, password)

        self.cursor.execute(sql)
        records = self.cursor.fetchall()
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

        for row in records:
            return User(username, password, row[0])

    def getUserSettings(self, user):
        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = "SELECT * FROM userSettings WHERE user_id = '{}' limit 1".format(user.getId())

        self.cursor.execute(sql)
        records = self.cursor.fetchall()
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

        for row in records:
            return Settings(row[2], row[1], row[3], row[4], row[5])
        self.insertUserSettings(Settings(), user)
        return Settings()

    def insertUserSettings(self, settings, user):
        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = "INSERT INTO userSettings VALUES(NULL, '{}', '{}', '{}', '{}', '{}', '{}')".format(
            settings.getDepth("Tic Tac Toe"), 
            settings.getDepth("Dame"),
            settings.getDepth("Bauernschach"),
            settings.getColorKi(),
            settings.getColorPlayer(),
            user.getId())

        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()

    def updateUserSettings(self, settings, user):
        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = "UPDATE userSettings SET depth_ttt = '{}', depth_dame = '{}', depth_bauernschach = '{}', colorKI = '{}', colorPlayer = '{}' WHERE user_id = {};".format(
            settings.getDepth("Tic Tac Toe"), 
            settings.getDepth("Dame"),
            settings.getDepth("Bauernschach"),
            settings.getColorKi(),
            settings.getColorPlayer(),
            user.getId())

        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close()

    def userAlreadyExists(self, username):
        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = "SELECT * FROM user WHERE username = '{}' limit 1".format(username)

        self.cursor.execute(sql)
        records = self.cursor.fetchall()
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

        for row in records:
            return True
        return False

    def insertNewUser(self, username, password):
        if self.userAlreadyExists(username) is False:
            self.connection = sqlite3.connect(self.databaseFile)
            self.cursor = self.connection.cursor()

            sql = "INSERT INTO user VALUES(NULL, '{}', '{}')".format(username, password)

            self.cursor.execute(sql)
            self.connection.commit()
            self.connection.close()
            return True
        else: return False

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

    def insertGameSession(self, winner, board, usrId, dpName, depth):
        session = uuid4()   

        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = "INSERT INTO gameSession VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(session, winner, board, usrId, dpName, depth)

        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close() 


    def getGameStats(self, game):

        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = "SELECT winner, username, depth FROM gameStats WHERE game = '{}' ORDER BY depth DESC LIMIT 15".format(game)

        self.cursor.execute(sql)

        records = self.cursor.fetchall()

        self.cursor.close()
        self.connection.commit()
        self.connection.close()

        return records