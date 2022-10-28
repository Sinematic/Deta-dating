class User:

    """
    Prénom, Âge, Email, Sexe, Description, Type(ONS, FWB, Relation sérieuse, ...), Orientation
    # Hobbies, critères physiques (taille/poids)
    """

    firstname = ""
    age = ""
    mail = ""
    gender = "Non spécifié"
    description = ""
    expectations = ""

    def __init__(self, firstname, age, mail, gender, description, expectations):

        self.firstname = firstname
        self.age = int(age)
        self.mail = mail
        self.gender = gender
        self.description = description
        self.expectations = expectations

    def __str__(self):
        return f"Je m'appelle {self.firstname}, " \
               f"j'ai {self.age} ans, " \
               f"genre : {self.gender}"

