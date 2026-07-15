for i in range(5):
    a=int(input("enter first number :"))
    b=int(input("enter secont number:"))
    c=int(input("enter third number :"))
    if a==b:
        print("a and b are equal")
        if c>a :
            print("c is greatest")
    elif a==c:
        print("a and c are equal")
        if b>a :
            print("c is greatest")
    elif b==c:
        print("c and b are equal")
        if a>b :
            print("c is greatest")
    elif a>b:
        if a>c:
            print("a is greatest")
        else:
            print("c is greatest")
    elif b>a:
        if b>c:
            print("b is greatest")
        else:
            print("c is greatest")
    elif a>c:
        if a>b:
            print("a is greatest")
        else:
            print("b is greatest")  
    else:
        print("all are equal")