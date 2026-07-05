from animal import Animal

class Cat(Animal):
    def __init__(self, name, color="black"):
        super().__init__(name)
        self.color = color

    def sound(self):
        print(self.name, "meows")
