# What is used to check whether an object o is an instance of class A?

"""
    Ans : 
    
    isinstance() : 
            method used to check for the object that is it relate
            to such class or not ?
"""

class Temp:

    num=12

    def display(self):
        print(self.num)

obj=Temp()

print(isinstance(obj,Temp))