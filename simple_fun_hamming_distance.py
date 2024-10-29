def hamming_distance(a, b):
    count = 0
    a_bin = bin(a).split('0b')[1]
    b_bin = bin(b).split('0b')[1]
    max_len = max(len(a_bin),len(b_bin))
    a_bin = a_bin.zfill(max_len)
    b_bin = b_bin.zfill(max_len)
    for bit_a, bit_b in list(zip(a_bin,b_bin)):
        if bit_a != bit_b:
            count += 1
    return count