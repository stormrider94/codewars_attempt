def cube_odd(arr):
    sum = 0
    for val in arr:
        if type(val) == int:
            if val%2 == 1:
                sum += val**3
        else:
            return None
    return sum