# Write a Python program to find the repeated items of a tuple. 

t = (12,3,43,65,65,12,4)

l1=list(t)
li=[]

print("Repeated Elements are : ")

for i in l1:
    if i not in li:
        li.append(i)
    else:
        print(i)