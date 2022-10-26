class User:

    """
    Prénom, Âge, Email, Sexe, Bio, Description, Type(ONS, FWB, Relation sérieuse, ...), Orientation
    # Hobbies, critères physiques (taille/poids)
    """

    firstname = ""
    age = ""
    mail = ""
    gender = "Non spécifié"
    bio = ""
    expectations = ""

    def __init__(self, firstname, age, mail, gender, bio, expectations, orientation):

        self.firstname = firstname
        self.age = int(age)
        self.mail = mail
        self.gender = gender
        self.bio = bio
        self.orientation = orientation
        self.expectations = expectations

    def __str__(self):
        return f"Je m'appelle {self.firstname}, " \
               f"j'ai {self.age} ans, " \
               f"genre : {self.gender}"



# je récupère les infos en db de l'utilisateur
#