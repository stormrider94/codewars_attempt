import math
# sorting_function 
def check_shape(val):
    if type(val) is tuple:
        return val[0] * val[1]
    else:
        return math.pi * val ** 2 
def sort_by_area(seq):
    return sorted(seq,key=check_shape)