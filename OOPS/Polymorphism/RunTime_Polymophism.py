class Animal:
    def __init__(self, name):
         self.name = name
    def make_sound(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meows")

# Create instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")
print("Dog sound: ", end="")
dog.make_sound()
print("Cat sound: ", end="")
cat.make_sound()