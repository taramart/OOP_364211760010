"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""

# Class Relations - Dependency

from datetime import date
class Customer:
    def __init__(self,cusid,name):
        self.cusid = cusid
        self.name = name

    def customer_info(self):
        return f'CusID: {self.cusid} Customer name: {self.name}'

class Order:
    def __init__(self,orderid,date,Customer,total):
        self.orderid = orderid
        self.date = date
        self.customer = Customer
        self.total = total

    def order_info(self):
        print("order description:")
        print(f'\tcustomer info: {self.customer.customer_info()}')
        print(f'\tDate: {self.date}')
        print(f'\ttotal cost: {self.total}')

# create objact
cus1 = Customer("CUS001","Taramart")

order1 = Order("ORDER001",date.today(),cus1,1500)
order1.order_info()