from geopy.geocoders import Nominatim


class Location:

    """
    Classe qui retourne la localisation après que l'utilisateur ait donné son code postal
    """

    zipcode = str
    city = str
    country = str
    geopy = object
    location = tuple

    def __init__(self, zipcode):

        self.zipcode = zipcode
        self.geopy = Nominatim(user_agent="Deta")

    def getlocation(self):

        self.location = (self.geopy.geocode(self.zipcode).latitude, self.geopy.geocode(self.zipcode).longitude)
        self.city = self.geopy.geocode(self.zipcode).address.split()[0]
        return self.location, self.city

    def getcity(self):

        __loc = Location(self.zipcode)
        __position = __loc.getlocation()
        self.city = __position[1]
        return self.city

    def __str__(self):

        return f"{self.getlocation()}"

