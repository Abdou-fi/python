# Finding Even Numbers ina List Way
#  1: Using a for loop 
def pairs_for(list): 
    pairs = [] 
    for num in list: 
        if num % 2 == 0:
            pairs.append(num)
        return pairs 
print(pairs_for([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#  2: Using List Comprehension
def pairs_list_comprehension(list):
    return [num for num in list if num % 2 == 0]
print(pairs_list_comprehension([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))