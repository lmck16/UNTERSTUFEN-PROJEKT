from login import PageHandler
from Database import Database
from pathlib import Path

if __name__ == "__main__":

    my_file = Path("data.db")
    if my_file.is_file():
        db = Database()
        db.start()

        program = PageHandler()
        program.mainloop()
    else:
        print("Datenbank File fehlt!")