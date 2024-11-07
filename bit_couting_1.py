def count_bits(n):
    quotient = n
    count_ones = 0
    while quotient!= 0:
        remainder = quotient%2
        quotient = quotient//2
        if remainder ==1:
            count_ones += 1
    # after quotient becomes equal to 1 we just return the number of ones
    return count_ones