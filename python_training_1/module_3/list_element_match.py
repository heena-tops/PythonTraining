# Write a Python function that takes two lists and returns true if they have
# at least one common member.

def li_common(x,y):
    status=False
    for i in x:
        for j in y:
            if(i==j):
                status=True
                return status


li=[12,34,6,8,56,90]

li1=[43,32,56,43,23]

print(li_common(li,li1))
