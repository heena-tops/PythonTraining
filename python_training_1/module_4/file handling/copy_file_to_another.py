# Write a Python program to copy the contents of a file to another file.

f=open("myfile_2.txt","x")

f1=open("sales.txt",'r')

str1=str(f1)

f=open("myfile_2.txt",'a')
f.write(str1)
f.close()
