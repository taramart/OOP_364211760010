"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""

# Class Relation - inheritance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def person_info(self):
        print(f'name: {self.name} Age: {self.age}')

class student(Person):
    def __init__(self,name,age,major,gpa):
        #1
        Person.__init__(self,name,age)
        #2
        super().__init__(name,age)
        self.major = major
        self.gpa = gpa
    def student_info(self):
        self.person_info()
        print(f'Major: {self.major} GPA:{self.gpa}')

# create object
p1 = Person("Taramart",20)
s1 = student("jantira",20,"MIT","3.80")

p1.person_info()
s1.person_info()

s1.student_info()