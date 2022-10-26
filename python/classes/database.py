import sqlite3


class Database:

    def __init__(self, dbname='users.db'):

        self.dbname = str(dbname)

        try:
            cnx = sqlite3.connect(self.dbname)
            cursor = cnx.cursor()
            cnx.close()

        except BaseException as e:
            print(f" Erreur ! {e}")

    def __str__(self):
        return "Connecté à la base de données"

    def createdbusers(self):
        cnx = sqlite3.connect(self.dbname)
        cursor = cnx.cursor()
        cursor.execute("CREATE Table IF NOT EXISTS users(user_id integer primary key autoincrement, "
                       "firstname text, email text, password, gender, orientation, expectations, description text, "
                       "age integer, age, zipcode)")
        cnx.commit()
        cnx.close()

    def searchmail(self):
        pass

