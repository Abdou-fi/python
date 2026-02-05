class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.superficy = length * width
        self.circonference = 2 * (length + width)

rec1=rectangle(2,3)
rec2=rectangle(6,10)
print("rectangle 1 length is ".ljust(32)+":", rec1.length)
print("rectangle 1 width is ".ljust(32)+":", rec1.width)
print("rectangle 2 length is ".ljust(32)+":", rec2.length)
print("rectangle 2 superficy is ".ljust(32)+":", rec2.superficy)
print("rectangle 1 circonference is ".ljust(32)+":", rec1.circonference)
print("rectangle 2 circonference is ".ljust(32)+":", rec2.circonference)



