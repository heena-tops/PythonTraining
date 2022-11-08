# Write a python program to sum of the first n positive integers.

num = int(input("Enter a number : "))
add=0

for num in range(1,num+1):
    add+=num

print("Addition = ",add)

