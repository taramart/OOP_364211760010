"""
Name: Taramart Kaewmanee
ID: 364211760010
Group: MIT221
"""

# class Relation - composition

class faculty:
    def __init__(self,fac_name):
        self.fac_name = fac_name
    def fac_info(self):
        print(f'Facylty name: {self.fac_name}')

class university:
    lst_faculty = list()
    def __init__(self,uniname):
        self.uniname = uniname
        self.get_faculty()
    def uni_info(self):
        print(f'university name: {self.uniname}')
        print(f'has faculty below:')
        if len(self.lst_faculty) ==0:
            print(f'Has no faculty.')
        else:
            for x in self.lst_faculty:
                x.fac_info()

    def get_faculty(self):
        f1 = faculty("MT")
        f2 = faculty("Sci-Tech")

        self.lst_faculty.append(f1)
        self.lst_faculty.append(f2)

u1 = university("RUTS")

u1.uni_info()

u1.lst_faculty[0].fac_info()