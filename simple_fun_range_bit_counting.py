def range_bit_count(a, b):
    count_ones = 0
    for x in range(a,b+1):
        binary_representation = bin(x)
        count_ones += binary_representation.count("1")
    return count_ones