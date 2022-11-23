# Write a Python function that checks whether a passed string is
# palindrome or not 

str1=input("Enter a string ")

def palindrom(x):
    if x[0:]==x[::-1]:
        return "string is Palindrom "
    else:
        return "Not a Palindrom !!!"


print("Result : ",palindrom(str1))
        