def even_last(numbers): 
    sum = 0
    if not numbers:
        return 0
    for i,val in enumerate(numbers):
        if i%2 == 0:
            sum += val
    return sum * numbers[-1]