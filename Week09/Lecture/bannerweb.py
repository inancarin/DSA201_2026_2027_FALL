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
    
class FacultyMember(Person):
    pass

class Student(Person): # sub/child class
    def __init__(self, name, age, studentID, university="Sabanci University"):
        super().__init__(name, age)
        self.id = studentID
        self.university = university
        self.courses = [] # a list of course objects

    def __str__(self):
        return "A student whose name is " + self.name + " studies in " + self.university

    def register(self, course):
        if course in self.courses:
            print("You've already enrolled in the course, not proceed.")
        else:
            if course.isFull():
                print("Sorry, there is no available seats in the class, not proceed!")
            else:
                self.courses.append(course)
                course.currentPopulation += 1
                print(self.name, "registered for", course.name)
    
    def drop(self, course): # homework for you
        pass

    def printAllRegisteredCourses(self):
        if len(self.courses) == 0:
            print("You haven't registered for any course yet")
        else:
            print("The courses registered by", self.name, ":")
            for course in self.courses:
                print(course)

class Course:
    def __init__(self, code, name, CRN, capacity, classroom="UC G030"):
        self.code = code
        self.name = name
        self.CRN = CRN
        self.capacity = capacity
        self.room = classroom
        self.currentPopulation = 0
    
    def __str__(self):
        return str(self.CRN) + " " + self.code + " " + self.name
    
    def isFull(self):
        return self.currentPopulation == self.capacity
 

s1 = Student("Ahmet Korkmaz", 20, 1, "Sabanci University")
s2 = Student("Elif Candan", 21, 2, "Sabanci University")
s3 = Student("Aslan Akbey", 24, 3)

dsa201 = Course("DSA201", "Advance Programming for Data Science", 10021, 2, "UC G030")
if100 = Course("IF100", "Computational Approaches to Problem Solving", 10001, 4, "FENS G077")

s1.register(dsa201)
s2.register(dsa201)
s3.register(dsa201)

s1.register(if100)
s1.register(if100)

s1.printAllRegisteredCourses()