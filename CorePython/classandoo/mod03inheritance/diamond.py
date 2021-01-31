class A:
    def func(self):
        return "A.func"


class B(A):
    def func(self):
        return "B.func"


class C(A):
    def func(self):
        return "C.func"


class D(B, C):
    pass


#> from classandoo.mod03inheritance.diamond import *
#> D.__mro__
#  (<class 'classandoo.mod03inheritance.diamond.D'>, <class 'classandoo.mod03inheritance.diamond.B'>, <class 'classandoo.mod03inheritance.diamond.C'>, <class 'classandoo.mod03inheritance.diamond.A'>, <class 'object'>)
#> d = D()
#> d.func()
#  'B.func'
