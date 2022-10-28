class User:

    """
    Prénom, Âge, Email, Sexe, Description, Type(ONS, FWB, Relation sérieuse, ...), Orientation
    # Hobbies, critères physiques (taille/poids)
    """

    firstname = ""
    age = ""
    email = ""
    gender = "Non spécifié"
    description = ""
    expectations = ""
    zipcode = ""

    def __init__(self, email, age, firstname='', gender='', description='', expectations='', zipcode=''):

        self.firstname = firstname
        self.email = email
        self.age = int(age)
        self.gender = gender
        self.description = description
        self.expectations = expectations
        self.zipcode = zipcode

    def __str__(self):
        return f"Je m'appelle {self.firstname}, " \
               f"j'ai {self.age} ans, " \
               f"genre : {self.gender}"


    def getcity(self, zipcode):
