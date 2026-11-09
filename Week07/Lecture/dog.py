class Dog:
    breed = "Poodle" # class variable
    friends = []

    def __init__(self, name):
        self.name = name # instance variable
        self.closeFriends = []

    def addNewFriend(self, friend):
        self.friends.append(friend)
    
    def addNewCloseFriend(self, friend):
        self.closeFriends.append(friend)
    
    def printFriends(self):
        print("Friends for", self.name, "is", self.friends)
    
    def printCloseFriends(self):
        print("Close Friends for", self.name, "is", self.closeFriends)