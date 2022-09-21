"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""

class EV_Car:
    my_EV_Car = []

    def __init__(self, brand, model, motor, Horse_Power, Battery_Size, Range, price):
        self.brand = brand
        self.model = model
        self.Motor = motor
        self.Horse_Power = Horse_Power
        self.Battery_Size = Battery_Size
        self.Range = Range
        self.price = price
        self.my_EV_Car.append(self)

    def display_ev_car(self):
        print(f'Brand:{self.brand} '
              f'Model:{self.model} '
              f'Motor:{self.motor} '
              f'Horse_Power:{self.Horse_Power} '
              f'Battery_Size:{self.Battery_Size} '
              f'Range:{self.Range} '
              f'Price:{self.price}')