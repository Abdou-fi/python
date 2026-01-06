global_var = 10 
def some_function():
  my_variable=global_var
  local_var = 5 
  print(global_var + local_var) 
some_function()



def greet2(name:str , age:int):    # This function has 2 parameters
  name = "John"  # This is an assigned default value for name
  print(f"Hello, {name}! You are {age} .")

greet2("Amine", 25)