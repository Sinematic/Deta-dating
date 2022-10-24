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
        pass

    def __str__(self):

        return f"{self.getlocation()}"


loc = Location("94410")
position = loc.getlocation()
#  print(position[1]) #  position[1] = city
