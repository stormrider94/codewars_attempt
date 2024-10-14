def unused_digits(*numbers):
    unused = ""
    numbers = "".join([str(number) for number in numbers])
    for val in "0123456789":
        if val not in numbers:
            unused+= val
    return unused