# Class and Object
A class is a blueprint or template for creating objects.
An object is an instance of a class created from that blueprint.

Every object has two main parts:
- Attributes: what the object has
- Methods: what the object can do

#  `self` Parameter
- The self parameter is a reference to the current instance of the class.
- It is used to access properties and methods that belong to the class.

```python
class Dog:
    def __init__(self, name):
        self.name = name   # attribute

    def bark(self):      # method
        print("Woof!")
```

Here:

name is an attribute because it describes the dog
bark() is a method because it defines an action the dog can perform

Example usage:
```python
dog1 = Dog("Buddy")

print(dog1.name)   # attribute
dog1.bark()        # method
```


# Class vs Instance Attributes

In Python, classes can have two types of attributes: class attributes and instance attributes. Understanding the difference between these two is crucial for effective object-oriented programming.

Class attributes live on the class and are shared by every instance. If the attribute is mutable (like a list or dict), mutating it from one instance changes it for all instances. To give each instance its own copy, initialize the attribute in __init__

```python
class Dog:
    species = 'Canis familiaris'  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Example usage
dog1 = Dog('Buddy', 3)
dog2 = Dog('Max', 5)

print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris
print(dog1.name)     # Output: Buddy
print(dog2.name)     # Output: Max
print(dog1.age)      # Output: 3
print(dog2.age)      # Output: 5
```

# Shared mutation 
Multiple references point to the same object in memory. 
When one reference mutates it, all other references see the change because they're looking at the same object.

```python
class Waiter:
    tips = []  # Class attribute (shared by all instances)

    def __init__(self, name):
        self.name = name  # Instance attribute

    def add_tip(self, tip):
        self.tips.append(tip)  # Mutating the class attribute

# Example usage
waiter1 = Waiter('Alice')
waiter2 = Waiter('Bob')
waiter1.add_tip(5)
print(waiter1.tips)  # Output: [5]
waiter2.add_tip(10)
print(waiter1.tips)  # Output: [5, 10]
print(waiter2.tips)  # Output: [5, 10]
```

