# Write a Python program to append text to a file and display the text

f=open("myfile.txt","w")

f.write("Have a nice day")
f.write("\nHope you arte well")
f.write("\nHello")
f.write("\nHappy Buddies")
f.write("\nHungry tummy")

f.close()


f=open("myfile.txt","r")
print(f.read())
f.close()