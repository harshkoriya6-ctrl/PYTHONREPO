# QUE 1

# class Person:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# person1 = Person("Harsh", 24)
# person2 = Person("Nihar", 22)
# person3 = Person("Raj", 25)

# person1.display()
# person2.display()
# person3.display()



# QUE 2

# class Counter:
    
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         self.count += 1

#     def display(self):
#         print("Count:", self.count)


# c = Counter()

# c.increment()
# c.increment()
# c.increment()

# c.display()



# QUE 3

# class Student:
    
#     def display(self):
#         print("Hello")


# student = Student()

# student.display()



# QUE 4

# class Book:
    
#     def __init__(self, title, author):
#         self.__title = title
#         self.__author = author

#     def get_title(self):
#         return self.__title

#     def set_title(self, title):
#         self.__title = title

#     def get_author(self):
#         return self.__author

#     def set_author(self, author):
#         self.__author = author


# book = Book("Python Basics", "John")

# print("Title:", book.get_title())
# print("Author:", book.get_author())

# book.set_title("Advanced Python")

# print("Updated Title:", book.get_title())



# QUE 5

# class Account:
    
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print("Deposited:", amount)
#         else:
#             print("Invalid Amount")

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Insufficient Balance")
#         elif amount <= 0:
#             print("Invalid Amount")
#         else:
#             self.__balance -= amount
#             print("Withdrawn:", amount)

#     def display_balance(self):
#         print("Balance:", self.__balance)


# account = Account(10000)

# account.display_balance()

# account.deposit(2000)
# account.withdraw(3000)

# account.display_balance()



# QUE 6

# class Person:
    
#     def __init__(self, age):
#         self.__age = 0
#         self.set_age(age)

#     def get_age(self):
#         return self.__age

#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be greater than 0")


# person = Person(24)

# print("Age:", person.get_age())

# person.set_age(-5)

# print("Age:", person.get_age())



# QUE 7

# class Student:
    
#     def __init__(self, name, m1, m2, m3):
#         self.__name = name
#         self.__m1 = m1
#         self.__m2 = m2
#         self.__m3 = m3

#     def average(self):
#         return (self.__m1 + self.__m2 + self.__m3) / 3

#     def grade(self):
#         avg = self.average()

#         if avg >= 90:
#             return "A"
#         elif avg >= 75:
#             return "B"
#         elif avg >= 60:
#             return "C"
#         elif avg >= 40:
#             return "D"
#         else:
#             return "F"

#     def display(self):
#         print("Name:", self.__name)
#         print("Average:", self.average())
#         print("Grade:", self.grade())


# student = Student("Harsh", 85, 78, 90)

# student.display()


