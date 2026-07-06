class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # private attribute

    # def get_salary(self):
    #     return self.__salary


# Create an instance of Employee
emp = Employee("John", 50000)
print(emp.name)  # Output: John
# print(emp.__salary)  # This will raise an AttributeError because __salary is private
print(emp.__salary)
