# Write a Python program to read first n lines of a file.

f = open("myfile.txt", "r")

print(f.readline(200))

f.close()