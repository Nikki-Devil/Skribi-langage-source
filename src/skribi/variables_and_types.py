# ============================= #
# Variables and types in Skribi #
# ============================= #

class Variable:
    """
    A variable is a value with a type. It hasn't any name
    """

    def __init__(self, value, base_type):
        self.value = value
        self.type = base_type

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value) + " " + str(self.type)


# ============================= #
# Types in Skribi               #
# ============================= #

class BaseType:
    """
    A base type is a type that can be used in a variable.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
