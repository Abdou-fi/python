class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.superficie = length * width

rec1=rectangle(2,3)
rec2=rectangle(6,10)
print(rec1.length)
print(rec1.width)
print(rec2.length)
print(rec2.superficie)
print(rec1.superficie)



