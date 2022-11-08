a = input("Enter first string : ")

b = input("Enter second string : ")

print(a)
print(b)

a_new = b[:2]+a[2:]
b_new = a[:2]+b[2:]

print("New string : ",a_new," ",b_new)