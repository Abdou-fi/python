# 2. Write a program to generate a random password with the following conditions:
# a. The password must contain at least one uppercase letter, one lowercase letter, one number, and one special character.  
# b. The user should be able to specify the length of the password.
# c. The program should ensure that the generated password meets the specified conditions.
import random
import string
length = int(input("Enter the length of the password: "))
password = ""
if length < 4:
    print("Password length should be at least 4 to meet all conditions.")
else:
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    if length > 4:
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password += ''.join(random.choices(all_characters, k=length - 4))
    password_list = list(password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)
    print(f"The generated password is: {final_password}")