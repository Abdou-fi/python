class rectangle:
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        self.superficy = length * width

rec1=rectangle(2, 3)
rec2=rectangle(6, 10)
print("length is ", rec1.length)
print("width is ", rec1.width)
print("length is ", rec2.length)
print("superficy is ", rec2.superficy)
print("superficy is ", rec1.superficy)



class square(rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        
sq1=square("Square 1", 4)
print("length is ", sq1.length)
print("width is ", sq1.width)
print("superficy is ", sq1.superficy)