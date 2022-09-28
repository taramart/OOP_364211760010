from labtop import labtop

def display_laptop(): #แสดงข้อมูล laptop
    if len(my_labtop) == 0:
        print("คุณยังไม่มีรายการ")
    else:
        num = 1
        print(f'คุณมีรายการ {len(my_labtop)} จำนวน:')
        for x in my_labtop:
            print(f'{num}. ',end="")
            x.display_labtop()
            num +=1
        print("\n")

def display_option_system(): #แสดงตัวเลือกให้ผู้ใช้เลือกใช้ฟังก์ชั่น
    print("Welcome to Labtop Store System")
    print("1.เพิ่มข้อมูล Labtop")
    print("2.แสดงข้อมูล Laptop")
    print("3.ลบข้อมูล")
    print("4.แก้ไขราคา")
    print("5.ออกจากระบบ")
    select = int(input("กรุณาเลือกตัวเลข 1-5?: "))
    if select == 1:
        input_laptop_data()
    elif select == 2:
        display_laptop()
    elif select == 3:
        delete_labtop()
    elif select == 4:
        edit_labtop_price()
    elif select == 5:
        print("ขอบคุณที่ใช้บริการค่ะ")
        exit(0)
    else:
        print("******************************")
        print("กรุณาเลือกตัวเลข 1-3 ด้วยค่ะ")
        print("******************************")
        print("\n")
def edit_labtop_price():
    print("คุณต้องการแก้ไขราคาหรือไม่?: ")
    display_laptop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n} or type 10 to main option:? "))
        if s in range(1, n + 1):
            print(f'ราคาเดิม: {my_labtop[s-1].get_price()}')
            newprice = float(input("ระบุราคาใหม่"))
            my_labtop[s-1].set_price(newprice)
            print("\nอัพเดตราคาเรียบร้อย.\n")
            break
        elif s == 0:
            break
        else:
            print(f"please, select number 1-{n} or type 0 to main option.")



def delete_labtop():
    print("คุณต้องการลบข้อมูลหรือไม่ ?: ")
    display_laptop()
    n = len(my_labtop)
    s = 1
    while s:
        s = int(input(f"select(1-{n} or type 10 to main option:? "))
        if s in range(1,n+1):
            my_labtop.pop(s-1)
            print("\nAlready delete labtop data.\n")
            break
        elif s ==0:
            break
        else:
            print(f"please, select number 1-{n} or type 0 to main option.")



def input_laptop_data(): #รับข้อมูล
    brand = input("Enter Labtop Brand: ")
    model = input("Enter Labtop Model: ")
    cpu = input("Enter Labtop CPU: ")
    ram = int(input("Enter Labtop RAM(GB): "))
    display = float(input("Enter Labtop Display(inch): "))
    storage = int(input("Enter Labtop Storage(GB): "))
    price = float(input("Enter Labtop Price: "))

    l = labtop("","","",0,0,0,0)

    l.set_brand(brand)
    l.set_model(model)
    l.set_cpu(cpu)
    l.set_ram(ram)
    l.set_display(display)
    l.set_storage(storage)
    l.set_price(price)

    #return no, brand, model, cpu, ram, display, storage, price #return as tuple
    #my_labtop.append(labtop(brand, model, cpu, ram, display, storage, price))
    my_labtop.append(l)
    print("******************************")
    print("เพิ่มสินค้าเรียบร้อยแล้วค่ะ")
    print("******************************")
    print("\n")

my_labtop = []
my_labtop.append(labtop("ASUS","Vivobook 15x","intel corei5-12500H","8","15.6","512","27990"))
my_labtop.append(labtop("Lenovo","idesPad Grameming", "intelcorei5-11320h","8","15.6","512","25990"))
my_labtop.append(labtop("Aser","Swift","intel corei7-1260P","8","14","512","33990"))
s = 0
while s == 0:
    display_option_system()
