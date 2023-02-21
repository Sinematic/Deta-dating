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
        value = self.cursor.execute("CREATE Table IF NOT EXISTS users(user_id integer primary key autoincrement, "
                       "firstname text, email text, password, gender, orientation, expectations, description text, "
                       "age integer, zipcode)")
        self.cnx.commit()
        self.cnx.close()

        if value is not None:
            print("Utilisateur créé")
        else:
            print("Adresse e-mail déjà utilisée")

    def feedusers(self):

        self.dbconnect()
        self.cursor.execute("INSERT INTO users (firstname, email, password, orientation, description, age, gender) " \
                       "VALUES ('Maxime', 'sine@sine.com', 'sine', '0', 'Salut je suis le plus beau', 26, '1'), \
                       ('Aurélie', 'aure@aure.com', 'aure', '1', 'Salut je suis la plus belle', 25, '0'), \
                       ('LadyGaga', 'lady@gaga.com', 'gaga', '2', 'Salut je suis une super star', 35, '0')"
                            )

        self.cnx.commit()
        self.cnx.close()

    def searchmail(self, email):  # Retourne True si le mail est utilisé

        self.dbconnect()
        test = self.cursor.execute(f"SELECT email FROM users WHERE email = '{email}'")
        result = test.fetchall()

        if len(result) == 0:
            return False  # Adresse e-mail disponible
        else:
            return True  # Adresse e-mail utilisée

    def login(self, email, password): # Retourne True si l'utilisateur est reconnu

        result = self.retrievedata(email, password)

        return result

    def retrievedata(self, email, password):

        self.dbconnect()
        test = self.cursor.execute(f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'")
        result = test.fetchone()

        if result:
            return User(firstname=result[1], email=result[2], password=result[3], gender=result[4],
                        orientation=result[5], expectations="Amour", description=result[7], age=result[8])
        else:
            return False

    def createuser(self, email, password, age):

        self.dbconnect()
        result = self.searchmail(email)

        if result:
            print("Adresse e-mail déjà utilisée")
        else:
            self.cursor.execute(f"INSERT INTO Users (email, password, age) values ('{email}', '{password}', '{age}')")
            self.cnx.commit()
            self.cnx.close()
            print("Utilisateur ajouté à la base de données")
            return User(email=email, age=age)

    def deleteuser(self, user_id):

        self.dbconnect()
        test = self.cursor.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
        result = test.fetchall()

        if len(result) == 0:
            print("Utilisateur non trouvé")
        else:
            self.cursor.execute(f"DELETE FROM users WHERE user_id = '{user_id}'")
            self.cnx.commit()
            self.cnx.close()
            print(f"Le compte de l'utilisateur dont l'ID est {user_id} a bien été supprimé.")

    def addcolumn(self, arg):

        self.dbconnect()

        try:
            self.cursor.execute(f"ALTER TABLE users ADD {arg}")
        except BaseException as e:
            print(e)

        self.cnx.commit()
        self.cnx.close()

