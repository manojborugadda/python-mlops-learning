
class Person:
    def __init__(self, name, age=7):
        self.name = name
        self.age = age

student1 = Person("Alice", 20)
print(student1.name)  # Output: Alice
print(student1.age)   # Output: 20
student2 = Person("Bob")
print(student2.name)  # Output: Bob
print(student2.age)   # Output: 7
print("############################")
print("Without __init__() method:")
# Without __init__() method, we would have to manually set the attributes after creating the object, which is less efficient and more error-prone.

class PersonWithoutInit:
    pass

person_without_init = PersonWithoutInit()
person_without_init.name = "Charlie"
person_without_init.age = 25

print(person_without_init.name)  # Output: Charlie
print(person_without_init.age)   # Output: 25