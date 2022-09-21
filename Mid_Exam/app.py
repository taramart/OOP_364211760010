from EV import EV_Car


#display
def display_ev_car():
    if len(my_EV_Car) == 0:
        print("You had no vehicle data.")
    else:
        print(f'You had {len(my_EV_Car)} following:')
        for x in my_EV_Car:
            x.vehicle_detail()
        print("\n")

# option
    def display_option_system():
        print("Welcome to Vehicle Data Store System (VDSS)")
        print("1.Add EV_Car")
        print("2.Display all EV_Car")
        print("3.exit")
        select = int(input("select(1-3)? : "))
        if select == 1:
            input_evcar_data()
        elif select == 2:
            display_ev_car()
        elif select == 3:
            print("Thank You Good Bye.")
            exit(0)
        else:
            print("Please, select number 1-3.")


# input data
    def input_evcar_data():
        brand = input("Enter vehicle brand: ")
        model = input("Enter vehicle model: ")
        motor = input("Enter vehicle Motor: ")
        Horse_Power = input(int("Enter vehicle Horse_Power: "))
        Battery_Size = input(int("Enter vehicle Battery_Size: "))
        Range = int(input("Enter vehicle Range:"))
        price = float(input("Enter vehicle price:"))

#return brand, model, Motor, Horse_Power, Battery_Size, Range, price #return as tuple
    my_EV_Car.append(EV_Car(brand, model, motor, Horse_Power, Battery_Size, Range, price))
    print("\n-----------------------------")
    print("Already add vehicle to store.")
    print("\n-----------------------------")

my_EV_Car = []
s = 0
while s == 0:
    display_ev_car()

