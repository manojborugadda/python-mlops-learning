#base class
class Parent:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Parent name is {self.name}")


# derived class 1
class Child1(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def info(self):
        print(f"Child1 name is {self.name} and age is {self.age}")

class Child2(Parent):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def info(self):
        print(f"Child2 name is {self.name} and grade is {self.grade}")

#driver code
child1 = Child1("Alice", 10)
child1.info()  # Output: Child1 name is Alice and age is 10
child2 = Child2("Bob", "A")
child2.info()  # Output: Child2 name is Bob and grade is A
