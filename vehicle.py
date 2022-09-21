"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""

class vehicle:
    my_vehicle = []
    def __init__(self, brand, model, color, maxspeed, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxspeed = maxspeed
        self.price = price
        self.my_vehicle.append(self)

    def vehicle_detail(self):
        print(f'Brand:{self.brand} '
              f'Model:{self.model} '
              f'Color:{self.color} '
              f'Maxspeed:{self.maxspeed} '
              f'Price:{self.price}')