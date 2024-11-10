def divisions(n, divisor):
    quotient=n
    count=0
    while quotient>=divisor:
        if quotient//divisor:
            quotient//=divisor
            count+=1
    return count