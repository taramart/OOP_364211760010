"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""

class Labtop:
    def __init__(self, Brand, Model, cpu, ram, display, storage, price):
        # attributes
        self.__Brand = Brand  # private member
        self.__Model = Model  # private member
        self.__cpu = cpu
        self.__ram = ram
        self.__display = display
        self.__storage = storage
        self.__price = price

    def get_Brand(self):
        return self.__Brand
    def set_Brand(self, Brand):
        self.__Brand = Brand

    def get_Model(self):
        return self.__Model
    def set_Model(self, Model):
        self.__Model = Model

    def get_cpu(self):
        return self.__cpu
    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_ram(self):
        return self.__ram
    def set_ram(self, ram):
        self.__ram = ram

    def get_display(self):
        return self.__display
    def set_display(self, display):
        self.__display = display

    def get_storage(self):
        return self.__storage
    def set_storage(self, storage):
        self.__storage = storage

    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

    def __str__(self):
        print(f'Brand: {self.__Brand} Modem:{self.__Model} cpu:{self.__cpu} ram:{self.__ram} '
              f'display:{self.__display} storage:{self.__storage} price:{self.__price}')

s = Labtop("acer","1234","128","456","d","1tb","23000")
s.__str__()

print(s.get_Brand())
s.set_Brand("goy")

print(s.get_Brand())

print(s.get_cpu())