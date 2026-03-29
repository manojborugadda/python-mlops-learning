
# Data types in Python

- Understanding data types is fundamental to programming in Python. 
- A data type defines the type of data that a variable can hold and determines the operations that can be performed on that data. 
- Python has several built-in data types, which can be categorized into the following groups:

1. **Numeric Types**: These include `int` for integers, `float` for floating-point numbers, and `complex` for complex numbers.
2. **Sequence Types**: These include `list`, `tuple`, and `range`. Lists are mutable, while tuples are immutable. The `range` type is used for generating a sequence of numbers.
3. **Text Type**: The `str` type is used for representing text (strings).
4. **Mapping Type**: The `dict` type is used for storing key-value pairs.
5. **Set Types**: These include `set` and `frozenset`. A `set` is a collection of unique elements, while a `frozenset` is an immutable version of a set.
6. **Boolean Type**: The `bool` type represents the truth values `True` and `False`.
7. **Binary Types**: These include `bytes`, `bytearray`, and `memoryview`, which are used for handling binary data.


**Everything is an object**: Python treats all data as *objects* and each object has a specific type, whether it’s an integer, string, or even a function.

## What is an Object?
An object is like a box that holds *data* (attributes) and tools (methods) to work with that data.

Key Features of Objects:
1️⃣ Data: This is the information stored in the object (e.g., numbers, strings).
2️⃣ Behavior: These are the actions or operations the object can perform (e.g., methods).
3️⃣ Type: Every object has a type (e.g., int, str, list).


# Analogy:
Think of an object like a smartphone:

*Data*: The apps and files stored on the phone.
*Behavior*: The phone’s tools (e.g., making calls, sending texts).
*Type*: The brand/model (e.g., iPhone, Samsung).

# Key points about data types in Python:
Dynamic typing: Python is dynamically typed, which means you don’t need to declare the type of a variable when you create it. The type is determined at runtime based on the value assigned to the variable.
Type conversion: Python provides built-in functions for converting between different data types, such as `int()`, `float()`, `str()`, etc.
Mutable vs Immutable: Some data types in Python are mutable (can be changed after creation) like lists and dictionaries, while others are immutable (cannot be changed after creation) like strings and tuples.
Type checking: You can check the type of a variable using the `type()` function, which returns the data type of the variable. For example, `type(42)` will return `<class 'int'>`.
