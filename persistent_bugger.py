def is_one_digit_len(num):
    return len(str(num)) == 1

def persistence(n, count=0):
    if is_one_digit_len(n):
        return count
    
    product = 1
    for digit in str(n):
        product *= int(digit)
    
    return persistence(product, count + 1)