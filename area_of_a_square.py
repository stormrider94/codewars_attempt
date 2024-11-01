import math
def square_area(A):
    radius = 2*A / math.pi
    area = radius ** 2
    return float("{:.2f}".format(area))