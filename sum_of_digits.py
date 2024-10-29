def digital_root(n,sum=0):
    if len(str(n)) == 1:
        return n
    for dig in str(n):
        sum += int(dig)
    return digital_root(sum)