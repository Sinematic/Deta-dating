from database import Database


db = Database()

max = db.retrievedata('sine@sine.com', 'sine')
max.firstname = 'Maxime'
max.zipcode = "94410"
print(max.firstname)

user2 = input("Entrez votre CP:")

