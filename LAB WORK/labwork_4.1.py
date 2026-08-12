# QUE 1

# l=[]

# for i in range (5):
#     num=int(input("Enter Number"))
#     l.append(num)
# print(len(l))
# print(max(l))
# print(sorted(l))
# print(sum(l))
# print(type(l))



# QUE 2

# def fact(a):
#     fact = 1
#     for i in range(1,a+1):
#         fact = fact*i
#     return fact
# print("Fcatorial is:",fact(5)) 



# QUE 3

# def sqr(a):
#     sql = [i**2 for i in a]
#     return sql
# lst=[int(input("Enter the element:"))for i in range(5)]
# print(sqr(lst))



# QUE 4

# def freq(a):
#     d={}

#     for i in a:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
# str = input("Enter string: ")
# res= freq(str)
# print(res)



# QUE 5

# def sqr(a):
#     cub = [i**3 for i in a]
#     return cub
# lst=[int(input("Enter the element:"))for i in range(5)]
# print(sqr(lst))



# QUE 6

# def calc(*args):
#     ttl = 0
#     prdt = 1

#     for i in args:
#         ttl+=i
#         prdt=i
#     return (ttl,prdt)
# a,p=calc(1,2,3,4,5)
# print("Sum:",a)
# print("Total:",p)



# QUE 7

# def stdnts(*args):

#     if args == 0:
#         print("Student list is Empty")
#     else:
#         for i in args:
#             print(i)
# stdnts("Harsh","Meet","Nihar","Deep","jay")



# QUE 8

# def sprt(*args):
#     stri =[]
#     numb=[]
#     for i in args:
#         if type(i) == str:
#             stri.append(i)
#         else:
#             type(i) == int or type(i) == float
#             numb.append(i)
#     return tuple(stri),tuple(numb)
# s,n = sprt("Harsh",10,"dusbu",56,"hdsvyusd")
# print("String:",s)
# print("Numbers:",n)



# QUE 9

# def descr(**kwargs):
#     print("Name:",kwargs["name"])
#     print("Age:",kwargs["age"])
#     print("City:",kwargs["city"])

# descr(name="Harsh",age=10,city="Ahmedabad")



# QUE 10

# def prod(**kwargs):
#     p = kwargs["price"]
#     q = kwargs["quantity"]
#     t = p*q
#     return t
# print(prod(name="kiwi",price=800,quantity=200))
# print(prod(name="Toothpaste",price=500,quantity=100))
# print(prod(name="Malkist",price=600,quantity=50))
# print(prod(name="Almond",price=700,quantity=300))



# QUE 11

# def employee(**kwargs):
    
#     if "name" not in kwargs:
#         print("Name is missing")

#     elif "department" not in kwargs:
#         print("Department is missing")

#     elif "salary" not in kwargs:
#         print("Salary is missing")

#     else:
#         print("Employee Details")

#         for key, value in kwargs.items():
#             print(key, ":", value)


# employee(name="Harsh", department="Data Scientist", salary=250000)



# QUE 12

# def area(length,width):
#     '''
#     Function Name : area

#     Purpose : Calculates the area of rectangle

#     parameter : 
#     length - length of rectangle
#     width - width of rectangle

#     Return : length*width
#     '''

#     return length*width
# l=int(input("Enter Length:"))
# w=int(input("Enter width:"))

# print("Area of Reactangle:",area(l,w))

# print(area.__doc__)



# QUE 13

# def fibonacci(n):
#     '''Function Name : area

#     Purpose : Return the Fibonacci sequence up to given number

#     parameter : 
#     N (given Numbers)

#     input:
#     Number of terms in fibonacci seriese
    
#     output :
#     Returns a list containing thr fibonacci sequence

#     '''
#     a=0
#     b=1
#     ans=[]
#     for i in range(n):
#         ans.append(a)
#         c=a+b
#         a=b
#         b=c
#     return ans
# value=int(input("Enter Number: "))
# print("Fibonacci:",fibonacci(value))
# print(fibonacci.__doc__)







        





    


