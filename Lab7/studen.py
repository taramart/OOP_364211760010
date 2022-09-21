"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""

class Student:
    def __init__(self,name,id):
        # attributes
        self.name = name #public member
        self.__id = id  #private member
    def __str__(self):
        print(f'Name: {self.name} ID:{self.__id}')

std = Student("Taramart","010")
# direct access
#print(std.name,std.id)
std.__str__()
std.name ="Athitaya" # change data attribute
std.__str__()

std.__id = "017"
std.__str__()

#name mangling
print(std._Student__id)
std._Student__id = "017"
std.__str__()