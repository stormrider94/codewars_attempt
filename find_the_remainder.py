def remainder(a,b):
    # if both are zero
    if a == 0 and b == 0:
        return None
    larger,smaller = max(a,b),min(a,b)
    if smaller == 0:
        return None  #division by zero
    return larger % smaller