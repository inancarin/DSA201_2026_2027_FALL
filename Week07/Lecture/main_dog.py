from dog import Dog

d1 = Dog("Rosie")
d2 = Dog("Rocky")

d1.addNewFriend("Kont")

d1.printFriends()
d2.printFriends()

d1.addNewCloseFriend("Kont")
d1.printCloseFriends()
d2.printCloseFriends()