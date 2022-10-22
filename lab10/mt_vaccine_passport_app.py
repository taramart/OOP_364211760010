"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""

from mdel import Person,Student,Vaccine,Vaccine_Passport

p1 = Person("Taramart",22,65,160)

v1 = Vaccine("Sionvac")
d1 = "30/5/2564"

vp1 = Vaccine_Passport(p1)
vp1.vaccine_passport_info()

vp1.add_vaccine(v1)
vp1.add_date(d1)

vp1.vaccine_passport_info()

v2 = Vaccine("Sionvac")
d2 = "30/8/2564"

vp1.add_vaccine(v2)
vp1.add_date(d2)

vp1.vaccine_passport_info()

s1 = Student("Athitaya",22,50,173,"LM")

v3 = Vaccine("Sionvac")
d3 = "17/10/2565"

vp2 = Vaccine_Passport(s1)
vp2.add_vaccine(v3)
vp2.add_date(d3)

vp2.vaccine_passport_info()

