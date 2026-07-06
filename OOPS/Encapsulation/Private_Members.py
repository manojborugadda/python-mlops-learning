
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def show_salary(self):
        print("Salary is :", self.__salary)

emp = Employee("Alexandra",1000)
print("Name is :", emp.name)
emp.show_salary()
# print(emp.__salary)
