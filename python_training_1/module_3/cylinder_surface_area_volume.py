# Write a Python program to calculate surface volume and area of a
# cylinder

# A cylinder's volume is π r² h, and its surface area is 2π r h + 2π r².

r=float(input("Enter value of radius : "))

h=float(input("Enter value of height : "))

pi=3.14

volume=pi*(r**2)*h

surface_area=(2*pi*r*h)+(2*pi*(r**2))

print("Volume of Cylinder : ",volume)
print("Surface area of Cylinder : ",surface_area)
