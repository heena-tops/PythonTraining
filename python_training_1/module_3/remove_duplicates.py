# Write a Python program to remove duplicates from a list.

li = [23,43,3,3,54,23,67,43,76,9,4]

unique_li = []

for i in li:
    if i not in unique_li:
        unique_li.append(i)

print(unique_li) 