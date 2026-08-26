# def prime(x):
#     global s
#     count = 0 
#     i = 1
#     while s <= x:
#         if x % i == 0:
#             count += 1
#         i+=1

#         if count == 2:
#             if x < s:
#                 x+=2
#             else:
#                 s-=1
#                 if s==0:  
#                     print(x)  
#                 else:
#                     x+=2
#         else:
#             x+=2

# def lgc(x):
#     if x % 2 == 0:
#         x+=1
#     while s > 0:
#         x = prime(x)

# s = 15
# x = int(input("Enter Number: "))
# l(x)

def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True

def main():
    S = 15
    x = int(input("Enter x: "))

    while True:

        
        if x % 2 == 0:
            x = x + 1

        
        if not is_prime(x):
            x = x + 2
            continue

      
        if x < S:
            S = S - x
            x = x + 2
        else:
            S = S - 1

        
        if S == 0:
            print("Output x =", x)
            break


main()

