def sum_even_numbers(seq):
    sum = 0
    for val in seq:
        if val%2 == 0:
            sum+=val
    return sum