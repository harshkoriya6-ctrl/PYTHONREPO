# QUE 1

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     print(*row, sep="\t")


# QUE 2

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# print("Main matrix")

# for row in matrix:
#     print(*row)
# transpose=[]

# for i in range(3):
#     row=[]

#     for j in range(2):
#         row.append(matrix[j][i])
#     transpose.append(row)
   

# print("Transpose Matrix")

# for row in transpose:
#     print(*row)



# QUE 3

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# total = 0

# for i in matrix:
#     for j in i:
#         total += j

# print("Sum of Matrix is: ",total)


# QUE 4

# matrix = [
#     [10, 5, 20],
#     [8, 30, 15],
#     [2, 25, 12]
# ]

# maximum = matrix[0][0]
# minimum = matrix[0][0]

# for row in matrix:
#     for value in row:
#         if value > maximum:
#             maximum = value

#         if value < minimum:
#             minimum = value

# print("Maximum:", maximum)
# print("Minimum:", minimum)



# QUE 5

# numbers = [5, 2, 8, 1, 9, 3]

# numbers.sort()

# print("Ascending Order:", numbers)



# QUE 6

# data = [
#     ("Harsh", 25),
#     ("Nihar", 18),
#     ("Raj", 30),
#     ("Amit", 20)
# ]

# result = sorted(data, key=lambda x: x[1])

# print("Sorted Data:")

# for item in result:
#     print(item)



# QUE 7

# employees = [
#     {"name": "Harsh", "salary": 30000},
#     {"name": "Nihar", "salary": 25000},
#     {"name": "Raj", "salary": 40000},
#     {"name": "Amit", "salary": 20000}
# ]

# result = sorted(employees, key=lambda x: x["salary"])

# print("Employees Sorted by Salary:")

# for employee in result:
#     print(employee)



# QUE 8

# numbers = [5, 2, 8, 1, 9, 3]

# print("Original List:", numbers)

# numbers.sort()

# print("After sort():", numbers)

# numbers = [5, 2, 8, 1, 9, 3]

# new_numbers = sorted(numbers)

# print("Original List after sorted():", numbers)
# print("New List:", new_numbers)



