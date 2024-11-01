import math
def round_it(n):
    len_left,len_right = len(str(n).split('.')[0]),len(str(n).split('.')[1])
    if len_left < len_right:
        return math.ceil(n)
    elif len_right < len_left:
        return math.floor(n)
    else:
        return round(n)