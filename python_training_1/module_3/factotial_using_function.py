# Write a Python function to calculate the factorial of a number



num = int(input("Enter a number : "))

def fact(x):
    f=1
    for i in range(1,x+1):
        f*=i

    return f

print("Factorial of ",num," is : ",fact(num))
