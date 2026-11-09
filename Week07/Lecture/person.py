class Person:
    def __init__(self, name, age=20): # constructor
        self.myName = name
        self.age = age
    
    def __str__(self):
        return "Name: " + self.myName + ", Age: " + str(self.age)

    def __repr__(self):
        return self.myName + " - " + str(self.age)
    
    # setter
    def changeAge(self, newAge):
        if isinstance(newAge, int):
            if newAge > 0:
                self.age = newAge
            else:
                print("Age must be a positive integer!")
        else:
            print("Age must be an integer!")
    
    # getter
    def getAge(self):
        return self.age
    
    # getter
    def getName(self):
        return self.myName