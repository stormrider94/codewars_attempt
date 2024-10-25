import math
def square_or_square_root(arr):
    return_li = []
    for val in arr:
        if math.sqrt(val) == round(math.sqrt(val)):
            return_li.append(int(math.sqrt(val)))
        else:
            return_li.append(val**2)
    print(arr,return_li)
    return return_li