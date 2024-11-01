def sum_mul(n, m):
    if m<= 0 or n<=0:
        return "INVALID"
    sum = 0
    for i in range(m):
        if i%n == 0:
            sum+= i
    return sum
    