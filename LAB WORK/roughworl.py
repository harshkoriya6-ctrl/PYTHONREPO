class friend_data:
    
    def __init__(self, nameoffriend, gfs, gfsname):
        self.nameoffriend = nameoffriend
        self.gfs = gfs
        self.gfsname = gfsname

    def get_detail(self, name):
        if name == self.nameoffriend:
            print("Friend Name:", self.nameoffriend)
            print("Number of GFs:", self.gfs)
            print("GF Name:", self.gfsname)
        else:
            print("Friend not found")


friend = friend_data("Nihar", 5, "Chameli")

friend.get_detail("Nihar")


