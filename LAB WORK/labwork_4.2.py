# QUE 1

# def factorial(n):
#     if n < 0:
#         return "Factorial is not possible for nagative number"
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# n = int(input("Enter Number: "))
# print("Factorial:",factorial())



# QUE 2

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci (n-2)

# n=int(input("Enter Number:"))
# print("Fibonacci:",fibonacci(n))



# QUE 3

# def reverse_str(s):
#     if len(s) == 0:
#         return s
#     return reverse_str(s[1:])+s[0]

# word =input("Enter string:")
# print("Reversed string:",reverse_str(word))


# QUE 4

# def singl_digitsum(n):
#     if n < 10:
#         return n
#     total = 0

#     while n > 0:
#         total+= n%10
#         n //= 10 
#     return singl_digitsum(total)

# n=int(input("Enter Number:"))
# print("Sum is:",singl_digitsum(n))



# QUE 5

# def prime_num(n, i=2):
#     if n < 2:
#         return False
#     if i * i < n:
#         return True
#     if n % i == 0:
#         return False
#     return prime_num(n, i+1)

# def print_prime(start, end):
#     if start > end :
#         return 
#     if prime_num(start, end):
#         print(start, end=" ")
#     print_prime(start+1, end)

# start = int(input("Enter start Num: "))
# end = int(input("Enter end Num: "))

# print("prime Numbers:")
# print_prime(start, end)



# QUE 6

# square = lambda x: x * x

# numbers = list(map(int, input("Enter numbers: ").split()))

# result = list(map(square, numbers))

# print("Squares:", result)



# QUE 7

# numbers = list(map(int, input("Enter numbers: ").split()))

# result = list(filter(lambda x: x % 2 != 0, numbers))

# print("Odd numbers:", result)



# QUE 8

# largest = lambda a, b, c: max(a, b, c)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# print("Largest:", largest(a, b, c))



# QUE 9

# count = 0


# def my_function():
#     global count
#     count += 1
#     print("Function called")


# my_function()
# my_function()
# my_function()

# print("Function called", count, "times")



# QUE 10

# total = 0
# def add_number(n):
#     global total
#     total += n


# for i in range(5):
#     n = int(input("Enter number: "))
#     add_number(n)

# print("Sum of all numbers:", total)



# QUE 11

# username = "Guest"

# def update_name():
#     global username
#     username = input("Enter new username: ")


# print("Old username:", username)

# update_name()

# print("New username:", username)



# QUE 12

# count = 0


# def initialize():
#     global count
#     count = 0


# def increment():
#     global count
#     n = int(input("Enter value to increment: "))
#     count += n


# initialize()

# increment()
# increment()

# print("Final value:", count)



# QUE 13

# name = "Global"


# def show_name():
#     name = "Local"
#     print("Inside function:", name)


# print("Outside function:", name)

# show_name()

# print("Outside function:", name)



# QUE 14

# name = "Global"


# def show_name():
#     name = "Local"
#     print("Inside function:", name)


# print("Outside function:", name)

# show_name()

# print("Outside function:", name)



# QUE 15

# def calculate(numbers):
#     total = sum(numbers)
#     maximum = max(numbers)
#     minimum = min(numbers)

#     return total, maximum, minimum


# numbers = list(map(int, input("Enter numbers: ").split()))

# total, maximum, minimum = calculate(numbers)

# print("Sum:", total)
# print("Maximum:", maximum)
# print("Minimum:", minimum)



# QUE 16

# def rectangle(length, width):
#     area = length * width
#     perimeter = 2 * (length + width)

#     return area, perimeter


# length = float(input("Enter length: "))
# width = float(input("Enter width: "))

# area, perimeter = rectangle(length, width)

# print("Area:", area)
# print("Perimeter:", perimeter)



# QUE 17

# def split_string(text):
#     vowels = ""
#     others = ""

#     for ch in text:
#         if ch.lower() in "aeiou":
#             vowels += ch
#         else:
#             others += ch

#     return vowels, others


# text = input("Enter a string: ")

# vowels, others = split_string(text)

# print("Vowels:", vowels)
# print("Remaining characters:", others)


# QUE 18

# def separate_words(words):
#     vowel_words = []
#     consonant_words = []

#     for word in words:
#         if word[0].lower() in "aeiou":
#             vowel_words.append(word)
#         else:
#             consonant_words.append(word)

#     return vowel_words, consonant_words


# words = input("Enter words: ").split()

# vowel_words, consonant_words = separate_words(words)

# print("Words starting with vowels:", vowel_words)
# print("Words starting with consonants:", consonant_words)












