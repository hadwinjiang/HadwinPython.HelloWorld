class ShippingContainer:
    next_serial = 1337  # Class attribute

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code  # Instance attribute
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1

# from classandoo.mod01shipping.shipping import ShippingContainer
# c2 = ShippingContainer("YML", ["books"])
# c2.owner_code

# Scopes in Python  -   LEGB
# Local -   Inside the current function
# Enclosing -   Inside enclosing functions
# Global    -   At the top level of the module
# Built-in  -   In the special builtins module
