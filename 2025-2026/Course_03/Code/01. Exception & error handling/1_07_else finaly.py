# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.



# many errors
# X="gggg"
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")
  

# else
# You can use the else keyword to define a block of code to be executed if no errors were raised:
# x=10
# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
  
# # Finally
# # The finally block, if specified, will be executed regardless if the try block raises an error or not.
# x="Hello"
# try:
#   print(x)
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
# finally:
#   print("The 'try except' is finished")
  
  
# Python code to illustrate 
# working of try()  
def divide(x, y): 
    try: 
        # Floor Division : Gives only Fractional 
        # Part as Answer 
        result = x // y 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
    else:
        print("Yeah ! Your answer is :", result) 
    finally:  
        # this block is always executed   
        # regardless of exception generation.  
        print('This is always executed')   

# Look at parameters and note the working of Program 
divide(3, 0)
divide(3, 2) 

"https://github.com/Abdou-fi/python/tree/main/2025-2026/Course_03"