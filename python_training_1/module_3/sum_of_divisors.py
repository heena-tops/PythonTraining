# Write a Python program to returns sum of all divisors of a number 

num=int(input("enter a number : "))
sum=0
for i in range(1,num+1):
    
    if num%i==0:
        print(i)
        sum+=i

print("Sum of All Divisors : ",sum)
