def check_age(age): 
    if age < 13:
        raise ValueError("Age cannot be less than 13.") 
    elif age < 18: 
        print("You are not old enough.")
    else: 
        print("You are welcome.")
try: 
    user_age = int(input("Enter your age: ")) 
    check_age(user_age)
except ValueError as e: 
    print("Error:", e)