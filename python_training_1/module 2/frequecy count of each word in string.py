# frequecy count of each word in string 

string = input("Enter a string : ")

dic = {}
words = string.split()

for i in words:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

print(dic)