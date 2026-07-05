
from animal import Animal
from cat import Cat

animal1 = Cat("Tom", color="orange")
# inherited method from parent class
animal1.info()
# inherited behavior from child class
animal1.sound() # method overriding is demonstrated here
print(f"Cat color is {animal1.color}")

