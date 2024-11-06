import functools
def square_sum(numbers):
    if not numbers: 
        return 0
    return functools.reduce(lambda x,y : x + (y**2),numbers,0)
    