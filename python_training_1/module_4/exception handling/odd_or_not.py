# Write python program that user to enter only odd numbers, else will
# raise an exception.

num=int(input("enter any odd number : "))

try:
    assert num%2!=0
except Exception as e:

    print("Error : ",e)

