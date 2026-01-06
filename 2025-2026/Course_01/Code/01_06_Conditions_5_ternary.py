# example of ternary condition

# syntax: <expression_if_true> if <condition> else <expression_if_false>

# example 1
x = 10
y = 20
# if x > y, assign x to max, else assign y to max
max = x if x > y else y
print(max)  # output: 20

# example 2
age = 18
can_vote = "yes" if age >= 18 else "no"
print(can_vote)  # output: yes

# example 3
num = 5
is_even = "even" if num % 2 == 0 else "odd"
print(is_even)  # output: odd



