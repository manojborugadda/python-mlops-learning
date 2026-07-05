
class Parent:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Parent name is {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def info(self):
        print(f"Child name is {self.name} and age is {self.age}")

child1 = Child("Alice", 10)
child1.info()  # Output: Child name is Alice and age is 10
child2 = Child("Bob", 12)
child2.info()  # Output: Child name is Bob and age is 12

