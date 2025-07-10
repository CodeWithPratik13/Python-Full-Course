class Employee:
    company = "Asus"
    def __init__(self, name, salary):
        self.name = name
        self.salary= salary

    # instance method (Default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # static method
    @staticmethod
    def sum(a, b):
        return a + b
    
    # class method
    @classmethod
    def print_company(cls):
        print(cls.company)
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
     


e1 = Employee("jack", 3435)
e2 = Employee("jill",5646)
# print(Employee.company)
# print(Employee.name) # this will throw an error
# e1.print_info()
# e2.print_info()

# print(e2.sum(5, 23))
e1.print_company()
e1.change_company("HP")
# e1.print_company()
print(Employee.company)