# When will the else part of try-except-else be executed? 
"""
    Ans :The else part is executed when no exception occurs.
"""

# Can one block of except statements handle multiple exception? 
"""
    Ans :Yes, it is possible, Each type of exception can be specified directly.

"""

# When is the finally block executed? 
"""
    Ans :
    --> finally block is always executed after leaving the try statement.
    In case if some exception was not handled by except block, it is
    re-raised after execution of finally block.

    --> finally block is used to deallocate the system resources.
    One can use finally just after try without using except block,
    but no exception is handled in that case.
"""

# What happens when „1‟== 1 is executed? 

"   Ans : it will give false bcz one element is string and another is integer"

# How Do You Handle Exceptions With Try/Except/Finally In Python?

"""
    Ans : 

    The try......except allow you to catch one or more exceptions
    and handle it in exception block
        --> in try : block there is the code which may have some exceptions
        --> in except : block it handle the exception occoured in try block
        --> finally : block will always excecute however the exception is
            occoured or not.

"""

# Explain with coding snippets.


num1 = int(input("Enter fist number : "))
num2 = int(input("Enter second number : "))
try :
    ans = num1 / num2
    print("Answer is : ",ans)
except Exception as e:
    print("Error : ",e)
finally :
    print("Finished")