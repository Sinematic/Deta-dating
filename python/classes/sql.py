import sqlite3
import database

"""

"ALTER TABLE users ADD zipcode" # ajoute une catégorie

"""

db = database.Database()
db.createdbusers()
db.feedusers()
mail = db.searchmail('sine @ sine.com')
if mail:
    print("Mail utilisé")
else:
    print("Mail disponible")


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
