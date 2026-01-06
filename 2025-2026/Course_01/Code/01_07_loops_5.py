# Example 2 : User input until correct

password=""
while password != "1234":
    password = input("Enter your password : ")
    if password == "1234":
        print("Password is correct")
    else:
        print("Password is incorrect")