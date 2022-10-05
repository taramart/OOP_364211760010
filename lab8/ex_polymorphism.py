"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""

# polymorphism - การพ้องรูป

# functoin polymorphism
l = {1,2,3,4,5}
x = 100
print(l)
print(x)
s ="RUTS"
print(len(l))
print(len(s),s[2])

# polymorphism with class method
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f' I am a cat, my name is {self.name}'
              f' I am {self.age} year old.')

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f' I am a cat, my name is {self.name}'
              f' I am {self.age} year old.')

# create object

c = Cat("mumu",2)
d = Dog("lulu",5)

animal = [c,d]
for x in animal:
    x.info()
    
