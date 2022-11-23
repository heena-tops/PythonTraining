# Write a Python function to check whether a number is perfect or not.

num=int(input("Enter a number : "))

def perfect_num(x):
    sum=0

    for i in range(1,x):
        if x%i==0:
            sum+=i

    return sum==x

print(perfect_num(num))