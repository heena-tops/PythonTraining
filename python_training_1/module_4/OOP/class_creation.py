# How to Define a Class in Python? What Is Self? Give An Example Of
# A Python Class


"""
    Ans : How to deine class ? 

        class creation -->

        Syntax : 
        class class_name:
            class_var..
            class_methods...

    Ans : What is self

        SELF is a keyword which is reference to the current instance
        of a class 
        and use to acces class variables 

        tip: works same as this pointer in c++
        
        
"""

#example of class is given below 

class sample:
    
    num=int(input("Enter a number : "))

    def display(self):
        print("Number : ",self.num)


obj1=sample()
obj1.display()
