import math
class Circle:
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius 
        
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        
def circle_area(circle):
    return round(math.pi * circle.radius **2,6)