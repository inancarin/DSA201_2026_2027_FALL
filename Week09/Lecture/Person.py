class Person: # super/parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return "A person whose name is " + self.name + " and age is " + str(self.age)
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
class Student(Person): # sub/child class
    def __init__(self, name, age, studentID, university="Sabanci University"):
        """
        self.name = name
        self.age = age
        """
        super().__init__(name, age)
        self.id = studentID
        self.university = university

    def __str__(self):
        return "A student whose name is " + self.name + " studies in " + self.university

# main
p1 = Person("John", 22)
p2 = Person("Alice", 23)
#print(p2)

s1 = Student("Bob", 18, 1, "Koc University")
s2 = Student("Rose", 20, 2)
print(p1)
print(s2)