# Write a Python program to check a list is empty or not.

def Empty_list(x):
    if (len(x)==0):
        return "List is empty"

    else:
        return "List is not Empty"

li = [23,43,65,78,9,5,3]
lis1 = []
li1 = ['Name']

print(Empty_list(li))
print(Empty_list(lis1))
print(Empty_list(li1))