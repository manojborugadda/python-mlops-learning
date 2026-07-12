
# By default, all members in Python are public
# They are defined without any underscore prefix

class PublicMembers:
    def __init__(self, name):
        self.name = name  # public member

    def display_name(self):
        print(f"Name: {self.name}")  # public method

employee = PublicMembers("Sacha Zverev")
# Accessing public member directly
print(employee.name)  # Output: Sacha Zverev
# Accessing public method directly
employee.display_name()  # Output: Name: Sacha Zverev