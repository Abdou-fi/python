# def sum_all(*args):
#     """ Sum all given arguments. """
#     return sum(args)

# total = sum_all(8, 1, 2, 3, 4, 5, 6, 7, 8) 
# print(total)

def get_average(*numbers): 
    if numbers: 
        print(sum(numbers) / len(numbers))
    else: print("No numbers provided.")

get_average(4, 6, 8, 10)
get_average(1, 2, 3) 
get_average(10, 20, 30, 40, 50) 
get_average(7, 14) 
get_average()