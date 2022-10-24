class User:

    """
    Prénom, Âge, Email, Sexe, Description, Type(ONS, FWB, Relation sérieuse, ...)
    """

    firstname = ""
    age = ""
    mail = ""
    gender = "Non spécifié"
    bio = ""
    expectations = ""

    def __init__(self, firstname, age, mail, gender, bio, expectations):

        self.firstname = firstname
        self.age = int(age)
        self.mail = mail
        self.gender = gender
        self.bio = bio
        self.expectations = expectations

    def __str__(self):
        return f"Je m'appelle {self.firstname}, " \
               f"j'ai {self.age} ans, " \
               f"genre : {self.gender}"
