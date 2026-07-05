class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Animal name is {self.name}")

    def sound(self):
        print(f"{self.name} makes a sound")