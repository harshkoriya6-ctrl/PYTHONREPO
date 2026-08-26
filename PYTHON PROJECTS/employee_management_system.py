
class Person:
     """
    Definition: Base class representing a person.
    Attributes: name and age
    Return: None
    """
     def __init__(self, name, age):
        self.name = name
        self.age = age
        """
        Definition: Initializes a Person object.
        Arguments: name, age
        Return: None
        """
     def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        """
        Definition: Displays the name and age of the person.
        Arguments: self
        Return: None
        """

class Employee(Person):
    """
    Definition: Represents an employee inherited from Person.
    Attributes: employee_id, name, age and salary
    Return: None
    """

    def __init__(self, employee_id=None, name=None, age=None, salary=0):
        """
        Definition: Initializes an Employee object.
        Arguments: employee_id, name, age, salary
        Return: None
        """

        super().__init__(name, age)

        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        """
        Definition: Returns the private employee ID.
        Arguments: self
        Return: Employee ID
        """
        return self.__employee_id


    def set_employee_id(self, employee_id):
        """
        Definition: Updates the private employee ID.
        Arguments: employee_id
        Return: None
        """
        self.__employee_id = employee_id
        print("Employee ID Updated Successfully")


    def get_salary(self):
        """
        Definition: Returns the private employee salary.
        Arguments: self
        Return: Salary
        """
        return self.__salary

    def set_salary(self, salary):
        """
        Definition: Updates salary if it is not negative.
        Arguments: salary
        Return: None
        """   

        if salary < 0:
            print("Salary cannot be negative")
        else:
            self.__salary = salary
            print("Salary Updated Successfully")

    def display(self):
        """
        Definition: Displays employee ID, name, age and salary.
        Arguments: self
        Return: None
        """

        print("\nEmployee Details")
        print("----------------")
        print("Employee ID:", self.__employee_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.__salary)


    def __del__(self):
        """
        Definition: Destructor used when Employee object is deleted.
        Arguments: self
        Return: None
        """
        pass


class Manager(Employee):
    """
    Definition: Represents a Manager inherited from Employee.
    Attribute: department
    Return: None
    """

    def __init__(self, employee_id, name, age, salary, department):
        """
        Definition: Initializes a Manager object.
        Arguments: employee_id, name, age, salary, department
        Return: None
        """

        super().__init__(
            employee_id,
            name,
            age,
            salary
        )

        self.department = department

    def display(self):
        """
        Definition: Displays employee details and department.
        Arguments: self
        Return: None
        """

        super().display()
        print("Department:", self.department)


class Developer(Employee):
    """
    Definition: Represents a Developer inherited from Employee.
    Attribute: programming_language
    Return: None
    """

    def __init__(
        self,
        employee_id,
        name,
        age,
        salary,
        programming_language
    ):

        super().__init__(
            employee_id,
            name,
            age,
            salary
        )

        self.programming_language = programming_language

    def display(self):
        """
        Definition: Initializes a Developer object.
        Arguments: employee_id, name, age, salary, programming_language
        Return: None
        """

        super().display()
        print(
            "Programming Language:",
            self.programming_language
        )


# Storage
employees = {}
persons = []


print("\n--- Python OOP Project: Employee Management System ---")


