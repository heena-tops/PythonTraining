# Write a Python script to sort (ascending and descending) a dictionary by value
dic = {
'A':1,
'B':4,
'C':3,
'D':2,
}

l1 = sorted(dic.items(), key=lambda x:x[1])
sortdict = dict(l1)
print(sortdict)