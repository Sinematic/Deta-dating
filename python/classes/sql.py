import sqlite3

"""
"CREATE Table IF NOT EXISTS users(user_id integer primary key autoincrement, firstname text, email text, password, " \
                "orientation, expectations, description text, age integer, age, zipcode, gender)"
"ALTER TABLE users ADD zipcode" # ajoute une catégorie


query = "INSERT INTO users (firstname, email, password, orientation, description, age, gender) " \
        "VALUES ('Maxime', 'sine@sine.com', 'sine', '0', 'Salut je suis le plus beau', 26, '1') "

"""

try:
    cnx = sqlite3.connect('users.db')
    cursor = cnx.cursor()
    email = "sine@sine.com"
    cursor.execute(f"SELECT * FROM users WHERE email = 'sie@sine.com'")
    user = cursor.fetchall()
    if user:
        print('Adresse e-mail déjà utlisée')
    else:
        print('Adresse e-mail disponible')

    query = "INSERT INTO users (firstname, email, password, orientation, description, age, gender) " \
            "VALUES ('Lady Gaga', 'lady@gaga.com', 'gaga', '2', 'Super star', 25, '0') "

    #cursor.execute(query)
    #cnx.commit()
    cnx.close()

except BaseException as e:
    print(f" Erreur ! {e}")

# query = "INSERT INTO Users (firstname, email, description, age) values " \
# "(User.firstname, User.email, User.description, User.age)"

# loginquery = "SELECT * FROM Users WHERE email = ?, password = ?"


# SELECT //  Donne moi les utilisateurs qui correspondent à crit age, orientation,
# results -> distance (si oui : ->retour html)

# modifier son profil, update set ->

# update ex: bio
# chercher les valeurs établies par l'utilisateur

# form qui donne des données, on fait la comparaison mail + pw
# si correspondance :
# création du user

# user_id
# chat -> 2 user_id