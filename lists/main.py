
# basic unpacking

a, b, c = [1, 2, 3]
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# unpacking with *
numbers = [1, 2, 3, 4, 5]

first, second, *remaining = numbers

print("first is :",first)
print("second is :",second)
print("remaining values are : ",remaining)

