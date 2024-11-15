def divisors(n):
    divisors_li = []
    for i in range(1,n+1):
        if n % i  == 0:
            divisors_li.append(i)
    return len(divisors_li)
            