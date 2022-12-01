# Write a Python class named Rectangle constructed by a length and
# width and a method which will compute the area of a rectangle

l=float(input("Enter Length : "))
w=float(input("Enter width : "))

class Rectangle:

    def __init__(self,x,y):
        self.length=x
        self.width=y

    def area(self):
        return self.length*self.width


obj=Rectangle(l,w)
print("Area of Rectangle : ",obj.area())

