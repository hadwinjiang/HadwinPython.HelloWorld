import classandoo.mod01shipping.iso6346 as iso6346


class ShippingContainer:
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
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)

    def __init__(self, owner_code, contents, **kwargs):
        self.owner_code = owner_code  # Instance attribute
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code,
            serial=ShippingContainer._generate_serial()
        )

# from classandoo.mod01shipping.shipping import ShippingContainer
# c2 = ShippingContainer("YML", ["books"])
# c2.owner_code
# c3 = ShippingContainer("XUS", ["computers"])
# c7 = ShippingContainer.create_empty("YML")
# c8 = ShippingContainer.create_with_items("MAE", {"food", "textiles", "minerals"})
# c = ShippingContainer.create_empty("YML")

# Scopes in Python  -   LEGB
# Local -   Inside the current function
# Enclosing -   Inside enclosing functions
# Global    -   At the top level of the module
# Built-in  -   In the special builtins module


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents, **kwargs)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self.celsius = celsius

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
