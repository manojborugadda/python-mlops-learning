# Inheritance

- `Inheritance` allows a class (child class) to acquire properties/attributes and methods of another class (parent class).

- `Parent class` is the class being inherited from, also called `base class`.

- `Child class` is the class that inherits from another class, also called `derived class`.

# Benefits of Inheritance

- It provides reusability of code by sharing attributes and methods across classes.
- Enables method overriding for customized subclass behavior
- Simplifies maintenance through centralized updates in parent classes.

# super() function
- The `super()` function is used to call a method from the parent class in the child class. It allows access to inherited methods that have been overridden in a class.

- It is commonly used in the child class's `__init__()` method to initialize inherited attributes. This way, the child class can leverage the functionality of the parent class
