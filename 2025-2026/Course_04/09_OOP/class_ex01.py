from math import cos, sin, pi
import matplotlib.pyplot as plt

class parallelogram():
        
    def __init__(self, x0:float, y0:float, length:float, width:float, angle: float):
        self.length = length
        self.width = width
        height= width * sin(angle)
        self.superficy = length * height
        self.point_A_x, self.point_A_y = x0, y0
        self.point_B_x, self.point_B_y = x0 + length, y0
        self.point_C_x, self.point_C_y = x0 + length + width * cos(angle), y0 + width * sin(angle)
        self.point_D_x, self.point_D_y = x0 + width * cos(angle), y0 + width * sin(angle)

    def draw_parallelogram(self):
        data = [[self.point_A_x, self.point_A_y], [self.point_B_x, self.point_B_y], [self.point_C_x, self.point_C_y], [self.point_D_x, self.point_D_y], [self.point_A_x, self.point_A_y]]
        plt.plot(*zip(*data))
        plt.show()
        plt.close()

    def print_superficy(self):
        print("The superficy of the parallelogram is: ", self.superficy)
        
parallelogram1 = parallelogram(2, 2, 9, 4, pi/9)
parallelogram1.draw_parallelogram()
parallelogram1.print_superficy()

class rectangle(parallelogram):
    def __init__(self, x0:float, y0:float, length:float, width:float):
        super().__init__(x0, y0, length, width, pi/2)   
rectangle1 = rectangle(0, 0, 10, 4)
rectangle1.print_superficy()
rectangle1.draw_parallelogram()


4


