from person import Person
#import person as p

p1 = Person(name="John", age=25) # creating a new instance
print(p1.myName, p1.age)
p2 = Person("Jack") # creating another instance
#p2.age = "inanc"
p2.changeAge(14)
print(p2.getName(), p2.getAge())
print(p1)
print(p2)

"""
society = []
society.append(p1)
society.append(p2) # society = [p1, p2]
print(society)
"""