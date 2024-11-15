import math
def nb_dig(n, d):
    d_count = 0
    squares = [x**2 for x in range(n+1)]
    for sq in squares:
        if str(d) in str(sq):
            d_count += str(sq).count(str(d))
    return d_count