# QUE - 1

# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# c = int(input("Enter Third Number: "))

# if a > b:
#     if a > c:
#         print("Maximum Number:", a)
#     else:
#         print("Maximum Number:", c)
# else:
#     if b > c:
#         print("Maximum Number:", b)
#     else:
#         print("Maximum Number:", c)

# QUE - 2

# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# c = int(input("Enter Third Number: "))

# if a < b:
#     if a < c:
#         print("Minimum Number is",a)
#     else:
#         print("Minimum Number is",c)
# else:
#     if b < a:
#         if b < c:
#             print("Minimum Number",b)
#         else:
#             print("Minimum Number",c)    
# 
# QUE - 3
 
# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# c = int(input("Enter Third Number: "))
# d = int(input("Enter Fourth Number: "))

# if a > b:
#     if a > c:
#         if a > d:
#             print("Maximum Number:", a)
#         else:
#             print("Maximum Number:", d)
#     else:
#         if c > d:
#             print("Maximum Number:", c)
#         else:
#             print("Maximum Number:", d)
# else:
#     if b > c:
#         if b > d:
#             print("Maximum Number:", b)
#         else:
#             print("Maximum Number:", d)
#     else:
#         if c > d:
#             print("Maximum Number:", c)
#         else:
#             print("Maximum Number:", d)       

# QUE - 4

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# op = input("Enter Operator (+,-,*,/): ")

# match op:
#     case "+":
#         print("Result =", num1 + num2)

#     case "-":
#         print("Result =", num1 - num2)

#     case "*":
#         print("Result =", num1 * num2)

#     case "/":
#         print("Result =", num1 / num2)

#     case _:
#         print("Invalid Operator")


# QUE - 5

# print("1. Sandwich")
# print("2. Pizza")
# print("3. Burger")

# choice = int(input("Enter Your Choice: "))

# match choice:

#     case 1:
#         print("1. Veg Sandwich")
#         print("2. Cheese Sandwich")
#         print("3. Grilled Sandwich")

#         sub = int(input("Select Sandwich Type: "))

#         match sub:
#             case 1:
#                 print("You Ordered Veg Sandwich")
#             case 2:
#                 print("You Ordered Cheese Sandwich")
#             case 3:
#                 print("You Ordered Grilled Sandwich")
#             case _:
#                 print("Invalid Choice")

#     case 2:
#         print("1. Thin Crust Pizza")
#         print("2. Cheese Burst Pizza")
#         print("3. Fresh Dough Pizza")

#         sub = int(input("Select Pizza Type: "))

#         match sub:
#             case 1:
#                 print("You Ordered Thin Crust Pizza")
#             case 2:
#                 print("You Ordered Cheese Burst Pizza")
#             case 3:
#                 print("You Ordered Fresh Dough Pizza")
#             case _:
#                 print("Invalid Choice")

#     case 3:
#         print("1. Veg Burger")
#         print("2. Cheese Burger")
#         print("3. Double Patty Burger")

#         sub = int(input("Select Burger Type: "))

#         match sub:
#             case 1:
#                 print("You Ordered Veg Burger")
#             case 2:
#                 print("You Ordered Cheese Burger")
#             case 3:
#                 print("You Ordered Double Patty Burger")
#             case _:
#                 print("Invalid Choice")

#     case _:
#         print("Invalid Main Menu Choice")


# QUE - 6

# language = int(input("""
# Select Language
# 1. English
# 2. Hindi
# 3. Gujarati
# Enter your choice: """))

# match language:

#     case 1:
#         print("\nEnglish Selected")
#         option = int(input("""
# 1. Recharge
# 2. Balance Check
# 3. Talk to Customer Care
# Enter your choice: """))

#         match option:
#             case 1:
#                 print("Recharge Successful.")
#             case 2:
#                 print("Your Balance is Rs. 250")
#             case 3:
#                 print("Connecting to Customer Care...")
#             case _:
#                 print("Invalid Choice")

#     case 2:
#         print("\nHindi Selected")
#         option = int(input("""
# 1. Recharge
# 2. Balance Check
# 3. Customer Care
# Enter your choice: """))

#         match option:
#             case 1:
#                 print("Recharge Safal Hua.")
#             case 2:
#                 print("Aapka Balance Rs. 250 Hai.")
#             case 3:
#                 print("Customer Care Se Joda Ja Raha Hai...")
#             case _:
#                 print("Galat Choice")

#     case 3:
#         print("\nGujarati Selected")
#         option = int(input("""
# 1. Recharge
# 2. Balance Check
# 3. Customer Care
# Enter your choice: """))

#         match option:
#             case 1:
#                 print("Recharge Safal Thayo.")
#             case 2:
#                 print("Tamaro Balance Rs. 250 Chhe.")
#             case 3:
#                 print("Customer Care Sathe Connect Thai Rahyu Chhe...")
#             case _:
#                 print("Khoti Choice")

#     case _:
#         print("Invalid Language Selection")

