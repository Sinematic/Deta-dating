from location import Location


class User:

    """
    Prénom, Âge, Email, Sexe, Description, Type(ONS, FWB, Relation sérieuse, ...), Orientation
    # Hobbies, critères physiques (taille/poids)
    """

    firstname = str
    age = int
    email = str
    gender = int
    orientation = int
    description = str
    expectations = int
    zipcode = int
    city = str
    password = str

    def __init__(self, email, age, firstname='', gender='', description='', expectations='', zipcode='', password='',
                 orientation=''):

        self.firstname = firstname
        self.email = email
        self.age = age
        self.gender = gender
        self.description = description
        self.expectations = expectations
        self.zipcode = zipcode
        self.password = password
        self.orientation = orientation

    def __str__(self):

        return f"Je m'appelle {self.firstname}, " \
               f"j'ai {self.age} ans, " \
               f"genre : {self.gender}"

    def getcity(self):

        __loc = Location(self.zipcode)
        __loc.getcity()

        """
        __position = __loc.getlocation()
        self.city = __position[1]
        return self.city
        """