while True:

    print("""
Choose an operation:

1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)

        persons.append(person)

        print(
            f"\nPerson created with name: "
            f"{name} and age: {age}."
        )

    elif choice == "2":

        employee_id = int(
            input("Enter Employee ID: ")
        )

        name = input("Enter Name: ")

        age = int(
            input("Enter Age: ")
        )

        salary = float(
            input("Enter Salary: ")
        )

        employee = Employee(
            employee_id,
            name,
            age,
            salary
        )

        employees[employee_id] = employee

        print(
            "\nEmployee Created Successfully!"
        )


    elif choice == "3":

        print("""
Choose Employee Type:

1. Manager
2. Developer
""")

        role = input("Enter Choice: ")


        if role == "1":

            employee_id = int(
                input("Enter Employee ID: ")
            )

            name = input("Enter Name: ")

            age = int(
                input("Enter Age: ")
            )

            salary = float(
                input("Enter Salary: ")
            )

            department = input(
                "Enter Department: "
            )

            manager = Manager(
                employee_id,
                name,
                age,
                salary,
                department
            )

            employees[employee_id] = manager

            print(
                "\nManager Created Successfully!"
            )

        elif role == "2":

            employee_id = int(
                input("Enter Employee ID: ")
            )

            name = input("Enter Name: ")

            age = int(
                input("Enter Age: ")
            )

            salary = float(
                input("Enter Salary: ")
            )

            programming_language = input(
                "Enter Programming Language: "
            )

            developer = Developer(
                employee_id,
                name,
                age,
                salary,
                programming_language
            )

            employees[employee_id] = developer

            print(
                "\nDeveloper Created Successfully!"
            )


        else:

            print("Invalid Choice")




    elif choice == "4":

        print("""
Choose Operation:

1. Show Person Details
2. Show Employee Details
3. Update Employee
4. Remove Employee
5. Check Inheritance
6. Back to Main Menu
""")

        sub_choice = input(
            "Enter Choice: "
        )


        if sub_choice == "1":

            if len(persons) == 0:

                print("No persons found.")

            else:

                for person in persons:

                    print("\nPerson Details")
                    print("----------------")

                    person.display()


        elif sub_choice == "2":

            if len(employees) == 0:

                print("No employees found.")

            else:

                employee_id = int(
                    input("Enter Employee ID: ")
                )

                if employee_id in employees:

                    employees[
                        employee_id
                    ].display()

                else:

                    print(
                        "Employee Not Found"
                    )

        elif sub_choice == "3":

            employee_id = int(
                input("Enter Employee ID: ")
            )

            if employee_id not in employees:

                print(
                    "Employee Not Found"
                )

            else:

                employee = employees[
                    employee_id
                ]

                print("""
Update Options:

1. Update Employee ID
2. Update Salary
""")

                update_choice = input(
                    "Enter Choice: "
                )


                if update_choice == "1":

                    new_id = int(
                        input(
                            "Enter New Employee ID: "
                        )
                    )

                    employee.set_employee_id(
                        new_id
                    )

                    employees[new_id] = employee

                    del employees[
                        employee_id
                    ]


                elif update_choice == "2":

                    new_salary = float(
                        input(
                            "Enter New Salary: "
                        )
                    )

                    employee.set_salary(
                        new_salary
                    )


                else:

                    print(
                        "Invalid Choice"
                    )


        elif sub_choice == "4":

            employee_id = int(
                input("Enter Employee ID: ")
            )

            if employee_id in employees:

                del employees[
                    employee_id
                ]

                print(
                    "Employee Removed Successfully!"
                )

            else:

                print(
                    "Employee Not Found"
                )


        elif sub_choice == "5":

            print("\nInheritance Check")
            print("-----------------")

            print(
                "Is Employee subclass of Person?",
                issubclass(
                    Employee,
                    Person
                )
            )

            print(
                "Is Manager subclass of Employee?",
                issubclass(
                    Manager,
                    Employee
                )
            )

            print(
                "Is Developer subclass of Employee?",
                issubclass(
                    Developer,
                    Employee
                )
            )

            print(
                "Is Person subclass of Employee?",
                issubclass(
                    Person,
                    Employee
                )
            )


    elif choice == "5":

        print(
            "\nThank you for using "
            "Employee Management System!"
        )

        print("Goodbye!")
        print("Person Class:")
        print(Person.__doc__)

        print("\nPerson.__init__():")
        print(Person.__init__.__doc__)

        print("\nPerson.display():")
        print(Person.display.__doc__)


        print("\nEmployee Class:")
        print(Employee.__doc__)

        print("\nEmployee.__init__():")
        print(Employee.__init__.__doc__)

        print("\nEmployee.get_employee_id():")
        print(Employee.get_employee_id.__doc__)

        print("\nEmployee.set_employee_id():")
        print(Employee.set_employee_id.__doc__)

        print("\nEmployee.get_salary():")
        print(Employee.get_salary.__doc__)

        print("\nEmployee.set_salary():")
        print(Employee.set_salary.__doc__)

        print("\nEmployee.display():")
        print(Employee.display.__doc__)

        print("\nEmployee.__del__():")
        print(Employee.__del__.__doc__)


        print("\nManager Class:")
        print(Manager.__doc__)

        print("\nManager.__init__():")
        print(Manager.__init__.__doc__)

        print("\nManager.display():")
        print(Manager.display.__doc__)


        print("\nDeveloper Class:")
        print(Developer.__doc__)

        print("\nDeveloper.__init__():")
        print(Developer.__init__.__doc__)

        print("\nDeveloper.display():")
        print(Developer.display.__doc__)


        break


    else:

        print(
            "Invalid Choice. Please try again."
        )