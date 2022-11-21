# Write a Python program to print all unique values in a dictionary

L = [{'A':100}, {'B': 200}, {'C': 200}, {'D': 100}, {'E':800}]

print("Actual List: ",L)

u_value = set( val for dic in L for val in dic.values())

print("Unique Values: ",u_value)