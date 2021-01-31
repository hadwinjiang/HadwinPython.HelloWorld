class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")

        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {latitude} out of range")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    def __repr__(self):
        return f"{typename(self)}(latitude={self.latitude}, longitude={self.longitude})"


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


def typename(obj):
    return type(obj).__name__


#> from classandoo.mod02string.position import *
#> oslo = Position(60.0, 10.7)
#> repr(oslo)
# '<classandoo.mod02string.position.Position object at 0x10d6c1070>'
#> str(oslo)
# '<classandoo.mod02string.position.Position object at 0x10d6c1070>'
#> format(oslo)
# '<classandoo.mod02string.position.Position object at 0x10d6c1070>'
#> dir(object)
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
# __format__, __repr__, __str__

#> from classandoo.mod02string.position import *
#> sydney = Position(-33.9, 151.2)
#> repr(sydney)
# 'Position -33.9 151.2'
#> sydney
# Position -33.9 151.2
#> earth_position = EarthPosition(23, 23)
#> mars_position = MarsPosition(34, 45)