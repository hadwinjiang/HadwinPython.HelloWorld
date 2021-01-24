class ShippingContainer:
    next_serial = 1337  # Class attribute

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code  # Instance attribute
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()

# from classandoo.mod01shipping.shipping import ShippingContainer
# c2 = ShippingContainer("YML", ["books"])
# c2.owner_code
# c3 = ShippingContainer("XUS", ["computers"])

# Scopes in Python  -   LEGB
# Local -   Inside the current function
# Enclosing -   Inside enclosing functions
# Global    -   At the top level of the module
# Built-in  -   In the special builtins module
