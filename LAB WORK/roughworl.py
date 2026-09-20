# class friend_data:
    
#     def __init__(self, nameoffriend, gfs, gfsname):
#         self.nameoffriend = nameoffriend
#         self.gfs = gfs
#         self.gfsname = gfsname

#     def get_detail(self, name):
#         if name == self.nameoffriend:
#             print("Friend Name:", self.nameoffriend)
#             print("Number of GFs:", self.gfs)
#             print("GF Name:", self.gfsname)
#         else:
#             print("Friend not found")


# friend = friend_data("Nihar", 5, "Chameli")
 
# friend.get_detail("Nihar")




# #############################


cls = [0, 10, 20, 30, 40]

frnht = [x for x in map(lambda C : C * 9/5 + 32, cls )]

print(frnht)




num = [12, 5, 8, 23, 16, 4, 42, 7]

evn = [x for x in filter(lambda x: x % 2 == 0, num)]

rslt = sorted(evn, reverse=True)

print(rslt)


num = [12, 5, 8, 23, 16, 4, 42, 7]

# maxnum = max(num)

# print(maxnum)


maxnum = num[0]

for i in num:
    if i > maxnum:
        maxnum = i

print(maxnum)


from functools import reduce

words = ["Python", "is", "awesome", "and", "powerfull"]

fltr = list(filter(lambda word: len(word) > 3, words))

print(fltr)
