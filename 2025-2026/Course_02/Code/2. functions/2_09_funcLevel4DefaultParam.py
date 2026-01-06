# def greet3(name, age=25):    # This function has 2 parameters, one by default
#   print(f"Hello, {name}! You are {age} years old.")
# greet3("Asmaa")
# greet3("Asmaa", 27)


# def greet4(name, age):    # This function has 2 parameters
#   print(f"Hello, {name}! You are {age} years old.")
# greet4(age=24, name="Reema")    # changing arguments order


def profile_info(username, followers=1):
    print("Username: " + username)
    print("Followers: ", followers)

profile_info(username="Samir", followers=20)

profile_info("Samir")