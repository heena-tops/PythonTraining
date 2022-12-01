# Write a Python class named Circle constructed by a radius and two
# methods which will compute the area and the perimeter of a circle

r=float(input("Enter radius : "))

class Rectangle:

    def __init__(self,x):
        self.radius=x
        self.pi=3.14

    def perimeter(self):
        return self.radius*2*self.pi

    def area(self):
        self.r2=self.radius**2
        return self.r2*self.pi


obj=Rectangle(r)
print("Perimeter of Circle : ",obj.perimeter())
print("Area of Circle : ",obj.area())

