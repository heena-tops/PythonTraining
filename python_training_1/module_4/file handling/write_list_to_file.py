# Write a Python program to write a list to a file

#--------------------First method--------------------------

#to write content to file
l1=['Hi...','Have ','a ','good ','day']

f=open("list_file.txt","w")

for i in l1:
    f.write(i)

f.close()

# to read the list content from the file 
f=open("list_file.txt","r")

print(f.read())

f.close()


#----------------------------Scond method --------------------------

l = ["apple","banana","oranges"]
str1=str(l)

f = open("myfile.txt","a")
f.write(str1)
f.close()

f = open("myfile.txt","r")
print(f.read())
f.close()