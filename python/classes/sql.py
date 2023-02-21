from database import Database


db = Database()
db.dbconnect()

"""
if db.searchmail('sine@sine.com'):
    print("Adresse e-mail utilisée")
else:
    print("Adresse e-mail disponible")
"""

result = db.login('sine@sine.com', 'sine')
if result:
    print(f"Bonjour {result.firstname}")
else:
    print("Identifiants incorrects")

# SELECT //  Donne moi les utilisateurs qui correspondent à crit age, orientation,
# results -> distance (si oui : ->retour html)
