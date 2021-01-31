import inspect

import classandoo.mod02string.position as position


def auto_repr(cls):
    # print(f"Decorating {cls.__name__} with auto_repr")
    members = vars(cls)

    # for name, member in members.items():
    #     print(name, member)

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")

    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")

    sig = inspect.signature(cls.__init__)
    parameter_names = list(sig.parameters)[1:]
    # print("__init__ parameter names: ", parameter_names)

    if not all (
        isinstance(members.get(name, None), property)
        for name in parameter_names
    ):
        raise TypeError(
            f"Cannot apply auto_repr to {cls.__name__} because not all "
            "__init__ parameters have matching properties"
        )

    def synthesized_repr(self):
        return "{typename} with decorator ({args})".format(
            typename=typename(self),
            args=", ".join(
                "{name}={value!r}".format(
                    name=name,
                    value=getattr(self, name)
                ) for name in parameter_names
            )
        )

    setattr(cls, "__repr__", synthesized_repr)

    return cls


@auto_repr
class Location2:

    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    # def __repr__(self):
    #     return f"{typename(self)}(name={self.name}, position={self.position})"

    def __str__(self):
        return self.name


hong_kong = Location2("Hong Kong", position.MarsPosition(22.29, 114.16))
stockholm = Location2("Stockholm", position.MarsPosition(59.33, 18.06))
cape_town = Location2("Cape Town", position.MarsPosition(-33.93, 18.42))
rotterdam = Location2("Rotterdam", position.MarsPosition(51.96, 4.47))
maracaibo = Location2("Maracaibo", position.MarsPosition(10.65, -71.65))


def typename(obj):
    return type(obj).__name__

# > from classandoo.mod04decorators.location2 import *
# Decorating Location2 with auto_repr
# __module__ classandoo.mod04decorators.location2
# __init__ <function Location2.__init__ at 0x1082dc430>
# name <property object at 0x1082dbd60>
# position <property object at 0x1082dbd10>
# __str__ <function Location2.__str__ at 0x1082dc5e0>
# __dict__ <attribute '__dict__' of 'Location2' objects>
# __weakref__ <attribute '__weakref__' of 'Location2' objects>
# __doc__ None
