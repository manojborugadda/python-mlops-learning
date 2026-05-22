

# Decorators

#Step1: Functions can be passed around
# in python, Functions are OBJECTS -- we can pass them as arguments
def greet():
    print("Hello")

def run(func):
    func() # calling the function

run(greet)


#Step2 : A function inside a function
def outer():
    def inner():
        print("it's INSIDE")
    inner()

outer()

#Step3 : our first DECORATOR ( manual process without using @ symbol)
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper


def greet():
    print("Hello to manual decorator")

greet = my_decorator(greet)
greet()

print("\n")

#Step4 : Using the @ symbol ( the real decorator way to do it)
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator     # this is the same as greet = my_decorator(greet)
def greet():
    print("Hello to the real decorator")

greet()
