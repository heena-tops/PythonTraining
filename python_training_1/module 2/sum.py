#Write a Python program to sum of three given integers. However, if
# two values are equal sum will be zero.

x=int(input("Enter a number : "))
y=int(input("Enter a number : "))
z=int(input("Enter a number : "))

def sum(a,b,c):
    sum = a+b+c
    if(a==b or a==c or b==c):
        return 0
    else:
        return sum

print(sum(x,y,z))
