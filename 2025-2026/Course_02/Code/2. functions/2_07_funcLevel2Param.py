"""
def greet1(name: str)->None :   # This function greets to the person passed in as a parameter
  print("Hello,", name)
greet1("Ahmed")


"""

# Define function with parameters
def profile_info(username, followers):
    print("Username:", username, " - Followers:", followers)
    
x = "Abdesselam"
y = 40
profile_info(x, y)
profile_info("Sammy", 945)
profile_info(username="Rahim", followers=342)
profile_info(followers=999, username="Rahim")
