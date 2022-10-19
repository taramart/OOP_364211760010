"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""

# Claww Relations - association
class student:
    #class attribute
    lst_teacher = list()
    def __init__(self,name,major,project):
        self.name = name
        self.major = major
        self.project = project
    def student_info(self):
        print(f'STD Name: {self.name} Major: {self.major}')
        print(f'Working on project: {self.project}')
        print(f'Advisor list: ')
        if len(self.lst_teacher) ==0:
            print("\tNo advison.")
        else:
            for x in self.lst_teacher:
                x.teacher_info()
    def add_advison(self,teacher):
        self.lst_teacher.append(teacher)

class teacher:
    lst_student = list()
    def __init__(self,name):
        self.name = name
    def teacher_info(self):
        print(f'teacher name: {self.name}')
    def add_advisee(self,student):
        self.lst_student.append(student)
    def advisee_info(self):
        if len (self.lst_student) ==0:
            print("Have no student.")
        else:
            for x in self.lst_student:
                print(x.name,x.project)

s1 = student("Taramart","MIT","KFC")
s2 = student("Atitaya","LM","LPG")

t1 = teacher("Few")
t2 = teacher("GOY")

s1.student_info()
s1.add_advison(t1)
s1.add_advison(t2)

s1.student_info()

t1.add_advisee(s1)
t1.add_advisee(s2)

t1.teacher_info()
t1.advisee_info()