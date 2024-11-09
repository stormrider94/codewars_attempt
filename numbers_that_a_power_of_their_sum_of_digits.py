def power_sumDigTerm(n):
    series = [0]
    for a in range(2,99):
        for b in range(2,42):
            c = a**b
            if a ==sum(map(int,str(c))):
                series.append(c)
    term = sorted(series).__getitem__
    return term(n)