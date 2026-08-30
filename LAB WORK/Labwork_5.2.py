# QUE 1

# class Student:
    
#     def __init__(self, name):
#         self.name = name
#         print(self.name, "Object Created")

#     def __del__(self):
#         print(self.name, "Object Deleted")


# student1 = Student("Harsh")
# student2 = Student("Nihar")
# student3 = Student("Raj")

# del student1
# del student2
# del student3



# QUE 2

# class Animal:
    
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print("Animal Name:", self.name)


# animal = Animal("Dog")

# animal.display()



# QUE 3

# class Rectangle:
    
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# rectangle = Rectangle(10, 5)

# print("Length:", rectangle.length)
# print("Width:", rectangle.width)
# print("Area:", rectangle.area())



# QUE 4

# class Employee:
    
#     def __init__(self):
#         self.name = "Harsh"
#         self.id = 101
#         self.salary = 25000

#         print("Employee Created")

#     def display(self):
#         print("Name:", self.name)
#         print("ID:", self.id)
#         print("Salary:", self.salary)

#     def __del__(self):
#         print("Employee Object Deleted. Goodbye!")


# employee = Employee()

# employee.display()

# del employee


# QUE 5

# class Student:
    
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)

#     def result(self):
#         if self.marks >= 40:
#             print("Result: Pass")
#         else:
#             print("Result: Fail")


# student = Student("Harsh", 24, 85)

# student.display()
# student.result()