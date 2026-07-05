
# Base class
class Grandfather:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Grandfather name is {self.name}")


# Derived class 1 or intermediate class
class Father(Grandfather):
    def __init__(self, name, father_name, grandfather_name):
        super().__init__(name)
        self.father_name = father_name
        self.grandfather_name = grandfather_name
 
    def info(self):
        print(f"Father name is {self.father_name} and grandfather is {self.grandfather_name}")

# Derived class 2 or child class
class Son(Father):
    def __init__(self, name, father_name, grandfather_name, age):
        super().__init__(name, father_name, grandfather_name)
        self.age = age

    def info(self):
        print(f"Son name is {self.name}, father is {self.father_name}, grandfather is {self.grandfather_name} and age is {self.age}")

son1 = Son("yesobu", "paul", "chinna yesobu", 10)
son1.info()  # Output: Son name is yesobu, father is paul, grandfather is chinna yesobu and age is 10
