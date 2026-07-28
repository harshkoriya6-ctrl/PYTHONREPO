stud =[]
while True:
    print("Welcome to the Student Data Organizer!")
    print("""Select an Option
    1. Add Student
    2. Display All Student
    3. Update Student information
    4. Delete Student
    5. Display Subjects Offered
    6. Exit""")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        print("Enter Student Details:")

        rid = int(input("Enter Id Number: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))
        age = int(input("Enter Age: "))
        sub = input("Enter Suject: ")

        student = {
            "id" : rid,
            "Marks" : marks,
            "age" : age,
            "sub" : sub,
        }

        stud.apppend(student)

        print("Student Added")

    elif choice == 2:
        print("Display All Students")



