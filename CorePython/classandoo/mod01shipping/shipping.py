import classandoo.mod01shipping.iso6346 as iso6346


class ShippingContainer:
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0
    next_serial = 1337  # Class attribute

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), **kwargs)

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.owner_code = owner_code  # Instance attribute
        self.length_ft = length_ft
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code,
            serial=ShippingContainer._generate_serial()
        )

    @property
    def volume_ft3(self):
        return self._calc_volume()

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


# from classandoo.mod01shipping.shipping import *
# c2 = ShippingContainer("YML", ["books"])
# c2.owner_code
# c3 = ShippingContainer("XUS", ["computers"])
# c7 = ShippingContainer.create_empty("YML")
# c8 = ShippingContainer.create_with_items("MAE", {"food", "textiles", "minerals"})
# c = ShippingContainer.create_empty("YML", length_ft=20)

# Scopes in Python  -   LEGB
# Local -   Inside the current function
# Enclosing -   Inside enclosing functions
# Global    -   At the top level of the module
# Built-in  -   In the special builtins module


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents, **kwargs)
        self.celsius = celsius

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    def _calc_volume(self):
        return (
                super(RefrigeratedShippingContainer, self)._calc_volume()
                - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3
        )

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )


# from classandoo.mod01shipping.shipping import *
# r1 = RefrigeratedShippingContainer("MAE", ["fish"])
# r2 = RefrigeratedShippingContainer.create_empty("YML")
# r3 = RefrigeratedShippingContainer.create_with_items("ESC", ["onions"], celsius=2.0)
# r5 = RefrigeratedShippingContainer.create_empty("YML", length_ft=20, celsius=-10.0)


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20

    # def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
    #     super().__init__(owner_code, length_ft, contents, null, celsius, kwargs)
    #     self._celsius = value

    def _set_celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold!")
        super(HeatedRefrigeratedShippingContainer, self)._set_celsius(value)

# from classandoo.mod01shipping.shipping import *
# h1 = HeatedRefrigeratedShippingContainer.create_empty("ESC", length_ft=40, celsius=-18.0)