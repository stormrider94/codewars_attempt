def narcissistic( value ):
    result = 0
    number_of_digits = len(str(value))
    for dig in str(value):
        result += int(dig) ** number_of_digits
    return result == value