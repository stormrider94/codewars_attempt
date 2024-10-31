def sum_digits(number):
    sum = 0
    for val in list(str(abs(number))):
        sum += int(val)
    return sum