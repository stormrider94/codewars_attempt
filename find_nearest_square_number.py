import math
def nearest_sq(n):
    if str(math.sqrt(n)).split(".")[1] == 0:
        return sqrt(n)
    else:
        a = math.floor((math.sqrt(n)))
        b = math.ceil(math.sqrt(n))
        return a**2 if abs(a**2 - n) < abs(b**2 - n) else b**2