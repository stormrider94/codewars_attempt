def array_madness(a,b):
    sum_a,sum_b = 0,0
    for val in a:
        sum_a += val**2
    for val in b:
        sum_b += val**3
    return sum_a > sum_b