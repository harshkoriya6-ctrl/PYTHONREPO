class Employee():

    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.__salary = salary

    def get_salary(self):
        return  self.__salary

    def set_salary(self,salary):
        if salary < 0:
            print("Salary can not be Nagative")
        else:
            self.__salary = salary
            print("Salary Updated ")

    def details_employee(self):
        print("Employee Id:",self.id)
        print("Employee Name: ",self.name)
        print("Salary: ",self.__salary)

    def work(self):
        print(f"{self.name} is working")


class Developer(Employee):

    def __init__(self, name, id, salary,programming_language):
        super().__init__(name,id,salary)
        self.programming_language = programming_language

    def work(self):
        print(f"{self.name} is Working on {self.programming_language}")

    def display_info(self):
        super().details_employee()
        print("Programming Language:",self.programming_language)


class Manager(Employee):

    def __init__(self, name, id, salary,team_size,expr):
        super().__init__(name, id, salary)
        self.team_size = team_size
        self.expr = expr

    def work(self):
        print(f"Manager is managing team with {self.team_size} employee")

    def display_info(self):
        super().details_employee()
        print("Team size:",self.team_size)
        print("Work Expeirence:",self.expr)


class Trainer():

    def __init__(self,expertise):
        self.expertise = expertise
    def conduct_tranning(self):
        print(f"Conducting Training on {self.expertise}")

    def display_info(self):
        print("Expertise",self.expertise)
    def work(self):
        print("Gives Training of Python Programming Laguage to new Joiny")

class SeniorDeveloper(Developer, Trainer):
    
    def __init__(self, name, id, salary, programming_language, expertise, years_of_experience):
        Developer.__init__(self, name, id, salary, programming_language)
        Trainer.__init__(self, expertise)

        self.years_of_experience = years_of_experience

    def work(self):
        print("Software Architecting + Mentoring")
    def display_info(self):
        super().display_info()
        print(f"Years Of Expierence is {self.years_of_experience}")
        print(f"Expertise {self.expertise}")
 
    

        
developer = Developer("Nihar",19225,25000,"Python")
manager = Manager("Harsh",19525, 200000, 5, 10)
trainer = Trainer("Pyhton Programming")
seniorDeveloper = SeniorDeveloper("Harry",12455,300000,"Python","System Acrhitecture",9)
employee = [developer, manager, trainer, seniorDeveloper]

for i in employee:
    print("""
""")
    i.display_info()
    i.work()
print(SeniorDeveloper.mro())





    
        
   


