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
    
    def insertGameSession(self, winner, board, id):
        session = uuid4()   

        self.connection = sqlite3.connect(self.databaseFile)
        self.cursor = self.connection.cursor()

        sql = "INSERT INTO gameSession VALUES('{}', '{}', '{}')".format(session, winner, board)

        self.cursor.execute(sql)
        self.connection.commit()
        self.connection.close() 



x = Database()
x.insertNewUser("tets", "435345")
print(x.login("tets", "435345"))
