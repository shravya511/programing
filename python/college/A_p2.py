def rectangle():
    w=int(input("Enter the width of rectangle: "))
    h=int(input("Enter the height of rectangle: "))
    area_of_rec=w*h
    print(f"The area of rectangle is: {area_of_rec}\n")
def square():
    a=int(input("Enter the side lenght of square: "))
    area_of_sq=a*a
    print(f"The area of square is: {area_of_sq}\n")
def circle():
    r=int(input("Enter the radius of circle: "))
    area_of_cir=3.14*r*r
    print(f"The area of rectangle is: {area_of_cir}\n")
def triangle():
    b=int(input("Enter the breath of triangle: "))
    h=int(input("Enter the height of triangle: "))
    area_of_tri=(1/2)*b*h
    print(f"The area of triangle is: {area_of_tri}\n")
while True:
    print("Choose your option")
    print("1. To Find The Area Of Rectangle ")
    print("2. To Find The Area Of Square ")
    print("3. To Find The Area Of Circle ")
    print("4. To Find The Area Of Triangle ")
    print("5. To Exit ")
    i=int(input("Enter your choice: "))
    if i==1:
        rectangle()
    elif i==2:
        square()
    elif i==3:
        circle()
    elif i==4:
        triangle()
    elif i==5:
        break
    else:
        print("Enter valid choise!\n\n")