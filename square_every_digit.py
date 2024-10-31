def square_digits(num):
    return int("".join([str(int(val) ** 2) for val in list(str(num))]))