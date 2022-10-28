import sqlite3
from user import User

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

    def searchmail(self, email): # Retourne True si le mail est utilisé
        self.dbconnect()
        test = self.cursor.execute(f"SELECT email FROM users WHERE email = '{email}'")
        result = test.fetchall()

        if len(result) == 0:
            return False
        else:
            return True

    def login(self, email, password): # Retourne True si l'utilisateur est reconnu
        self.dbconnect()
        test = self.cursor.execute(f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'")
        result = test.fetchone()

        if len(result) == 0:
            return False
        else:
            return True

    def retrievedata(self, email, password):
        self.dbconnect()
        test = self.cursor.execute(f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'")
        result = test.fetchone()

        if result:
            return User(result[1], result[8], result[2], result[4], result[7], result[5])
        else:
            return "Utilisateur non trouvé"


db = Database()
db.dbconnect()
email = "sine@sine.com"
password = 'sine'
co = db.login(email, password)

if co:
    user = db.retrievedata(email, password)
    print(f"Bonjour {user.firstname}")
else:
    print("Identifiants incorrects !")
