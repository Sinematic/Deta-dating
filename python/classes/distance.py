from haversine import *
from location import Location


class Distance:

    """
    Classe permettant le calcul de la distance entre deux utilisateurs
    On lui fournit deux tuples contenant la longitude et la latitude de chaque utilisateur
    """

    location1 = tuple  # Tuple (latitude, longitude)
    location2 = tuple
    haversine = object  # Instance de la classe Haversine qui
    # propose le calcul de la distance grâce à la fonction haversine

    def __init__(self, location1, location2):

        self.location1 = (location1[0], location1[1])
        self.location2 = (location2[0], location2[1])

    def getdistance(self):
        # Distance en km arrondie en un int
        return round(haversine(self.location1, self.location2, unit='km'))

    def __str__(self):
        return f'Location1 : {self.location1}, Location2 : {self.location2}'


try:
    # L'utilisateur doit donner son CP
    loc1 = input("CP1")  # remplacer par une requête SQL qui renvoie le CP de l'utilisateur
    
    # On crée une instance de Location
    glocation1 = Location(loc1)
    
    # On récupère un tuple contenant latitude et longitude
    m1 = glocation1.getlocation()[0]
    print(glocation1, m1)
    
    loc2 = input("CP2")
    glocation2 = Location(loc2)
    m2 = glocation2.getlocation()[0]
    
    # On crée une instance de Distance et on lui donne pour arguments
    # les positions des utilisateurs dont il faudra calculer l'éloignement
    getdist = Distance(m1, m2)
    
    # On calcule la distance entre les deux utilisateurs
    dist = getdist.getdistance()
    print(f'{dist} km')
    
except ValueError as e:
    print(f"T'as tout cassé \n {e}")
    
