"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""

class student:
    #class attributes
    uni = "RUTS"

    def __init__(self,name,id,major):
        # object attributes
        self.name = name
        self.id = id
        self.major = major

    def introduce(self):
        print(f'My name is {self.name},my id is {self.id},and I am studying in {self.major} major.')




s1 = student("Taramart Kaewmanee","3642211760010","MIT")
s1.introduce()

s2 = student("atitaya darakai","364211860008","LM")
s2.introduce()

s1.major = "AC"
s1.introduce()

print(s1.uni)
print(s2.uni)

student.uni = "PSU"
print(s1.uni)
print(s2.uni)