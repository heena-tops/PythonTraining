# character frequency

val=input("Enter a string : ")

freq_count={}
for i in val:
    if i in freq_count:
        freq_count[i]+=1

    else:
        freq_count[i]=1

print("Frequency of a charcater in string is : ",freq_count)