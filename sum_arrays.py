def sum_array(a):
    sum = 0
    if not a: 
        return 0
    for num in a:
        sum += num
    return sum