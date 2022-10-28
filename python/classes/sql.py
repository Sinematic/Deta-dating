import database

"""
"ALTER TABLE users ADD zipcode" # ajoute une catégorie
"""

db = database.Database()
db.dbconnect()

if db.searchmail('sine@sine.com'):
    print("Adresse e-mail utilisée")
else:
    print("Adresse e-mail disponible")




# SELECT //  Donne moi les utilisateurs qui correspondent à crit age, orientation,
# results -> distance (si oui : ->retour html)

# modifier son profil, UPDATE SET
# user_id de l'user connecté, SELECT * FROM users WHERE crit = ? AND user_id is not = {user_id(connecté)}

# update ex: bio
# chercher les valeurs établies par l'utilisateur

# user_id
# chat -> 2 user_id

