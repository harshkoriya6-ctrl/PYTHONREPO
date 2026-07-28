while True:
    print("Welcome to format generator and Number Analyzer")
    print("""Select Optoin
    1. Generate Pattern
    2. Analyze a range of Numbes
    3. exit""")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        UserInput=int(input("Enter number of rows for the patterns:"))
        for i in range(1, UserInput + 1):
            for j in range(i):
               print("*", end="")
            print("")
    elif choice==2:
        a=int(input("Enter the start of the range:"))
        b=int(input("Enter the end of the range:" ))
        sum=0
        for i in range (a,b+1):
            sum=a+b
            if i % 2==0:
                print(f'Number {i} is even')
            else:
                print(f'Number {i} is odd') 
        print(f'Sum of all Numbers from {a} to {b} is {sum}')  

    elif choice==3:
        print("Exiting The Programe. Good Bye!")
        break
    
        

    


    