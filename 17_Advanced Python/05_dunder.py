class Employee:
    company = "Asus"
    def __init__(self, name, salary):
        self.name = name
        self.salary= salary

    def __str__(self):
        return f"The name is {self.name} and salary is {self.salary}"

    def __repr__(self):
        return f"name: {self.name}\nSalary: {self.salary}"

    def __len__(self):
        return len(self.name)

e = Employee("Pratik", 46546)
print(len(e))
# print(e.name, e.salary)
# print(str(e))
# print(repr(e))