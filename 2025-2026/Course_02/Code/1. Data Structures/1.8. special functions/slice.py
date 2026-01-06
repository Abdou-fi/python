numbers:list[int] = list(range(1, 11))
text:str = "Hello, World!"
# print(numbers[::-1])
# print(text[::-1])

rev:slice=slice(None, None, -2)
first_letters=slice(None, 3)

print(numbers[rev])
print(text[first_letters])

