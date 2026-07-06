

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # private attribute

    # Getter method for salary
    def get_salary(self):
        return self.__salary

    # Setter method for salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary. Please enter a positive value.")

emp = Employee("Stefan", 50000)
print(emp.name)  # Output: Stefan
print(emp.get_salary())  # Output: 50000
emp.set_salary(60000)
print(emp.get_salary())  # Output: 60000