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

        sid = input("Student ID: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        info = (sid, dob)
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        subjects = input("Subjects (Comma Separated): ")
        subject_set = set(subjects.split(","))
        info = (sid,dob)
        student = {
            "info": info,
            "name" : name,
            "Grade" : grade,
            "Age" : age,
            "sub" : subject_set,
        }

        stud.append(student)

        print("Student Added Successfully")

    elif choice == 2:
        print("Display All Students")
        if len(stud) == 0:
            print("Student Details Not Found")
        else:
            print("Students Record Found")

        for s in stud:
            print(f"""
Student ID : {s['info'][0]}
DOB        : {s['info'][1]}
Name       : {s['name']}
Age        : {s['Age']}
Grade      : {s['Grade']}
Subjects   : {", ".join(s['sub'])}
                """)

    elif choice == 3:
    
        sid = input("Enter Student ID: ")
        found = False

        for s in stud:
          if s["info"][0] == sid:
                
              print("Student Found")
              s["name"] = input("New Name: ")
              s["Age"] = int(input("New Age: "))
              s["Grade"] = input("New Grade: ")

              subjects = input("New Subjects: ")
              s["sub"] = set(subjects.split(","))

              print("Updated Successfully")
              print("Updated Details:",stud)
              found = True
              break
        if found == False:
           print("Student Not Found")

    elif choice == 4:
        sid = input("Enter Student ID: ")

        found = False

        for i in range(len(stud)):

            if stud [i]["info"][0] == sid:

                del stud [i]

                print("Student Deleted Successfully")

                found = True
                break

        if found == False:
            print("Student Not Found")

    elif choice == 5:
        all_subjects = set()
        for s in stud:
            for subject in s["sub"]:
                all_subjects.add(subject)
        print(", ".join(all_subjects))

    elif choice == 6:
        print("Exit The Code")
        break



    
         
        
                
    
             




