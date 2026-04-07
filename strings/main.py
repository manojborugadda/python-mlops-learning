
# string formatting

# 1. old style -- format operator
name = "Medvedev"
age = 30
tennis1 = "{} is {} yrs old".format(name,age)

print(tennis1)

# 2. f-string
name1 = "Fonseca"
age = 19
tennis2 = f"{name1} is {age} yrs old"

print(tennis2)



# Escape Sequences in Strings

print("This is a string with a newline character.\nThis is the second line.")

print("This is a string with a tab character.\tThis text is after the tab.")

print('It\'s a string with a single quote.')

print("She said, \"Hello!\"") 

print("Hello\vWorld") # This will print "Hello" and "World" on separate lines with a vertical tab in between.

