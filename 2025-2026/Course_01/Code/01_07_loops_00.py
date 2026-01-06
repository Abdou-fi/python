# i = 0 
# while i < 3 :
#     print(i)
#     i += 1
# else :
#     print("End of loop")


# i = 3 
# while i > 1: 
#     for j in range(2): 
#         print(i -j, end=" ") 
#     i -=1 


# x = 0 
# while x < 5 :
#     if x % 2 == 0: 
#         print("Even", end=' ') 
#     else: 
#         print("Odd", end=' ') 
#     x += 1 
    
#     #Answer --< clcoding.com (ID - 01201125) 
#     # A. EOEOE 
#     # 8. OEOEO 
#     # C. EEEEO 
#     # D. EOOEE



#Python Coding Challenge-Question With Answer 
# total = 0 
# for i in range(1, 4):
#     j = i 
#     while j > 0: 
#         total += (i + j) 
#         j -= 2
# print(total) 


# i = 1
    # j = 1         i+j=2
    # total = 2
# i = 2
    # j = 2         i+j=4
    # total = 6
# i = 3
    # j = 3        i+j=6
    # total = 12
    # j = 1        i+j=4
    # total = 16





""" def print_multiplication_table(n): 
    for i in range(1, 11): 
        for j in range(1, n+1): 
            print(i * j, end='\t') 
        print() 
mul = int(input("Enter the number you want the table for : ")) 
print_multiplication_table(mul)
 """




""" def check(num):
    # Compute sum of digits
    digitSum = 0
    while num > 0:
        rem = num % 10
        digitSum = digitSum + rem
        num = num // 10
    # Check if sum of digits is divisible by 3.
    return (digitSum % 3 == 0)
    
# main function
num = 1332
if check(num):
    print("Yes")
else:
    print("No") """