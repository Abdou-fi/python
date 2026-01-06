# #Create a new list 
# x = [1, "x", 3.1415] 
# y = list(x)
# y[0]="s"
# print(x)
# print(y)
# print(id(x))
# print(id(y))



# # indexing
# x1= [1, 2, 3] 
# x1[0]       #1 
# x1[1]       #2 
# x1[-1]      #3 
# print(x1[-2] )     #2


# # Length of List 
# xs = [1, 2, 1, 2] 
# length = len(xs)    # length = 4
# print(length)


# # Assignment 
# xs = [1, 1, 1] 
# print(xs)
# xs[-1] = 2 
# xs[0] = 'r'
# print(xs)
# # xs = [2, 1, 2]



# # Append 
# xs = [1, 1] 
# ys = [3, 4] 
# xs.append(2)    # xs = [1, 1, 2] 
# xs.append(ys)   # xs = [1, 1, 2, [3, 4]]
# print(xs[3][0])






# # Extend 
# xs = [1, 2] 
# ys = [3, 4] 
# xs.extend(ys)  # xs =[1, 2, 3, 4]



# # Insert 
# xs = [1, 3] 
# xs.insert(1, "f")     # xs = [1, "f", 3] 
# print(xs)


# # Remove 
# xs = [1, 2, 3] 
# xs.remove(2)    # xs =[1, 3]
# print(xs)


# # Slicing
# #      0    1    2    3    4
# xs = ['a', 'b', 'c', 'd', 'e']
# # print(xs[1:3] )   # ['b', 'c']
# # print(xs[:3])     # ['a', 'b', 'c']
# # print(xs[3:]    )      # ['d', 'e']
# print(xs[:]   )        # [1, 2, 3, 4, 5]
# print(xs[::2] )        # [1, 3, 5]
# print(xs[::-1] )       # [5, 4, 3, 2, 1]
# print(xs[::]  )        # [1, 2, 3, 4, 5]
# xs[1:3] = [8, 9, 10] ; print(xs)  
# xs[1:3] = [] ; print(xs) 






# # Slicing 
# start = 5 
# stop = 15 
# step = 2 
# xs = list(range(20))    # [0, 1, 2, ..., 19]
# print(xs[start:stop:step])   # [5, 7, 9, 11, 13]






# # min/max
# xs = [1, 2, 3] 
# print( min(xs) )    
# print( max(xs)     )


# # sum
# xs = [1, 8, -2] 
# S = sum(xs)     
# print(S)


# # Sort ascendint
# xs = [3, 1, 4, 2] 
# xs.sort()
# # xs = [1, 2, 3, 4]


# # Sort descending
# xs = [3, 1, 4, 2] 
# xs.sort(reverse=True)
# # xs = [4, 3, 2, 1]
# print(xs)