

# base class 1
class Mother:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Mother name is {self.name}")

# base class 2
class Father:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Father name is {self.name}")


# derived class
class Child(Mother, Father):
    def __init__(self, mother_name, father_name, age):
        Mother.__init__(self, mother_name)
        Father.__init__(self, father_name)
        self.mother_name = mother_name
        self.father_name = father_name
        self.age = age

    def info(self):
        print(f"Child's mother is {self.mother_name} and father is {self.father_name} and age is {self.age}")

son1 = Child("Alice", "Bob", 10)
son1.info()  # Output: Child's mother is Alice and father is Bob and age is 10