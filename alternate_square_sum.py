def alternate_sq_sum(arr):
    total = 0
    for i,val in enumerate(arr):
        i = i+1
        if i%2 == 0:
            total += val**2
        else:
            total += val
    return total