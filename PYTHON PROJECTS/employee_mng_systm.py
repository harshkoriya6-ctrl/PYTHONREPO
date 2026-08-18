class employee():

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


class developer(employee):
   pass


