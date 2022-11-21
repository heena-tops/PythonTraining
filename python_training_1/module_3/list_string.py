# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
# list of strings.

li = ["OrangesO","twt","Apple","Mango"]
str_count=0
for i in li:

    if(len(i)>=2) and i[0]==i[-1]:
        str_count+=1

print("No.  of such string : ",str_count)
