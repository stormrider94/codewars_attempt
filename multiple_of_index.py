def multiple_of_index(arr):
    vals = []
    for i,val in enumerate(arr):
        if i != 0 and (val%i == 0):
            vals.append(val)
        elif i==0 and val==0:
            vals.append(0)
    return vals