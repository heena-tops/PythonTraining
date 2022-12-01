# Explain Inheritance in Python with an example? 
"""
    Inheritance : 

    The process of adapting the property and behaviour
    or characteristics of another class 

    Here two class are in IS-A relaion : 
        one of them is child class and another is parent class  

    It is the proccess of reusing the existing methods and variables
    of parent class to reduce line of code as well a to make your code
    reusable 

    Example of such class is given below  :

"""

class Add():

    def input(self,x,y):
        self.val=x+y

class Perimeter(Add):
    def per(self):
        return 2*self.val

obj=Perimeter()
obj.input(12,2)
print("Perimeter of rectangle : ",obj.per())


# What is init? Or What Is A Constructor In Python?
"""
    Ans : 

    The __int__() method is works as constructor in C++ 

    the method will automatically call when the object of such class is created

    this methos works as constructor in Python 
"""

# What is Instantiation in terms of OOP terminology?

"""
    Ans : Instantiation is refere as the term to create the object for a class 

"""


