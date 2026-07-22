# 1. Normalize

# sentence = input("Enter a Sentence: ")

# sentence = " ".join(sentence.split())
# sentence = sentence.lower()

# print("Normalized Sentence:", sentence)


# 2. Capitalize


# sentence = input("Enter a Sentence: ")

# words = sentence.split()

# for i in range(len(words)):
#     words[i] = words[i].capitalize()

# result = " ".join(words)

# print("Output:", result)


# 3. Remove Panctuation

# sentence = input("Enter Sentence:")
# result= " "

# for i in sentence:
#     if i.isalpha() or i == " ":
#         result= result + i

# print(result)           


# 4. Extract

# sentence = input("Enter Sentence:")
# result=""

# for i in sentence:
#     if i.isdigit():
#         result=result+i
# print(result)     
# 
# 

# 5. Extract Alphabets

# words=input("Enter Words:")
# result=""

# for i in words:
#     if i.isalpha():
#         result+=i
# print(result)        


# 6. Reverse Words

# sentence = input("Enter Sentence: ")

# word = sentence.split()

# word = word[::-1]

# result=" ".join(word)

# print("Output:", result)


# 7. Remove Duplicate

# sentence = input("Enter Sentence:")

# dup = sentence.split()

# for i in dup:
#     if dup.count(i)==2:
#         dup.remove(i)
# output=" ".join(dup)   
# print(output)     


# 8. Valid Email

# mail = input("Enter Email-id:")

# if mail.count("@")==1 and mail.endswith(".com") and mail.find(16)!= 1:
#     print("Email is Valid")
# else:
#     print("Invalid Mail")    
       


# 9. Number Mask

# number = input("Enter Phone Number:")

# print(list(number))
# print(number[:3],"*****",number[7:-1])



# 10. Convert sentence to snake_case

# sentence = input("Enter Sentence:")

# b=(sentence.lower())

# b = sentence.split()

# print("_".join(b))


# 11. Remove First And last

# sentence = input("Enter Sentence: ")

# a = sentence.split()

# for i in range(len(a)):
#     a[i] = a[i][1:-1]

# result = " ".join(a)
# print(result)



# 12. Find Longest Number

# sentence = input("Enter a Sentence: ")

# words = sentence.split()

# longest = words[0]

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print("Longest Word:", longest)



# 13. Count Words ignore Punctuation

# sentence = input("Enter a Sentence: ")

# result = ""

# for ch in sentence:
#     if ch.isalpha() or ch == " ":
#         result = result + ch

# words = result.split()

# print("Word Count:", len(words))



# 14.  Check if sentence is palindrome

# sentence = input("Enter a Sentence: ")

# sentence = sentence.replace(" ", "")

# if sentence == sentence[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


# 15. Toggle Case

# sentence = input("Enter a String: ")

# result = ""

# for ch in sentence:
#     if ch.isupper():
#         result = result + ch.lower()
#     elif ch.islower():
#         result = result + ch.upper()
#     else:
#         result = result + ch

# print("Output:", result)

#########################################################################


# Other Notion Task


# Task 1

# words = ["apple", "banana", "cherry"]

# count = 0

# for word in words:
#     for ch in word:
#         if ch in "aeiouAEIOU":
#             count += 1

# print("Total Vowels:", count)



# Task 2

# word = ["Helo","Harsh"]

# result = []

# for word in word:
#     result.append(word[::-1])

# print(result)


# Task 3


# word = ["cat", "elephant", "dog"]

# longest = word[0]

# for word in word:
#     if len(word) > len(longest):
#         longest = word

# print("Longest Word:", longest)



# Task 4

# word = ["Apple","Pooolo"]

# result = []

# for i in word:
#     newword=""

#     for j in i:
#         if j not in newword:
#                 newword=newword+j
#     result.append(newword)

# print(result)            


# Task 5

# word = ["apple", "dog", "elephant"]

# result = []

# for i in word:
#     if i[0] in "aeiouAEIOU":
#         result.append(i)
# print(result)





            