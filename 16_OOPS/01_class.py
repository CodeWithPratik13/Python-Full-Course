class Employee:
    company = "Asus"

    def get_salary(self): # Self is important here because self is a way to reference the objec t of the class which is being created
        
        
        return 34000
    

e= Employee()
print(e.get_salary())

e2 = Employee()
print(e2.get_salary())
print(e2.company)