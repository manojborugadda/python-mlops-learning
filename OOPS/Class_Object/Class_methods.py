
# creating methods in the class

class Person:
    def __init__(self, name="roger federer", age=7):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
person1 = Person("Dominic Theim", 30)
person1.greet()  # Output: Hello, my name is Dominic Theim and I am 30 years old.

print("###############################################################################################")

# methods with parameters

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
calc = Calculator()
result1 = calc.add(5, 3)
print(f"Addition Result: {result1}")  # Output: Addition Result: 8
result2 = calc.subtract(10, 4)
print(f"Subtraction Result: {result2}")  # Output: Subtraction Result: 6

print("###############################################################################################")
#methods modifying object properties
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

account = BankAccount("Alice", 100)
account.deposit(50)  # Output: Deposited 50. New balance: 150
account.withdraw(30)  # Output: Withdrew 30. New balance: 120
