# first two numbers
num1, num2 = 0, 1

print("Fibonacci sequence:")
# run loop 10 times
for i in range(10):
    # print next number of a series
    print(num1, end="  ")
    # add last two numbers to get next number
    res = num1 + num2

    # update values
    num1 = num2
    num2 = res

    # iteration 1 -> 0 1
    # iteration 2 -> 1 1
    # iteration 3 -> 1 2
    # iteration 4 -> 2 3
    # iteration 5 -> 3 5
    # iteration 6 -> 5 8
    # iteration 7 -> 8 13
    # iteration 8 -> 13 21
    # iteration 9 -> 21 34
    


