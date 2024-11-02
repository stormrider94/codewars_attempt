def sum_cubes(n):
    sum = 0
    for i in range(n+1):
        sum += i ** 3
    print(n,sum)
    return sum