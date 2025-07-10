class Employee:
    company = "Asus"

    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond}")

e1 = Employee(40000, "Pratik", 4, "BMW")
print(e1.company) # this will always print instance attribute whenever present
print(Employee.company) # this will always print the class attribute


# Object introspection
print(dir(e1))
