
# creating the class with properties

class Person:
    profession = ""  # Class variable
    def __init__(self, name="roger federer", age=7):
        self.name = name
        self.age = age

person1 = Person("Alicia Parks", 20)

print(person1.age)
print(person1.name)
print(person1.profession)

# modifying the properties of the object
person1.name = "Belinda bencic"
person1.profession = "Professional Tennis Player"

print(person1.name)
print(person1.profession)

"""
# deleting the properties of the object
# del person1.age
# print(person1.age)  # This will raise an AttributeError since the age property has been deleted.

"""

# add new properties to the object
person1.country = "Switzerland"
print(person1.country)  # Output: Switzerland

person1.city = "Basel"
print(person1.city)  # Output: Basel

# modify properties of the class
Person.profession = "Athlete"
print(Person.profession)  # Output: Athlete