import classandoo.mod02string.position as position


class Location:

    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    def __repr__(self):
        return f"{typename(self)}(name={self.name}, position={self.position})"

    def __str__(self):
        return self.name


hong_kong = Location("Hong Kong", position.MarsPosition(22.29, 114.16))
stockholm = Location("Stockholm", position.MarsPosition(59.33, 18.06))
cape_town = Location("Cape Town", position.MarsPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", position.MarsPosition(51.96, 4.47))
maracaibo = Location("Maracaibo", position.MarsPosition(10.65, -71.65))


def typename(obj):
    return type(obj).__name__

# > from classandoo.mod04decorators.location import *
