import sqlite3


class Database:

    def __init__(self, dbname='users.db'):

        self.dbname = str(dbname)

    def dbconnect(self):

        try:
            self.cnx = sqlite3.connect(self.dbname)
            self.cursor = self.cnx.cursor()
            return self.cnx, self.cursor

        except BaseException as e:
            print(f" Erreur ! {e}")

    def __str__(self):
        return "Connecté à la base de données"

    def createdbusers(self):

        self.dbconnect()
        self.cursor.execute("CREATE Table IF NOT EXISTS users(user_id integer primary key autoincrement, "
                       "firstname text, email text, password, gender, orientation, expectations, description text, "
                       "age integer, zipcode)")
        self.cnx.commit()
        self.cnx.close()

    def feedusers(self):

        self.dbconnect()
        self.cursor.execute("INSERT INTO users (firstname, email, password, orientation, description, age, gender) " \
                       "VALUES ('Maxime', 'sine@sine.com', 'sine', '0', 'Salut je suis le plus beau', 26, '1'), \
                       ('Aurélie', 'aure@aure.com', 'aure', '1', 'Salut je suis la plus belle', 25, '0'), \
                       ('LadyGaga', 'lady@gaga.com', 'gaga', '2', 'Salut je suis une super star', 35, '0')"
                       )
        self.cnx.commit()
        self.cnx.close()

    def searchmail(self, email):
        self.dbconnect()
        return self.cursor.execute(f"SELECT * FROM users WHERE email = {email}")

