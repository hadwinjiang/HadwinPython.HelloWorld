class Base:
    def __init__(self):
        print("Base initializer")

    def f(self):
        print("Base.f()")


class Sub(Base):
    def __init__(self):
        super().__init__()
        print("Sub initializer")

    def f(self):
        print("Sub.f()")


#> from classandoo.mod03inheritance.base import *
#> b = Base()
#> b.f()
#> s = Sub()