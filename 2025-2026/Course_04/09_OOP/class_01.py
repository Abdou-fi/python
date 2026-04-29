class rectangle:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.superficy = length * width

rec1=rectangle("Rectangle 1", 2, 3)
rec2=rectangle("Rectangle 2", 6, 10)
print(rec1.name,"length is ", rec1.length)
print(rec1.name,"width is ", rec1.width)
print(rec2.name,"length is ", rec2.length)
print(rec2.name,"superficy is ", rec2.superficy)
print(rec1.name,"superficy is ", rec1.superficy)



class square(rectangle):
    def __init__(self, name, side_length):
        super().__init__(name, side_length, side_length)
        
sq1=square("Square 1", 4)
print(sq1.name,"length is ", sq1.length)
print(sq1.name,"width is ", sq1.width)
print(sq1.name,"superficy is ", sq1.superficy)