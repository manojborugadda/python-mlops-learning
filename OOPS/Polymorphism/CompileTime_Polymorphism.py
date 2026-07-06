# defualt arguments
class Calculator:
    def add(self, a=0, b=0):
        return a + b

    def subtract(self, a=0, b=0):
        return a - b

calc = Calculator()
print(calc.add(5, 3))  # Output: 8
print(calc.add(5))     # Output: 5 (b defaults to 0)
print(calc.subtract(10, 4))  # Output: 6
print(calc.subtract(10))     # Output: 10 (b defaults to 0)
print("\n")
print("###############################################################################################")
# variable-length arguments
class Calculator:
    def add(self, *args):
        return sum(args)

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

calc = Calculator()
print(calc.add(5, 3))  # Output: 8
print(calc.add(5, 3, 2))  # Output: 10
print(calc.multiply(2, 3))  # Output: 6
print(calc.multiply(2, 3, 4))  # Output: 24

print("\n")
print("###############################################################################################")

# keyword arguments

class Calculator:
    def add(self, **kwargs):
        return sum(kwargs.values())

    def multiply(self, **kwargs):
        result = 1
        for num in kwargs.values():
            result *= num
        return result

calc = Calculator()
print(calc.add(a=5, b=3))  # Output: 8
print(calc.multiply(a=2, b=3))  # Output: 6
print("###############################################################################################")

class User:
    def create_profile(self, **kwargs):
        profile = {}
        for key, value in kwargs.items():
            profile[key] = value
        return profile

user = User()
profile = user.create_profile(name="Alice", age=30, city="New York")
print(profile)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
profile2 = user.create_profile(name="Bob", age=25, country="USA", profession="Engineer")
print(profile2)  # Output: {'name': 'Bob', 'age': 25, 'country': 'USA', 'profession': 'Engineer'}