def same_order_but_different_digits(n,k1,k2):
    digits_k1 = sorted(str(n * k1))
    digits_k2 = sorted(str(n * k2))
    return digits_k1 == digits_k2

def find_lowest_int(k):
    k1 = k
    k2 = k1 + 1
    n = 1
    while not same_order_but_different_digits(n,k1,k2):
        n += 1
    print(sorted(str(n*k1)))
    print(sorted(str(n*k2)))
    return n