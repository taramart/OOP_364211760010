"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""


# polymorphism with inheritance

from math import pi
class shape:
    def area(self):
        pass

class Rectangle(shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length

class Circle(shape):
        def __init__(self, redius):
            self.rudius = redius
        def area(self):
            return pi*(self.rudius**2)

r = Rectangle(5.0,10.0)
c = Circle(7.7)

myshape = [r,c]

for x in myshape:
    print(x.area())

