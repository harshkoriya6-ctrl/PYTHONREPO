
class Employee():
    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id 
        self.___salary = salary

    def get_salary(self):
            return  self.__salary
    
    def set_salary(self,salary):
        if salary < 0:
            print("Salary can not be Nagative")
        else:
            self.__salary = salary
            print("Salary Updated ")

    

    


print("---- Pyhton OOP Project: Employee Management System ----")
while True:
    print("Choose an Operation:")
    print("""
1. Create a Person
2. Create a Employee
3. Create a Manager
4. Show Details
5. Exit 
""")
    choice = int(input("Enter Your choice"))
    