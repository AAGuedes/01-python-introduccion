"""
Comparando objetos
"""


class Coords:
    """
    Docstring
    """

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # Equal
    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon

    # Not equal - Cuando se define el __eq__ infiere este, por lo que se puede omitir
    # def __ne__(self, otro):
    #     return self.lat != otro.lat or self.lon != otro.lon

    # Less than
    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon

    # Less or equal
    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon


coords1 = Coords(10, 10)
coords2 = Coords(10, 10)

# Implementando el primero, infiere el segundo
print(coords1 == coords2)
print(coords1 != coords2)

# Al igual que en el caso interior, infiere el contrario
print(coords1 < coords2)
print(coords1 > coords2)

# También infiere la el contrario
print(coords1 <= coords2)
print(coords1 >= coords2)
