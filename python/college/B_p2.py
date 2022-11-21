class Rectangle:
    def __init__(self):
        self.rect_area=0
        self.rect_peri=0
        self.l=0
        self.w=0
    def rectArea(self):
        self.l=int(input("\nEnter lenght of rectangle to find the area: "))
        self.w=int(input("Enter width of rectangle to find the area: "))
        self.rect_area=self.l*self.w
    def perimeter(self):
        self.l=int(input("\nEnter lenght of rectangle to find the perimeter: "))
        self.w=int(input("Enter width of rectangle to find the perimeter: "))
        self.rect_peri=2*self.l+2*self.w
class box(Rectangle):
    def __init__(self):
        super().__init__()
        self.volume=0
        self.h=0
        self.box_peri=0
    def box_volume(self):
        self.l=int(input("\nEnter lenght of box to find the volume: "))
        self.w=int(input("Enter width of box to find the volume: "))
        self.h=int(input("Enter height of the box to find the volume: "))
        self.volume=self.l*self.w*self.h
    def perimeter(self):
        super().perimeter()
        self.l=int(input("\nEnter lenght of box to find the perimeter: "))
        self.w=int(input("Enter width of box to find the perimeter: "))
        self.h=int(input("Enter height of the box to find the perimeter: "))
        self.box_peri=4*(self.l+self.w+self.h)
    def disBox(self):
        print("\n---Rectanle---")
        print("Area of rectangle: ",self.rect_area)
        print("Perimeter of rectangle: ",self.rect_peri)
        print("\n---Box---")
        print("Volume of box: ",self.volume)
        print("Perimeter of box: ",self.box_peri)
b=box()
b.rectArea()
b.perimeter()
b.box_volume()
b.disBox()