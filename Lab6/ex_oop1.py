"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def my_gog(self):
        print(f'My dog name is {self.name} and it {self.age} year old.')


d1 = Dog("meetang",10)
print(d1.name)
print(d1.age)

d2 = Dog("lulu",12)
print(d2.name)
print(d2.age)
d1.my_gog()
d2.my_gog()