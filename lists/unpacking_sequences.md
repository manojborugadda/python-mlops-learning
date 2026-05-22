# Unpacking Sequences

In Python, you can unpack sequences (like lists, tuples, etc.) into individual variables. This is a convenient way to assign values from a sequence to multiple variables in a single line of code.

## Basic Unpacking

You can unpack a sequence by assigning it to a tuple of variables. The number of variables must match the number of elements in the sequence.

```python # Unpacking a list
my_list = [1, 2, 3]
a, b, c = my_list
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Unpacking a tuple
my_tuple = ('Alice', 30, 'Engineer')
name, age, profession = my_tuple
print(name)       # Output: Alice
print(age)        # Output: 30
print(profession) # Output: Engineer
``` 

## Unpacking with the Asterisk (*)

If you want to unpack a sequence but don't know the exact number of elements, you can use the asterisk (*) operator to capture the remaining elements in a list.

```python
my_list = [1, 2, 3, 4, 5]
a, b, *rest = my_list
print(a)    # Output: 1
print(b)    # Output: 2
print(rest) # Output: [3, 4, 5]
```
You can also use the asterisk to unpack elements from the middle of a sequence:

```python
my_list = [1, 2, 3, 4, 5]
a, *middle, b = my_list
print(a)      # Output: 1
print(middle) # Output: [2, 3, 4]
print(b)      # Output: 5
```
## Unpacking with Ignoring Values
If you want to unpack a sequence but ignore certain values, you can use the underscore (_) as a placeholder for the values you want to ignore.

```python
my_list = [1, 2, 3, 4, 5]
a, _, c, _, e = my_list
print(a)  # Output: 1
print(c)  # Output: 3
print(e)  # Output: 5
```

## Unpacking in Function Arguments
You can also use unpacking when passing arguments to a function. This allows you to pass a sequence of values as individual arguments.

```python
def print_values(a, b, c):
    print(a)
    print(b)
    print(c)

my_list = [1, 2, 3]
print_values(*my_list)

In this example, the `*my_list` syntax unpacks the list into individual arguments for the `print_values` function. The output will be:
# output:
1
2
3
```
You can also use unpacking with keyword arguments by using the double asterisk (**) operator:

```python
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")
my_dict = {'name': 'Alice', 'age': 30}
print_info(**my_dict)

In this example, the `**my_dict` syntax unpacks the dictionary into keyword arguments for the `print_info` function. The output will be:
# output:
Name: Alice, Age: 30
```

Unpacking sequences is a powerful feature in Python that allows for more concise and readable code when working with sequences of data. It can be used in various contexts, such as variable assignment, function arguments, and more.

